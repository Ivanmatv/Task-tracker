from django.test import TestCase

from tasks.models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        # Create a Task instance for testing
        self.task = Task.objects.create(
            name="Test Task",
            descriptions="This is a test task.",
            status="In a queue"
        )

    def test_task_creation(self):
        """We check that the task is created correctly"""
        self.assertIsInstance(self.task, Task)
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.descriptions, "This is a test task.")
        self.assertEqual(self.task.status, "В очереди")
        self.assertIsNotNone(self.task.data_creation)

    def test_task_str_method(self):
        """Check that the __str__ method returns the correct value"""
        self.assertEqual(str(self.task), "Test Task")

    def test_task_status_choices(self):
        """We check that the task status corresponds to one of the acceptable values"""
        valid_statuses = dict(Task.STATUS).keys()
        self.assertIn(self.task.status, valid_statuses)

    def test_task_name_max_length(self):
        """We check that the length of the name field does not exceed 200 characters"""
        max_length = self.task._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_task_descriptions_max_length(self):
        """We check that the descriptions field length does not exceed 400 characters"""
        max_length = self.task._meta.get_field('descriptions').max_length
        self.assertEqual(max_length, 400)
