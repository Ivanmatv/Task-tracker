# индексирование задачь
from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

connections.create_connection()


class TaskIndex(Document):
    title = Text()
    description = Text()
    created_at = Date()

    class Index:
        name = 'tasks'

    def save(self, **kwargs):
        return super().save(**kwargs)
