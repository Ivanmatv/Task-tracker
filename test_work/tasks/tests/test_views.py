from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateViewTest(APITestCase):

    def setUp(self):
        self.task_data = {
            'name': 'Test Task',
            'descriptions': 'This is a test task.',
            'status': 'In a queue'
        }
        self.url = reverse('task-list-create')

    def test_get_task_list(self):
        # Create several tasks for the test
        Task.objects.create(**self.task_data)
        Task.objects.create(name='Another Task', descriptions='Another test task.', status='In a queue')

        response = self.client.get(self.url)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    @patch('tasks.views.process_task.delay')
    def test_create_task(self, mock_process_task):
        response = self.client.post(self.url, self.task_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, 'Test Task')
        self.assertEqual(mock_process_task.call_count, 1)
        mock_process_task.assert_called_once_with(Task.objects.get().id) # Check that the process_task.delay function was called


class TaskDetailViewTest(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(
            name='Test Task',
            descriptions='This is a test task.',
            status='В очереди'
        )
        self.url = reverse('task-detail', args=[self.task.id])

    def test_get_task_detail(self):
        response = self.client.get(self.url)
        serializer = TaskSerializer(self.task)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    @patch('tasks.views.process_task.delay')
    def test_update_task(self, mock_process_task):
        updated_data = {
            'name': 'Updated Task',
            'descriptions': 'This is an updated task.',
            'status': 'В процессе'
        }

        response = self.client.put(self.url, updated_data, format='json')
        self.task.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.task.name, 'Updated Task')
        self.assertEqual(self.task.descriptions, 'This is an updated task.')
        self.assertEqual(self.task.status, 'В процессе')

    def test_delete_task(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
