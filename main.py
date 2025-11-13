from fastapi import FastAPI,Request
from database import Base, engine
from fastapi.templating import Jinja2Templates 
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from config.config import settings
from routes.web_soucket_auth import router as web_soucket_auth_routes
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
from routes.user_role import router as user_role_routes
from routes.permission import router as permission_routes 
from routes.chat import router as chat_routes





#books, authors, employees, publishers, borrowings, returns, transactions, reports

Base.metadata.create_all(bind=engine)



app = FastAPI(title="Library Management API")


# ✅ Add SessionMiddleware (required for OAuth state)
# Session middleware (must be present and have same secret_key)
# ✅ Correct session middleware (must be before OAuth)

# ✅ Session Middleware (must be before all routes)
# app.add_middleware(
#     SessionMiddleware,
#     secret_key=settings.SECRET_KEY,
#     same_site="lax",     # ensures cookies sent even cross-tab
#     https_only=False,    # for localhost
#     max_age=3600,
# )
# ✅ Add session middleware (MUST come before include_router)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")



# # ✅ Example root
# @app.get("/")
# async def root():
#     return {"message": "Library Management System API is running with OAuth2 + JWT"}

# # ✅ Dashboard route
# @app.get("/dashboard")
# async def dashboard(request: Request):
#     user_email = request.session.get("user_email", "Guest")
#     return templates.TemplateResponse("dashboard.html", {"request": request, "user_email": user_email})




# # ✅ Template folder path
# templates = Jinja2Templates(directory="templates")



# # ✅ Allow CORS
# origins = [
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
#     "http://localhost:3000",   # if using React/Next frontend
#     "http://127.0.0.1:3000"
# ]

# # 🔐 Add this middleware BEFORE including routes
# app.add_middleware(
#     SessionMiddleware,
#     secret_key=settings.SECRET_KEY
# )

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
app.include_router(user_role_routes)
app.include_router(permission_routes)
app.include_router(chat_routes)
app.include_router(web_soucket_auth_routes)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("chat_room.html", {"request": request})


# ✅ Dashboard route
@app.get("/dashboard")
async def dashboard(request: Request):
    user_email = request.session.get("user_email", "Guest")
    return templates.TemplateResponse("dashboard.html", {"request": request, "user_email": user_email})

# # ✅ Root endpoint
# @app.get("/")
# def home():
#     return {"message": "Library Management System API is running with OAuth2 + JWT authentication"}

@app.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie("access_token")  # optional: clear session or token
    return response


# app.include_router(authors.router)
# app.include_router(employees.router)
# app.include_router(publishers.router)
# app.include_router(borrowings.router)
# app.include_router(returns.router)
# app.include_router(transactions.router)
# app.include_router(reports.router)
