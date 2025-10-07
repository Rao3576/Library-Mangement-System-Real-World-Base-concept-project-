from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import auth_user
from repositories.auth_user import UserQuery

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

# ✅ Forgot Password – send reset link
@router.post("/forgot-password")
def forgot_password(request_data: auth_user.PasswordResetRequest, db: Session = Depends(get_db)):
    return UserQuery.send_reset_password_email(request_data.email, db)


# ✅ Reset Password – update password using token
@router.post("/reset-password")
def reset_password(payload: auth_user.ResetPassword, db: Session = Depends(get_db)):
    return UserQuery.reset_user_password(payload.token, payload.new_password, db)





