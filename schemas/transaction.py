from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional




# Transaction
# ---------------------------
class TransactionBase(BaseModel):
    Transaction_Type: str
    Account: float
    Transaction_date: date

class TransactionCreate(TransactionBase):
    Transaction_id: str
    Student_id: str

class TransactionUpdate(BaseModel):
    Transaction_Type: Optional[str] = None
    Account: Optional[float] = None
    Transaction_date: Optional[date] = None

class Transaction(TransactionBase):
    Transaction_id: str
    Student_id: str
    class Config:
        orm_mode = True

