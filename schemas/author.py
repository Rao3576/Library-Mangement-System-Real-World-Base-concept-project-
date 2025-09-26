from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional




# Author
# ---------------------------
class AuthorBase(BaseModel):
    Author_name: str
    Bio: str
    Nationality: str

class AuthorCreate(AuthorBase):
    Author_id: str

class AuthorUpdate(BaseModel):
    Author_name: Optional[str] = None
    Bio: Optional[str] = None
    Nationality: Optional[str] = None

class Author(AuthorBase):
    Author_id: str
    class Config:
        orm_mode = True
