## Сайт для лаборатории

### Технологический Стек
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)

### Используемые технологии:
- Python 3.8.10
- Django==2.2.19
- Pillow==8.3.1

## Установить venv 
``` python3.8 -m venv venv ```

## Активировать venv 
``` source venv/bin/activate ```

## Обновить менеджер пакетов pip 
``` python3 -m pip install --upgrade pip ```

## Установить все зависимости из requirements 
``` pip install -r requirements.txt ```

### Создать миграции
``` python manage.py makemigrations ```

### Применить миграции
``` python manage.py migrate ```

### Создать суперюзера
``` python manage.py createsuperuser ```