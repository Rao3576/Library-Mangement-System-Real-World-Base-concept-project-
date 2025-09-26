from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class Employee(Base):
    __tablename__ = "Employee"
    Employee_id = Column(String(255), primary_key=True)
    Employee_name = Column(String(255), nullable=False)
    Email = Column(String(255), nullable=False)
    phone = Column(Integer, nullable=False)
    Position = Column(String(255), nullable=False)

    borrowings = relationship("Borrowing", back_populates="employee")
    returns = relationship("BookReturn", back_populates="employee")
    reports = relationship("Report", back_populates="employee")