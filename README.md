# API_Yatube

## Description:

API_Yatube - REST API for Yatube. The application allows you to use the functionality of the Yatube project without website. (Yatube - social network for bloggers).

### Used frameworks and libraries:

- Python 3.7
- Django 2.2.16
- DRF 3.12.4
- JWT

## How to start a project (Unix):

Clone repository:
```
git clone https://github.com/ZhannaVen/api_final_yatube.git
cd api_final_yatube
```
Create and activate virtual environment:
```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```
Install dependencies from  requirements.txt:
```
pip install -r requirements.txt
```
Make migrations:
```
python3 manage.py makemigrations
```
Start project:
```
python3 manage.py runserver
```

## Sample Requests and Responses:


### Authentication:

- **Obtaining a token:**

POST request to /api/v1/jwt/create/

    {

      "username": "XXX",

      "password": "XXX"

    }

*Response Example:*

    {

      "refresh": "XXX",

      "access": "XXX"

    }

The token will be returned in the access field, and the data from the refresh field will be useful for updating token. When sending requests, pass the token in the Authorization: Bearer <token> header.

### Request examples:

- **Get all user posts:**

GET request to /api/v1/posts/

*Response Example:*


    {

      "id": 0,

      "author": "string",

      "text": "string",

      "pub_date": "2021-10-14T20:41:29.648Z",

      "image": "string",

      "group": 0

    }


- **Subscribe to a user (anonymous requests are prohibited):**

POST request to /api/v1/follow/

    {

      "following": "string"
      
    }

*Response Example:*

    {

      "user": "string",

      "following": "string"

    }

***Also see the API documentation, available at http://localhost:8000/redoc/***
