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








---

## 🌟 Features

✔ JWT Authentication
✔ Role-Based Access (Admin, Student, Employee, Borrower)
✔ CRUD Operations for students, employees, borrowers
✔ Master Lookup System (Authors, Publishers, Categories, Languages, Locations)
✔ Complete Book Management
✔ Issue / Return / Fine Calculation System
✔ Reservation Queue
✔ Activity Logs (Login & Operations)
✔ Alembic Migrations
✔ Clean Layered Architecture
✔ Fully documented APIs
✔ SQL relational database using SQLAlchemy ORM

---

# 🧰 Tech Stack

| Category        | Technology                        |
| --------------- | --------------------------------- |
| **Language**    | Python 3.x                        |
| **Framework**   | FastAPI                           |
| **Database**    | SQL (PostgreSQL / MySQL / SQLite) |
| **ORM**         | SQLAlchemy                        |
| **Migrations**  | Alembic                           |
| **Auth System** | JWT (Access Tokens)               |
| **Validation**  | Pydantic                          |
| **Dev Tools**   | Uvicorn, Postman, Virtualenv      |

---

# 📁 Project Structure (Exact From Your Repo)

```
Library-Mangement-System-Real-World-Base-concept-project-/
│
├── alembic/                 # Migration scripts
│   ├── versions/
│   │   ├── 292cff..._create_base_tables.py
│   │   ├── 5f8ab0..._add_employee_and_role_tables.py
│   │   ├── f6e0c7..._create_book_and_details_tables.py
│   │   └── ffb218..._add_activity_logs_table.py
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── config/              # Config files
│   ├── controllers/         # Business Logic (one per entity)
│   ├── database/            # DB connection & BaseModel
│   ├── logs/                # Activity logger
│   ├── middleware/          # Auth middleware
│   ├── models/              # ORM Models
│   ├── routes/              # API Route files
│   ├── schemas/             # Request / Response Schemas
│   └── services/            # Core Services
│
├── utils/                   # Helper functions (JWT, hashing)
├── main.py                  # FastAPI Entry Point
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Rao3576/Library-Mangement-System-Real-World-Base-concept-project-
cd Library-Mangement-System-Real-World-Base-concept-project-
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables (`.env`)

```
DATABASE_URL=sqlite:///./library.db
JWT_SECRET=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5️⃣ Run database migrations

```bash
alembic upgrade head
```

### 6️⃣ Start the server

```bash
uvicorn main:app --reload
```

Now open Swagger UI ➝
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

# 🔐 Authentication (JWT)

### Login Flow

```
User → /auth/login
Backend verifies email + password
→ Generates JWT access token
→ User sends token in Authorization header
```

### Protected Routes Example

Send header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 📌 API Documentation (Beginner-Friendly + Clear)

## 🔐 1. Authentication

### **POST /auth/register**

Creates new user (student, employee, borrower).

### **POST /auth/login**

Returns **JWT token** on successful login.

### **GET /auth/me**

Get logged-in user profile.
*(Protected)*

### **GET /auth/logout**

Logout user (client-side token removal).

---

# 🧾 2. Master Lookup APIs

These are simple tables used across entire system.

### **Authors**

* GET /authors
* POST /authors
* PUT /authors/{id}
* DELETE /authors/{id}

### **Publishers**

* GET /publishers
* POST /publishers
* PUT /publishers/{id}
* DELETE /publishers/{id}

### **Categories**

* GET /categories
* POST /categories
* PUT /categories/{id}
* DELETE /categories/{id}

### **Languages**

* GET /languages
* POST /languages

### **Locations**

* GET /locations
* POST /locations

---

# 👥 3. Users Module

(Students, Employees, Borrowers)

All follow same structure:

### **Students**

* GET /students
* POST /students
* GET /students/{id}
* PUT /students/{id}
* DELETE /students/{id}

### **Employees**

* GET /employees
* POST /employees
* GET /employees/{id}
* PUT /employees/{id}
* DELETE /employees/{id}

### **Borrowers**

* GET /borrowers
* POST /borrowers
* GET /borrowers/{id}
* PUT /borrowers/{id}
* DELETE /borrowers/{id}

---

# 📚 4. Books Module

### **POST /books**

Create new book with all metadata (author, publisher, category).

### **GET /books**

List all books.

### **GET /books/{id}**

Book details.

### **PUT /books/{id}**

Update book.

### **DELETE /books/{id}**

Delete book.

---

# 🔁 5. Issue / Return / Fine System

### **POST /issue**

Issue a book to a user.
System checks:

* Is book available?
* Is borrower valid?
* Is quantity > 0?

### **POST /return**

Return a book.
System:

* Calculates fine (if late)
* Increases book quantity
* Updates issue record

### **GET /issues**

List of all issued books.

---

# 📊 6. Activity Logs

Every login & important action logs into:

```
models/login_activity.py
```

and stored in DB for auditing.

---

# 📘 ERD (Database Diagram)

```
Users (Student/Employee/Borrower)
        |
        | 1-to-1
Borrowers
        |
        | 1-to-many
Issues -------- Books -------- Authors
                |               |
                |               |
             Category       Publisher
```

---

# 🔄 High-Level Flow (Beginner Friendly)

```
User Registers/Login → Gets JWT Token  
↓  
User Browses Books → Issues Book  
↓  
Book Quantity Decreases  
↓  
User Returns Book → Fine Calculated  
↓  
Admins Manage: Authors, Publishers, Categories, Users, Books  
↓  
Logs stored for security & tracking  
```

---

# 🧩 Why This Project Is Special

✔ Real-world backend architecture
✔ Clean separation of controllers, services, models
✔ Alembic migrations (professional DB management)
✔ SQLAlchemy relationships
✔ Activity logging
✔ JWT-based role management
✔ Easy for beginners to understand
✔ Perfect as a portfolio project

---

# 🤝 Contribution

1. Fork repo
2. Create branch
3. Commit & push
4. Open Pull Request

---






