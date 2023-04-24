#API Yatube

## Описание проекта

Этот проект решает проблему передачи данных между сервисом Yatube и другими сервисами с помощью REST API.
---

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/daniil-orlovv/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```
или
```
python -m venv venv
```

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
