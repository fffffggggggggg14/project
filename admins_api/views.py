from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomAdmin
from .serializers import CustomAdminSerializer

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
