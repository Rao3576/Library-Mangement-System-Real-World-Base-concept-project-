from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "Student"

    id = Column(String(255), primary_key=True)
    student_name = Column(String(255), nullable=False)
    Email = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Status = Column(Boolean, nullable=False)

    transactions = relationship("Transaction", back_populates="student")
    borrowings = relationship("Borrowing", back_populates="student")

