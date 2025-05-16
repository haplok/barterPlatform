# Бартерная платформа на Django

Веб-приложение для размещения объявлений, предложений обмена и личных сообщений между пользователями.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/haplok/barterPlatform.git
cd barterPlatform
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```
3. Установите зависимости:

```bash
pip install -r requirements.txt
```
## Инициализация базы данных
1. Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

## Запуск сервера

```bash
python manage.py runserver
```
Откройте в браузере: http://127.0.0.1:8000

## Запуск тестов
```bash
python manage.py test
```

## Стек технологий
- Python 3.8+
- Django
- SQLite

## Возможности
- Регистрация, аутентификация пользователей
- Размещение и просмотр объявлений
- Отправка предложений обмена
- Обмен сообщениями с уведомлением о непрочитанных
- Поддержка сообщений как с предложением, так и без него
- Поиск и фильтрация по объявлениям и предложениям**