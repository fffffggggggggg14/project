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

