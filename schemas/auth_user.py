# app/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_verified: bool
    is_active: bool
    login_provider: str | None = None

    class Config:
        from_attributes = True  # ✅ Works for ORM models in Pydantic v2


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

# ✅ Add these for password reset flow
class PasswordResetRequest(BaseModel):
    email: EmailStr


class ResetPassword(BaseModel):
    token: str
    new_password: str