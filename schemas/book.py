from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

# Book
# ---------------------------
class BookBase(BaseModel):
    Title: str
    Publication_Year: int
    Edition: str

class BookCreate(BookBase):
    Book_id: str
    Publisher_id: str

class BookUpdate(BaseModel):
    Title: Optional[str] = None
    Publication_Year: Optional[int] = None
    Edition: Optional[str] = None
    Publisher_id: Optional[str] = None

class Book(BookBase):
    Book_id: str
    Publisher_id: str
    class Config:
        orm_mode = True
    