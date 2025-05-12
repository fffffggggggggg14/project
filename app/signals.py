from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Todo

@receiver(post_save, sender=Todo)
def update_task_status(sender, instance, **kwargs):
    task = instance.todo
    all_todos_completed = task.todo_set.all().count() > 0 and all(todo.is_completed for todo in task.todo_set.all())
    if all_todos_completed:
        task.status = 'done'
    else:
        task.status = 'in_progress'
    task.save()