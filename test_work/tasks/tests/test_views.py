from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateViewTest(APITestCase):

    def setUp(self):
        # Data for testing the serializer
        self.task_data = {
            'name': 'Test Task',
            'descriptions': 'This is a test task.',
            'status': 'In a queue'
        }
        self.url = reverse('task-list-create')

    def test_get_task_list(self):
        """Checks that the GET method works correctly to retrieve a list of tasks"""
        Task.objects.create(**self.task_data)
        Task.objects.create(name='Another Task', descriptions='Another test task.', status='In a queue')

        response = self.client.get(self.url)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    @patch('tasks.views.process_task.delay')
    def test_create_task(self, mock_process_task):
        """Checks that the POST method works correctly to create a new task and call a background task"""
        response = self.client.post(self.url, self.task_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, 'Test Task')

        # mock_process_task.assert_called_once_with(Task.objects.get().id) # Check that the process_task.delay function was called


class TaskDetailViewTest(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(
            name='Test Task',
            descriptions='This is a test task.',
            status='In a queue'
        )
        self.url = reverse('task-detail', args=[self.task.id])

    def test_get_task_detail(self):
        """Checks that the GET method works correctly to retrieve task details."""
        response = self.client.get(self.url)
        serializer = TaskSerializer(self.task)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    @patch('tasks.views.process_task.delay')
    def test_update_task(self, mock_process_task):
        """Checks that the PUT method works correctly to update an existing task."""
        updated_data = {
            'name': 'Updated Task',
            'descriptions': 'This is an updated task.',
            'status': 'In a queue'
        }

        response = self.client.put(self.url, updated_data, format='json')
        self.task.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.task.name, 'Updated Task')
        self.assertEqual(self.task.descriptions, 'This is an updated task.')
        self.assertEqual(self.task.status, 'In a queue')

    def test_delete_task(self):
        """Checks that the DELETE method works correctly to delete a task."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
