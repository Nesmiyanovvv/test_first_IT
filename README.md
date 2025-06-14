# 💼 Тестовое задание для Первая IT-компания

ДДС (движение денежных средств) — это процесс учета, управления и анализа
поступлений и списаний денежных средств компании или частного лица.

ссылка на демо-версию: https://drive.google.com/file/d/11wGjuVqgmIqUJjWVTb3IWI7HtMlmjxxj/view?usp=sharing  
в фильтрации записей также работают логические зависимости
---

## Инструкция по запуску

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Nesmiyanovvv/test_first_IT.git
cd test_first_IT
```

### 2. Создать виртуальное окружение и активировать
```bash
python -m venv venv
source venv/bin/activate       # для Linux/macOS
venv\Scripts\activate          # для Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```
### 4. Применить миграции базы данных
```bash
python manage.py migrate
```
### 5. Создать суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:

Username (leave blank to use 'admin'): admin  
Email address: admin@admin.com  
Password: не показывается, но пишется  
Superuser created successfully.

### 6. Запустить сервер разработки
```bash
python manage.py runserver
```
Откройте в браузере: http://127.0.0.1:8000/


