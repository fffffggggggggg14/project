from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Todo

@receiver(post_save, sender=Todo)
def update_task_status(sender, instance, **kwargs):
    task = instance.task
    all_todos_completed = True
    for todo in task.todos.all():
        if not todo.is_completed:
            all_todos_completed = False
            break

    if all_todos_completed:
        task.status = 'done'
    else:
        task.status = 'in_progress'

    task.save()