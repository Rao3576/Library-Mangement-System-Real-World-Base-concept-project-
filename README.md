# Library-Mangement-System-Real-World-Base-concept-project-
**Library Management System – FastAPI, OAuth2 & JWT**

🚀 A modern Library Management System built using FastAPI, featuring JWT authentication, Google OAuth2 login, and Role-Based Access Control (RBAC).
This project follows a clean modular architecture, separating routes, queries, models, schemas, and utilities for scalability and maintainability.

**🧩 Key Features**

**✅ User Authentication System**

Register users with email verification

Login using JWT tokens

Secure password hashing with bcrypt

**✅ OAuth2 + Google Login**

Sign in with Google using authlib

Automatically generates access & refresh tokens

**✅ Role-Based Access Control (RBAC)**

Admin, Manager, and Student roles

Access control using role dependencies

**✅ Token System**

JWT-based authentication

Refresh token endpoint

Logout endpoint to invalidate tokens

**✅ Swagger UI Documentation**

Auto-generated API documentation

Interactive testing via /docs

**✅ Clean Project Architecture**

Routes, Queries, Models, Schemas, and Utils organized separately


| Component              | Technology            |
| ---------------------- | --------------------- |
| **Framework**          | FastAPI               |
| **Database ORM**       | SQLAlchemy            |
| **Database**           | MySQL                 |
| **Authentication**     | JWT + OAuth2 (Google) |
| **Email**              | SMTP + `itsdangerous` |
| **Password Hashing**   | Passlib (bcrypt)      |
| **Environment Config** | python-dotenv         |





**🧩 API Endpoints Summary**

| Category                  | Method | Endpoint                      | Description     |
| ------------------------- | ------ | ----------------------------- | --------------- |
| **Authentication_System** | POST   | `/user/register`              | Register user   |
|                           | GET    | `/user/verify-email`          | Verify email    |
|                           | POST   | `/user/login`                 | User login      |
| **OAuth2 & JWT**          | GET    | `/Oauth/auth/google`          | Google login    |
|                           | GET    | `/Oauth/auth/google/callback` | Google callback |
|                           | POST   | `/Oauth/refresh-token`        | Refresh token   |
|                           | POST   | `/Oauth/logout`               | Logout user     |
| **Roles**                 | GET    | `/roles/`                     | Read roles      |
|                           | POST   | `/roles/`                     | Create role     |



**🏆 About This Project**

This FastAPI-based Library Management System demonstrates a production-level architecture with authentication, authorization, and OAuth2 integration.
It’s suitable for learning, extending to full enterprise applications, or showcasing as a professional portfolio project.



