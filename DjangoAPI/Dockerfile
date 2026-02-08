FROM python:3.10-slim

# Установка зависимостей для Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

# Сборка статики
RUN python manage.py collectstatic --noinput

# Вместо старого CMD вставьте это:
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8000 DjangoAPI.wsgi:application

