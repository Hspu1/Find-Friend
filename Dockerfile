# Используем официальный образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY pyproject.toml poetry.lock* ./

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Устанавливаем зависимости проекта
RUN poetry install --no-root --no-interaction --no-ansi

# Копируем исходный код
COPY . .

# Команда для запуска приложения
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
