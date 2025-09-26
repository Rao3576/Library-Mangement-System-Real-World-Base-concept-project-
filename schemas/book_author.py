from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional




# BookAuthor
# ---------------------------
class BookAuthorBase(BaseModel):
    Book_id: str
    Author_id: str

class BookAuthorCreate(BookAuthorBase):
    pass

class BookAuthor(BookAuthorBase):
    class Config:
        orm_mode = True