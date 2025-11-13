from pydantic import BaseModel

class StudentBase(BaseModel):
    id: str
    student_name: str
    Email: str
    Address: str
    Status: bool

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    student_name: str | None = None
    Email: str | None = None
    Address: str | None = None
    Status: bool | None = None

class Student(StudentBase):
    class Config:
        orm_mode = True
