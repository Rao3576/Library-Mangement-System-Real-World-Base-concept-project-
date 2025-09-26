from fastapi import FastAPI
from database import Base, engine
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

#books, authors, employees, publishers, borrowings, returns, transactions, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API")

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



# app.include_router(authors.router)
# app.include_router(employees.router)
# app.include_router(publishers.router)
# app.include_router(borrowings.router)
# app.include_router(returns.router)
# app.include_router(transactions.router)
# app.include_router(reports.router)
