# API_Yatube

## Описание проекта:

API_Yatube - REST API для Yatube. Приложение позволяет пользоваться функционалом проекта Yatube не заходя на сайт. 

Yatube - социальная сеть для блогеров.
### Технологии:

- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ZhannaVen/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создать миграции:

```
python3 manage.py migrate
```

Выполнить миграции:

```
python3 manage.py makemigrations
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов и ответов:


### Аутентификация:

- **Получение токена:**

POST запрос по адресу /api/v1/jwt/create/

    {

      "username": "XXX",

      "password": "XXX"

    }

*Пример ответа:*

    {

      "refresh": "XXX",

      "access": "XXX"

    }

Токен вернётся в поле access, а данные из поля refresh пригодятся для обновления токена. При отправке запроcов передавайте токен в заголовке Authorization: Bearer <токен>.

### Примеры запросов:

- **Получение всех публикаций пользователей:**

GET запрос по адресу /api/v1/posts/

*Пример ответа:*


    {

      "id": 0,

      "author": "string",

      "text": "string",

      "pub_date": "2021-10-14T20:41:29.648Z",

      "image": "string",

      "group": 0

    }


- **Подписка на пользователя(анонимные запросы запрещены):**

POST запрос по адресу /api/v1/follow/

    {

      "following": "string"
      
    }

*Пример ответа:*

    {

      "user": "string",

      "following": "string"

    }

***Также см. документацию к API, доступную по адресу http://localhost:8000/redoc/***
