from rest_framework import serializers
from .models import CustomAdmin

class CustomAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdmin
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'date_joined']
        read_only_fields = ['date_joined']
