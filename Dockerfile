FROM python:3.11-slim

RUN apt-get update -y
RUN apt-get upgrade -y

RUN mkdir /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY test_work/ /app

WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0:8000"] 
