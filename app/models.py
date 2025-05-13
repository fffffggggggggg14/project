from django.db import models
from PIL import Image as PILImage
import os

class Todo(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    choices = (
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    todo = models.ForeignKey(Todo, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=choices, default='new')

    def __str__(self):
        return self.title

class Image(models.Model):
    task = models.ForeignKey(Task, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = PILImage.open(self.image.path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            webp_path = os.path.splitext(self.image.path)[0] + '.webp'
            img.save(webp_path, 'webp')
            name_without_ext = os.path.splitext(os.path.split(self.image.name)[1])[0]
            self.image.name = f"{name_without_ext}.webp"
            self.save(update_fields=['image'])

    def __str__(self):
        return self.image.name