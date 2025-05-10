from django.db import models

class Task(models.Model):
    choices = [
            ('new', 'new'),
            ('in_progress', 'in_progress'),
            ('done', 'done'),
        ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='new',)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='todos')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    