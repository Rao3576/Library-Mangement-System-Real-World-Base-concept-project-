from fastapi import FastAPI
from database import Base, engine
from starlette.middleware.sessions import SessionMiddleware
from config.config import settings
from routes.student import router as students_routes
from routes.book import router as books_routes
from routes.publishers import router as publishers_routes
from routes.report import router as report_routes
from routes.author import router as author_routes
from routes.employee import router as employee_routes
from routes.bookstatus import router as bookstatus_routes
from routes.transaction import router as transaction_routes
from routes.borrowing import router as borrowing_routes
from routes.return_record import router as return_record_routes
from routes.book_author import router as book_author_routes
from routes.master_lookup import router as master_lookup_routes
from routes.book_eligibility import router as book_eligibility_routes
from routes.auth_user import router as auth_user_routes 
from models import *
from routes.google_auth import router as google_auth_routes
from routes.role import router as role_routes

#books, authors, employees, publishers, borrowings, returns, transactions, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API")


# ✅ Allow CORS
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",   # if using React/Next frontend
    "http://127.0.0.1:3000"
]

# 🔐 Add this middleware BEFORE including routes
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY
)

app.include_router(students_routes)
app.include_router(books_routes)
app.include_router(publishers_routes)
app.include_router(report_routes)
app.include_router(author_routes)
app.include_router(employee_routes)
app.include_router(transaction_routes)
app.include_router(bookstatus_routes)
app.include_router(return_record_routes)
app.include_router(borrowing_routes)
app.include_router(book_author_routes)
app.include_router(master_lookup_routes)
app.include_router(book_eligibility_routes)
app.include_router(auth_user_routes)
app.include_router(google_auth_routes)
app.include_router(role_routes)

# ✅ Root endpoint
@app.get("/")
def home():
    return {"message": "Library Management System API is running with OAuth2 + JWT authentication"}
# app.include_router(authors.router)
# app.include_router(employees.router)
# app.include_router(publishers.router)
# app.include_router(borrowings.router)
# app.include_router(returns.router)
# app.include_router(transactions.router)
# app.include_router(reports.router)
