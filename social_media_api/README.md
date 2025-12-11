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

Register a User:

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


## COMMENTS API

### 1. List Comments
GET /api/comments/

### 2. Retrieve Comment
GET /api/comments/{id}/

### 3. Create Comment
POST /api/comments/
Content-Type: application/json

{
"post": 1,
"content": "Nice post!"
}

### 4. Update Comment
PUT /api/comments/{id}/

### 5. Delete Comment
DELETE /api/comments/{id}/

### API Test Requests (.http file)

### ---------------------------
### POSTS ENDPOINT TESTS
### ---------------------------

# Get first page of posts
GET http://127.0.0.1:8000/api/posts/
Accept: application/json

###
# Get second page of posts
GET http://127.0.0.1:8000/api/posts/?page=2
Accept: application/json

###
# Get posts with custom page size
GET http://127.0.0.1:8000/api/posts/?page=1&page_size=20
Accept: application/json

###
# Search posts (title or content)
GET http://127.0.0.1:8000/api/posts/?search=django
Accept: application/json

###
# Combine search + pagination
GET http://127.0.0.1:8000/api/posts/?search=api&page=2
Accept: application/json

### ---------------------------
### COMMENTS ENDPOINT TESTS
### ---------------------------

# Get comments (first page)
GET http://127.0.0.1:8000/api/comments/
Accept: application/json

###
# Get page 3 of comments
GET http://127.0.0.1:8000/api/comments/?page=3
Accept: application/json

###
# Combine search (if added later) + pagination
GET http://127.0.0.1:8000/api/comments/?search=nice&page=1
Accept: application/json

## Likes System

The Likes system lets authenticated users like or unlike posts.
Each like generates a Like object and triggers a notification for the post owner.

# Likes Endpoints
Action	Method	Endpoint	Auth Required
Like a post	POST	/api/posts/{post_id}/like/	✔
Unlike a post	POST	/api/posts/{post_id}/unlike/	✔
Get likes for a post	GET	/api/posts/{post_id}/likes/	Optional
Like a Post
POST /api/posts/{post_id}/like/
Request Headers
Authorization: Bearer <token>
Content-Type: application/json

Example Request
POST /api/posts/12/like/

Successful Response
{
  "message": "Post liked successfully",
  "post_id": 12,
  "liked": true
}

Behavior

Prevents duplicate likes

Creates a Like object

Automatically creates a notification for the post owner

Unlike a Post
POST /api/posts/{post_id}/unlike/
Example Response
{
  "message": "Post unliked successfully",
  "post_id": 12,
  "liked": false
}

Behavior

Deletes the existing Like

No notification is created

Fetch Likes for a Post
GET /api/posts/{post_id}/likes/
Example Response
{
  "post_id": 12,
  "likes_count": 3,
  "liked_by": [
    {"id": 5, "username": "danny"},
    {"id": 9, "username": "ama"},
    {"id": 11, "username": "kofi"}
  ]
}

## Notifications System

The notification system keeps users informed about important interactions.


## Unread notifications appear first.

Example Response
[
  {
    "id": 45,
    "actor": "ama",
    "verb": "liked your post",
    "target_type": "Post",
    "target_id": 12,
    "timestamp": "2025-12-11T09:33:18Z",
    "read": false
  },
  {
    "id": 46,
    "actor": "kofi",
    "verb": "commented on your post",
    "target_type": "Post",
    "target_id": 12,
    "timestamp": "2025-12-11T09:35:02Z",
    "read": false
  }
]

Mark Notification as Read
POST /api/notifications/{id}/read/
Response
{
  "message": "Notification marked as read",
  "id": 45
}

Mark All as Read
POST /api/notifications/read-all/
Response
{
  "message": "All notifications marked as read"
}

## Benefits to Users

The Likes & Notifications system enhances the platform by:

Increasing engagement:
Users receive instant feedback for likes and comments.

Improving interaction awareness:
Users always know what's happening with their posts.

Boosting social connectivity:
Notifications help build connections and keep users active.