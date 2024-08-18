from django.urls import reverse, resolve
from django.test import SimpleTestCase
from tasks.views import TaskListCreateView, TaskDetailView


class TestUrls(SimpleTestCase):

    def test_task_list_create_url_resolves(self):
        """
        Тестируем, что URL /tasks/ правильно разрешается на представление TaskListCreateView.
        """
        url = reverse('task-list-create')
        self.assertEqual(resolve(url).func.view_class, TaskListCreateView)

    def test_task_detail_url_resolves(self):
        """
        Тестируем, что URL /tasks/<int:pk>/ правильно разрешается на представление TaskDetailView.
        """
        url = reverse('task-detail', args=[1])  # Используем произвольный ID (например, 1)
        self.assertEqual(resolve(url).func.view_class, TaskDetailView)
