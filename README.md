#API Yatube

## Описание проекта

Этот проект решает проблему передачи данных между сервисом Yatube и другими сервисами с помощью REST API.

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/daniil-orlovv/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать виртуальное окружение:

```
python3 -m venv env
```
или
```
python -m venv venv
```

Активировать виртуальное окружение:

```
source env/bin/activate
```
или
```
source venv/scripts/activare
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов

*Получение всех постов:*

GET-запрос на `http://127.0.0.1:8000/api/v1/posts/`

*Получение определенног поста:*

GET-запрос на `http://127.0.0.1:8000/api/v1/posts/1`, где 1 - id поста

*Создание поста:*

POST-запрос на `http://127.0.0.1:8000/api/v1/posts/`

В теле запроса:

JSON:
```
{
  "text": "Текст поста"
}
```
