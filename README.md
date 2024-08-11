# Task_trecker

# Description
System of management tasks.

## Launch project 

### Creat file .env
Example:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<the key is in single quotes>
```

1. Clone repository:
    ```bash
    git clone https://github.com/Ivanmatv/2Engine.git
    cd 2Engine
    ```

2. Launch Docker:
    ```bash
    docker-compose up --build
    ```

3. Launch migrations:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Access to Flower:
    ```
    http://localhost:5555`
    ```

5. Stop the operation of all containers with the command:
    ```
    docker-compose down
    ```

## Примеры API запросов

- Создание задачи:
    ```bash
    curl -X POST http://localhost:8000/api/tasks/ -d '{"name": "New Task", "description": "Task description"}' -H "Content-Type: application/json"
    ```

- Получение списка задач:
    ```bash
    curl http://localhost:8000/api/tasks/
    ```

- Обновление задачи:
    ```bash
    curl -X PUT http://localhost:8000/api/tasks/1/ -d '{"name": "Updated Task", "description": "Updated description", "status": "completed"}' -H "Content-Type: application/json"

- Удаление задачи:
    ```bash
    curl -X DELET http://localhost:8000/api/tasks/{id}/ 

### Использумые технологии:

- Python
- Django
- Django Rest Framework
- PostgreSQL
- Сelery
- Flower
- Elasticsearch
- Docker
