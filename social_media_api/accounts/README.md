# Project Setup

## Clone the repository:

git clone https://github.com/DannyTechStudio/Alx_DjangoLearnLab.git
cd project_dir


## Create and activate a virtual environment:

python -m venv env
# On Windows
.\env\Scripts\activate
# On macOS/Linux
source env/bin/activate


## Install dependencies:

Environment & Dependencies

Python 3.10+
Django 6.0
Django REST Framework
djangorestframework.authtoken

Make sure to add the following apps to INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'users',
]

## Database Migration

Run the following commands to apply migrations:

python manage.py makemigrations
python manage.py migrate

Running the Server

Start the development server:

python manage.py runserver

Your API will be available at http://127.0.0.1:8000/.


## User Authentication

The API uses DRF Token Authentication. Each registered user is issued a unique token to access protected endpoints.

Register a User

Endpoint: POST /api/auth/register/
Request Body:

{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "strongpassword",
  "bio": "Hello, I'm John!",
  "profile_picture": "<image-file>"
}


Response:

{
  "user": {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "bio": "Hello, I'm John!"
  },
  "token": "<user-token>"
}

Login

Endpoint: POST /api/auth/login/
Request Body:

{
  "username": "johndoe",
  "password": "strongpassword"
}


Response:

{
  "user": {
    "username": "johndoe",
    "email": "johndoe@example.com"
  },
  "token": "<user-token>"
}

Retrieve Profile

Endpoint: GET /api/auth/me/
Headers: Authorization: Token <user-token>

Response:

{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "bio": "Hello, I'm John!",
  "profile_picture": "http://127.0.0.1:8000/media/profiles/johndoe.png"
}

Logout

Endpoint: POST /api/auth/logout/
Headers: Authorization: Token <user-token>

Response:

{
  "detail": "Logout successful"
}


Note: Logout deletes the token, so the user must log in again to receive a new token.