from django.db import models


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
        max_length='400'
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
