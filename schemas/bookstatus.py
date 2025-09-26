from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional




# BookStatus
# ---------------------------
class BookStatusBase(BaseModel):
    Status: str
    Last_update: datetime

class BookStatusCreate(BookStatusBase):
    Status_id: str
    Book_id: str

class BookStatusUpdate(BaseModel):
    Status: Optional[str] = None
    Last_update: Optional[datetime] = None
    Book_id: Optional[str] = None

class BookStatus(BookStatusBase):
    Status_id: str
    Book_id: str
    class Config:
        orm_mode = True