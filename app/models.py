from django.db import models
from PIL import Image as PILImage
import os
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#######################################################################################################


class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    )
    MARITAL_STATUS_CHOICES = (
        ('single', 'أعزب'),
        ('married', 'متزوج'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    todo = models.ForeignKey(Todo, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')
    national_id = models.CharField(max_length=16, blank=True, null=True, verbose_name="رقم البطاقة")
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name="رقم التليفون")
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='single', verbose_name="الحالة الاجتماعية")

    def __str__(self):
        return self.title


#######################################################################################################


class Image(models.Model):
    task = models.ForeignKey(Task, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and hasattr(self.image, 'path') and os.path.exists(self.image.path):
            try:
                img = PILImage.open(self.image.path)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                webp_path = os.path.splitext(self.image.path)[0] + '.webp'
                img.save(webp_path, 'WEBP')
                name_without_ext = os.path.splitext(os.path.splitext(self.image.name)[0])[0]
                self.image.name = f'{name_without_ext}.webp'
                super().save(update_fields=['image'])
            except Exception as e:
                print(f"Error converting image to WEBP: {e}")

    def __str__(self):
        return self.image.name if self.image else "No Image"