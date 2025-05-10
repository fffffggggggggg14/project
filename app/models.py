from django.db import models
    
class Task(models.Model):
    task = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task

class Todo(models.Model):
    title = models.CharField(max_length = 255)
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    