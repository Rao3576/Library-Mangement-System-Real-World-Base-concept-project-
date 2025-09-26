from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional





# Report
# ---------------------------
class ReportBase(BaseModel):
    Report_Type: str
    Generated_date: date
    Report_content: str

class ReportCreate(ReportBase):
    Report_id: str
    Employee_id: str

class ReportUpdate(BaseModel):
    Report_Type: Optional[str] = None
    Generated_date: Optional[date] = None
    Report_content: Optional[str] = None
    Employee_id: Optional[str] = None

class Report(ReportBase):
    Report_id: str
    Employee_id: str
    class Config:
        orm_mode = True