from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomAdmin
from .serializers import CustomAdminSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str


class CustomAdminListCreateView(generics.ListCreateAPIView):
    queryset = CustomAdmin.objects.all()
    serializer_class = CustomAdminSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CustomAdminRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomAdmin.objects.all()
    serializer_class = CustomAdminSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response_data = {
            "user": serializer.data,
            "access_token": access_token,
            "refresh_token": str(refresh),
        }

        return Response(response_data, status=status.HTTP_201_CREATED)







User = get_user_model()

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("لا يوجد مستخدم بهذا البريد الإلكتروني.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("كلمتا المرور غير متطابقتان.")
        return data


class PasswordResetRequestView(generics.CreateAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)

        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        context = {
            'user': user,
            'domain': settings.DOMAIN,
            'uid': uidb64,
            'token': token,
        }

        subject = "إعادة تعيين كلمة المرور"
        html_message = render_to_string('password_reset_email.html', context)
        send_mail(subject, html_message, settings.DEFAULT_FROM_EMAIL, [email], html_message=html_message)

        return Response({"message": "تم إرسال بريد إلكتروني لإعادة تعيين كلمة المرور."}, status=status.HTTP_200_OK)



class PasswordResetConfirmView(generics.CreateAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uidb64 = serializer.validated_data['uidb64']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({"message": "تم تغيير كلمة المرور بنجاح."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "رابط إعادة تعيين كلمة المرور غير صالح."}, status=status.HTTP_400_BAD_REQUEST)


