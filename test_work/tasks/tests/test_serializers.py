from django.test import TestCase
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskSerializerTest(TestCase):

    def setUp(self):
        # Data for testing the serializer
        self.task_data = {
            'name': 'Test Task',
            'descriptions': 'This is a test task.',
            'status': 'In a queue'
        }

        self.invalid_task_data = {
            'name': '',  # name can't be empty
            'descriptions': 'This is a test task.',
            'status': 'Incorrect status'  # Incorrect status
        }

        self.task = Task.objects.create(**self.task_data)

    def test_task_serializer_valid_data(self):
        """Check serialization with correct data"""
        serializer = TaskSerializer(data=self.task_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], self.task_data['name'])
        self.assertEqual(serializer.validated_data['descriptions'], self.task_data['descriptions'])
        self.assertEqual(serializer.validated_data['status'], self.task_data['status'])

    def test_task_serializer_invalid_data(self):
        """Checking serialization with incorrect data"""
        serializer = TaskSerializer(data=self.invalid_task_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertIn('status', serializer.errors)

    def test_task_serializer_contains_expected_fields(self):
        """Check that the serializer contains all the required fields"""
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data
        self.assertEqual(set(data.keys()), {
            'id',
            'name',
            'descriptions',
            'status',
            'data_creation'
        })

    def test_task_serializer_field_content(self):
        """Checking the correctness of the contents of the serializer fields"""
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data
        self.assertEqual(data['name'], self.task.name)
        self.assertEqual(data['descriptions'], self.task.descriptions)
        self.assertEqual(data['status'], self.task.status)
        self.assertEqual(
            data['data_creation'][:-1], self.task.data_creation.isoformat()[:-6]
        )
