dockerfile
# Используем легкий образ Python
FROM python:3.10-slim

# Устанавливаем системные зависимости для работы с Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Копируем весь код проекта
COPY . .

# Собираем статику (нужно для админки)
RUN python manage.py collectstatic --noinput

# Команда для запуска сервера через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DjangoAPI.wsgi:application"]