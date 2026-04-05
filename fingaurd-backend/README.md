FinGuard – Secure Finance Analytics Backend
Overview

FinGuard is a backend system designed to manage personal financial data securely. It provides APIs for handling transactions and generating useful insights such as total income, expenses, and balance.

The system focuses on security, clean architecture, and scalability rather than just basic CRUD functionality.

Key Features
User registration and login using JWT authentication
Role-based access control (admin vs user)
Secure password storage using bcrypt hashing
Transaction management (create and retrieve data)
Analytics endpoint for financial summaries
Integrated API documentation using Swagger UI
Tech Stack
FastAPI
SQLAlchemy
SQLite
python-jose (JWT handling)
passlib (password hashing)
How to Run
Clone the repository
git clone https://github.com/<your-username>/finguard-backend.git
cd finguard-backend
Create and activate virtual environment
python -m venv venv
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Start the server
uvicorn app.main:app --reload
Open API docs
http://127.0.0.1:8000/docs
Authentication Flow
Register a user
Login to receive an access token
Use the Authorize button in Swagger
Access protected endpoints
API Endpoints
Auth
POST /auth/register
POST /auth/login
Transactions
POST /transactions
GET /transactions
Analytics
GET /analytics/summary (admin only)
Project Structure

The project follows a modular backend structure:

Routes → API endpoints
Models → Database schema
Services → Business logic
Dependencies → Auth and DB handling

This separation keeps the codebase clean and maintainable.

Notes

This project was built as a backend-focused system to demonstrate secure API design, authentication handling, and structured development practices.

Author: Meghna Tiwari