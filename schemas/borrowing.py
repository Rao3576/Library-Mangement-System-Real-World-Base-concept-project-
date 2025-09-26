from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional




# Borrowing
# ---------------------------
class BorrowingBase(BaseModel):
    Borrow_date: date
    Due_date: date

class BorrowingCreate(BorrowingBase):
    Borrowing_id: str
    Student_id: str
    Book_id: str
    Employee_id: str

class BorrowingUpdate(BaseModel):
    Borrow_date: Optional[date] = None
    Due_date: Optional[date] = None
    Student_id: Optional[str] = None
    Book_id: Optional[str] = None
    Employee_id: Optional[str] = None

class Borrowing(BorrowingBase):
    Borrowing_id: str
    Student_id: str
    Book_id: str
    Employee_id: str
    class Config:
        orm_mode = True

