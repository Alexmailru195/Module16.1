# Project setup

1. Создайте виртуальное окружение:
   python3 -m venv venv
   source venv/bin/activate

2. Установите зависимости:
   pip install -r requirements.txt

3. Создайте файл .env на основе .env_sample

4. Выполните миграции:
   python manage.py migrate

5. Создайте суперпользователя:
   ./create_superuser.sh