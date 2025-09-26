from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional




# Employee
# ---------------------------
class EmployeeBase(BaseModel):
    Employee_name: str
    Email: EmailStr
    phone: int
    Position: str

class EmployeeCreate(EmployeeBase):
    Employee_id: str

class EmployeeUpdate(BaseModel):
    Employee_name: Optional[str] = None
    Email: Optional[EmailStr] = None
    phone: Optional[int] = None
    Position: Optional[str] = None

class Employee(EmployeeBase):
    Employee_id: str
    class Config:
        orm_mode = True