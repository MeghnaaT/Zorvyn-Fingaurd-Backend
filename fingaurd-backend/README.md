# FinGuard – Secure Finance Analytics Backend

## Overview

FinGuard is a backend system built to manage financial transactions securely and provide useful insights through analytics. The project focuses on implementing authentication, role-based access control, and structured API design rather than just basic CRUD operations.

---

## Features

* User registration and login using JWT authentication
* Role-based access control (admin and user)
* Secure password hashing using bcrypt
* Transaction management (create, update, delete, view)
* Filtering transactions by type and category
* Financial summary (income, expense, balance)
* User-specific data isolation (each user accesses only their data)
* Admin override (admin can access all users' data)
* Interactive API testing using Swagger UI

---

## Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* python-jose (JWT handling)
* passlib (bcrypt hashing)

---

## Project Structure

```
app/
 ├── api/routes/        # API endpoints
 ├── models/            # Database models
 ├── schemas/           # Request/response schemas
 ├── services/          # Business logic
 ├── dependencies/      # Auth & DB dependencies
 ├── db/                # Database setup
 └── main.py            # Entry point
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/<MeghnaaT>/finguard-backend.git
cd finguard-backend
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the server

```
uvicorn app.main:app --reload
```

---

### 5. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## Authentication Flow

1. Register a user using `/auth/register`
2. Login using `/auth/login`
3. Copy the access token
4. Click **Authorize 🔒** in Swagger
5. Paste token as:

   ```
   Bearer <your_token>
   ```
6. Access protected endpoints

---

## API Endpoints

### Auth

* POST `/auth/register`
* POST `/auth/login`

### Transactions

* POST `/transactions`
* GET `/transactions`
* PUT `/transactions/{id}`
* DELETE `/transactions/{id}`

### Analytics

* GET `/analytics/summary`

---

## Test Credentials

```
Admin:
admin@test.com / 123456

User:
user@test.com / 123456
```

---

## Key Design Decisions

* JWT is used for stateless authentication
* Dependency-based role checks enforce access control
* Transactions are scoped per user for data security
* Admin override allows full system visibility
* Business logic is separated into services for clarity

---

## Notes

This project is designed to demonstrate backend fundamentals such as authentication, authorization, database handling, and API structuring. It can be extended with features like pagination, advanced analytics, or deployment configurations.

---

## Author

Meghna Tiwari
