from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        default='new',
        choices=[
            ('new', 'new'),
            ('in_progress', 'in_progress'),
            ('done', 'done'),
        ]
    )

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    