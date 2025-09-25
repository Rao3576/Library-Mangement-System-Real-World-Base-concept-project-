from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional


# Publisher
# ---------------------------
class PublisherBase(BaseModel):
    Publisher_name: str
    Address: str
    Email: EmailStr
    Phone: int

class PublisherCreate(PublisherBase):
    Publisher_id: str

class PublisherUpdate(BaseModel):
    Publisher_name: Optional[str] = None
    Address: Optional[str] = None
    Email: Optional[EmailStr] = None
    Phone: Optional[int] = None

class Publisher(PublisherBase):
    Publisher_id: str
    class Config:
        orm_mode = True

