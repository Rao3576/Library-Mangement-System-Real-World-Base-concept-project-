# app/schemas.py
from pydantic import BaseModel, EmailStr,Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

class UserOut(BaseModel):
    id: str          # ✅ درست — اب UUID (string) قبول کرے گا
    email: str
    is_active: bool
    is_verified: bool
    class Config:
        orm_mode = True


        
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