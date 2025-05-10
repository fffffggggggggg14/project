from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=50,
        choices=[
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        ],
        default='new'
    )

    def __str__(self):
        return self.title

    def update_status(self):
        """تحديث حالة المهمة بناءً على حالة العناصر الفرعية."""
        all_todos_done = self.todo_set.filter(is_done=False).count() == 0
        if all_todos_done:
            self.status = 'done'
        elif self.todo_set.exists() and self.status != 'done':
            self.status = 'in_progress'
        elif not self.todo_set.exists():
            self.status = 'new'
        self.save()

class Todo(models.Model):
    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.task.update_status()