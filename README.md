# User Management REST API

A RESTful User Management API built with FastAPI, featuring JWT authentication, bcrypt password hashing, CRUD operations, request validation, and MySQL database integration.

Click to visit : https://intern-x-tech-tasks-qf8uwk5ja-none-705d.vercel.app/docs

## 🚀 Features

- User Registration
- User Login with JWT Authentication
- Secure Password Hashing using bcrypt
- Protected API Endpoints
- Complete User CRUD Operations
- Pydantic Request/Response Validation
- MySQL Database Integration
- SQLAlchemy ORM
- Swagger UI / OpenAPI Documentation
- Environment Variable Configuration
- Docker Support
- Deployment-ready architecture

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- MySQL
- PyMySQL
- JWT (python-jose)
- bcrypt
- Uvicorn
- Docker
- Swagger / OpenAPI
- Aiven MySQL

## 📁 Project Structure

```text
week1-rest-api/
│
├── api/
│   └── index.py
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── users.py
│   │
│   ├── services/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── Dockerfile
├── README.md
├── requirements.txt
└── .gitignore
