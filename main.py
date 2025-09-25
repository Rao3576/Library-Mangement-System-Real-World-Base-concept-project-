from fastapi import FastAPI
from database import Base, engine
from routes.student import router as students_routes
from routes.book import router as books_routes
from routes.publishers import router as publishers_routes
#books, authors, employees, publishers, borrowings, returns, transactions, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API")

app.include_router(students_routes)
app.include_router(books_routes)
app.include_router(publishers_routes)


# app.include_router(authors.router)
# app.include_router(employees.router)
# app.include_router(publishers.router)
# app.include_router(borrowings.router)
# app.include_router(returns.router)
# app.include_router(transactions.router)
# app.include_router(reports.router)
