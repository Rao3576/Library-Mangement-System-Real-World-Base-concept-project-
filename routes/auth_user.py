# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import get_db
# from schemas.auth_user import UserLogin
# from repositories.auth_user import AuthUserQuery
# from utils.dependencies import require_role_in

# router = APIRouter(prefix="/auth", tags=["Authentication"])

# # ✅ Public Login route
# @router.post("/login")
# def login_user(form_data: UserLogin, db: Session = Depends(get_db)):
#     return AuthUserQuery.login_user(form_data, db)


# # ✅ Example of Protected Route
# @router.get("/protected")
# def protected_route(
#     current_role: str = Depends(require_role_in(["admin", "manager"]))
# ):
#     return {"message": f"Access granted! You are logged in as {current_role}"}








from fastapi import APIRouter, Depends, Request,Form
from sqlalchemy.orm import Session
from database import get_db
from fastapi.responses import HTMLResponse, JSONResponse
from schemas import auth_user
from repositories.auth_user import UserQuery
from utils.dependencies import require_role_in


router = APIRouter(prefix="/user", tags=["Authentication_System"])


@router.post("/register")
def register(user: auth_user.UserCreate, db: Session = Depends(get_db)):
    return UserQuery.register_user(user, db)


@router.get("/verify-email")
def verify_email(token: str, db: Session = Depends(get_db)):    
    return UserQuery.verify_email(token, db)


@router.post("/login")
def login(form_data: auth_user.UserLogin, db: Session = Depends(get_db)):
    return UserQuery.login_user(form_data, db)

# ✅ Step 1: Forgot password — send link
@router.post("/forgot-password")
def forgot_password(
    email: str,
    db: Session = Depends(get_db),
    
    #current_user: str = Depends(require_role_in(["admin", "manager"]))  # 👈 Role restriction
):
    
    return UserQuery.send_reset_password_email(email, db)


# ✅ Step 2: Show HTML form when user clicks email link
@router.get("/reset-password-form", response_class=HTMLResponse)
def show_reset_password_form(request: Request, token: str):
    html_content = f"""
    <html>
    <head>
        <title>Reset Password</title>
        <style>
            body {{
                background: #f4f4f4;
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                width: 400px;
                text-align: center;
            }}
            input {{
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            button {{
                background: #007BFF;
                color: white;
                border: none;
                padding: 10px 15px;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }}
            button:hover {{ background: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Reset Your Password</h2>
            <form action="/user/reset-password" method="post">
                <input type="hidden" name="token" value="{token}">
                <input type="password" name="new_password" placeholder="Enter new password" required>
                <button type="submit">Reset Password</button>
            </form>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# ✅ Step 3: Handle new password (POST)
@router.post("/reset-password")

def reset_password(
    token: str = Form(...),
    new_password: str = Form(...),
    db: Session = Depends(get_db),
    #current_user: str = Depends(require_role_in(["admin", "manager", "user"]))  # 👈 Restrict who can reset
):


    return UserQuery.reset_user_password(token, new_password, db)