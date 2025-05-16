# Базовый образ Python
FROM python:3.12.9-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов
COPY . .

# Экспорт порта
EXPOSE 8005

# Команда для запуска приложения
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]
CMD ["python", "./main.py"] 
