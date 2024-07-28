from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        process_task.delay(task.id)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        process_task.delay(task.id)
