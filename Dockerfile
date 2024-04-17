FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Установка зависимостей
RUN pip install --upgrade pip
RUN pip install Django
RUN pip install Pillow

# Копирование файлов окружения в контейнер
COPY DigitalHermitag /.

WORKDIR /.

# Команда запуска вашего приложения
CMD ["python", "manage.py", "runserver", "127.0.0.1:3100"]