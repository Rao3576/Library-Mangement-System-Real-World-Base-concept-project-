from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional


# BookReturn
# ---------------------------
class BookReturnBase(BaseModel):
    Return_date: date
    Condition: str

class BookReturnCreate(BookReturnBase):
    Return_id: str
    Borrow_id: str
    Employee_id: str

class BookReturnUpdate(BaseModel):
    Return_date: Optional[date] = None
    Condition: Optional[str] = None
    Borrow_id: Optional[str] = None
    Employee_id: Optional[str] = None

class BookReturn(BookReturnBase):
    Return_id: str
    Borrow_id: str
    Employee_id: str
    class Config:
        orm_mode = True