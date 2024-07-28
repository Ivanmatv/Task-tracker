from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import process_task


class Task(models.Model):

    STATUS = (
        ('В очереди', 'В очереди'),
        ('В процессе', 'В процессе'),
        ('Завершена', 'Завершена')
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=200
        )
    descriptions = models.TextField(
        verbose_name='Descriptions',
        max_length=400
    )
    status = models.CharField(
        verbose_name='Status',
        max_length=15,
        choices=STATUS
    )
    data_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data creation'
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self) -> str:
        return f'{self.name}'


@receiver(post_save, sender=Task)
def start_task_processing(sender, instance, created, **kwargs):
    if created:
        process_task.delay(instance.id)
