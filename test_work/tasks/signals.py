from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import process_task


@receiver(post_save, sender=Task)
def start_task_processing(sender, instance, created, **kwargs):
    if created:
        process_task.delay(instance.id)
