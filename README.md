# 2Engine

# Test work
Тестовое задание. 
Система управления задачами.

## Запуск проекта

### Создайте файл .env
Пример:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<ключ в одинарных ковычках>
```

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Ivanmatv/2Engine.git
    cd test_work
    ```

2. Запустите Docker:
    ```bash
    docker-compose up --build
    ```

3. Примените миграции:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Доступ к Flower:
    Откройте `http://localhost:5555` для доступа к Flower.

5. Остановить работу всех контейнеров командой:
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
