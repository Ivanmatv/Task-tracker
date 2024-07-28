# сигнал для индексации задач
from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task
from .search_indexes import TaskIndex


@receiver(post_save, sender=Task)
def index_task(sender, instance, **kwargs):
    task_index = TaskIndex(
        meta={'id': instance.id},
        title=instance.title,
        description=instance.description,
        created_at=instance.created_at
    )
    task_index.save()
