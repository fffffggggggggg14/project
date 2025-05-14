from rest_framework import serializers
from .models import Todo, Task, Image
from django.db import transaction

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        with transaction.atomic():
            task = Task.objects.create(**validated_data)
            # if 'condition':
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

class TodoSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'