# Blog Application

## Overview
A simple blog application built with Django and Django REST Framework. It supports CRUD operations for posts and comments, token-based authentication, pagination, and likes.

---

## Features
- Create, Read, Update, and Delete posts.
- Add comments to posts.
- User authentication using tokens.
- Pagination for posts.
- Like and count likes for posts.

---

## Setup and Installation
### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment tool (optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/roselinrani1303/blog-application.git
   ```
2. Move to the project folder:
   ```bash
   cd blog-application
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the application:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Posts
- **GET** — Get all posts:
  ```
  http://127.0.0.1:8000/posts
  ```
- **GET** — Get a post by ID:
  ```
  http://127.0.0.1:8000/posts/<id>
  ```
- **POST** — Add a new post:
  ```
  http://127.0.0.1:8000/posts
  ```
- **PUT** — Update an existing post:
  ```
  http://127.0.0.1:8000/posts/<id>
  ```
- **DELETE** — Delete a post:
  ```
  http://127.0.0.1:8000/posts/<id>
  ```

### Comments
- **GET** — Get all comments:
  ```
  http://127.0.0.1:8000/comments
  ```
- **POST** — Add a new comment:
  ```
  http://127.0.0.1:8000/comments
  ```

---

## Database
This application uses an SQL database for storing data related to posts, comments, and user information.

---

## Sample Output

### My SQL Workbench

![My SQL Workbench](output_images/o1.jpeg)

### Employee Table

![Employee Table](output_images/o2.jpeg)

### Add Employee

![Add Employee](output_images/o3.jpeg)

### Employee Added

![Employee Added](output_images/o4.jpeg)

### Update Employee

![Update Employee](output_images/o5.jpeg)

---

## Repository
[GitHub Repository](https://github.com/roselinrani1303/blog-application.git)
