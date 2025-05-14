from rest_framework import serializers
from .models import Todo, Task, Image
from django.db import transaction
import re

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


###################################################################################################


class TaskSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate_national_id(self, value):
        if value:
            if not value.isdigit():
                raise serializers.ValidationError("رقم البطاقة يجب أن يحتوي على أرقام فقط.")
            if len(value) != 16:
                raise serializers.ValidationError("رقم البطاقة يجب أن يكون 16 رقمًا.")
        return value

    def validate_phone_number(self, value):
        if value:
            if not value.isdigit():
                raise serializers.ValidationError("رقم التليفون يجب أن يحتوي على أرقام فقط.")
            if len(value) != 11:
                raise serializers.ValidationError("رقم التليفون يجب أن يكون 11 رقمًا.")
            if not re.match(r'^(010|012|015)\d{8}$', value):
                raise serializers.ValidationError("رقم التليفون يجب أن يبدأ بـ 010 أو 012 أو 015.")
        return value

    def validate_marital_status(self, value):
        if value not in [choice[0] for choice in Task.MARITAL_STATUS_CHOICES]:
            raise serializers.ValidationError("الحالة الاجتماعية يجب أن تكون إما 'single' أو 'married'.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        with transaction.atomic():
            task = Task.objects.create(**validated_data)
            # if not request.FILES.getlist('images'):
            #     transaction.set_rollback(True)
            for image in request.FILES.getlist('images'):
                Image.objects.create(task=task, image=image)
            return task

    @transaction.atomic
    def update(self, instance, validated_data):
        request = self.context.get('request')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        for image in request.FILES.getlist('images'):
            Image.objects.create(task=instance, image=image)
        return instance


##############################################################################################################


class TodoSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'