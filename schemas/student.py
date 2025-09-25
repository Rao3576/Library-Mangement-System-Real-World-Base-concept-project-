from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

# ---------------------------
# Student
# ---------------------------
class StudentBase(BaseModel):
    student_name: str
    Email: EmailStr
    Address: str
    Status: bool

class StudentCreate(StudentBase):
    student_id: str

class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    Email: Optional[EmailStr] = None
    Address: Optional[str] = None
    Status: Optional[bool] = None

class Student(StudentBase):
    student_id: str
    class Config:
        orm_mode = True