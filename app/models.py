from django.db import models
from PIL import Image
import os


class Todo(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Task(models.Model):
    choices = [
            ('new', 'new'),
            ('in_progress', 'in_progress'),
            ('done', 'done'),
        ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    task = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='new',)

    image = models.ImageField(upload_to='todo_images/', blank=True, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            image_path = self.image.path
            img = Image.open(image_path).convert('RGB')
            webp_path = os.path.splitext(image_path)[0] + '.webp'
            img.save(webp_path, 'webp')
            if not self.image.name.endswith('.webp'):
                os.remove(image_path)
                self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
                self.save(update_fields=['image'])

    def __str__(self):
        return self.title
