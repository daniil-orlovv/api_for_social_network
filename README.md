# REST API для социальной сети



# Описание

## Назначение проекта
Этот проект решает проблему передачи данных между сервисом Социальная сеть и другими сервисами с помощью REST API. Реализованы методы CRUD - чтение, запись, обвновление и удаление.

## Требования и зависимости
- **Django==3.2.16**
- **pytest==6.2.4**
- **pytest-pythonpath==0.7.3**
- **pytest-django==4.4.0**
- **djangorestframework==3.12.4**
- **djangorestframework-simplejwt==4.7.2**
- **django-filter==23.1** 
- **Pillow==9.3.0**
- **PyJWT==2.1.0**
- **requests==2.26.0**
- **djoser==2.1.0**
- **python-dotenv==1.0.0**

## Зачем был реализован проект?
Закрепление следующих знаний и навыков: `Django`, `Django REST Framework`, `JWT + Djoser` 

## Технологии
`Django REST Framework`, `Djoser`, `JWT`, `Sqlite3`


# :rocket: Инструкция по развертыванию и запуску
1. Клонируйте репозиторий на компьютер: `git clone <ссылка SSH>`
2. Создайте и активируйте виртуальное окружение: `python -m venv venv` -> `source venv/scripts/activate`
3. Установите зависимости из файла `requirements.txt`: `pip install -r requirements.txt`
4. Выполните миграции: `python manage.py migrate`
5. Перейдите в директорию с файлом `manage.py` и запустите сервер `python manage.py runserver`



# Доступные эндпоинты
- `http://127.0.0.1:8000/api/v1/posts/` - получение всех постов или создание нового(`POST`, `GET`)
- `http://127.0.0.1:8000/api/v1/posts/{post_id}` - получаем, редактируем или удаляем пост по id(`GET`, `PUT`, `PATCH`, `DELETE`)
- `http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/` - получение всех коментариев или создание нового(`GET`, `POST`)
- `http://127.0.0.1:8000/api/v1/posts/(?P<post_id>\d+)/comments/{comment_id}/` - получение, удаление, изменение комментария(`GET`, `PUT`, `PATCH`, `DELETE`)
- `http://127.0.0.1:8000/api/v1/groups/` - получение списка групп(`GET`)
- `http://127.0.0.1:8000/api/v1/groups/{group_id}` - получение информации о группе(`GET`)
- `http://127.0.0.1:8000/api/v1/follow/` - получаем или создаем подписку(`GET`, `POST`)


# Примеры запросов

**Получение всех постов:**

GET-запрос на `http://127.0.0.1:8000/api/v1/posts/`

**Получение определенног поста:**

GET-запрос на `http://127.0.0.1:8000/api/v1/posts/1/`, где 1 - id поста

**Создание поста:**

POST-запрос на `http://127.0.0.1:8000/api/v1/posts/`

В теле запроса:

  JSON:
  ```
  {
    "text": "Текст поста"
  }
  ```



# Авторы
Даниил Орлов
