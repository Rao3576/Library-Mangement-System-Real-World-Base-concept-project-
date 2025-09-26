from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class BookReturn(Base):
    __tablename__ = "Book-Return_record"
    Return_id = Column(String(255), primary_key=True)
    Borrow_id = Column(String(255), ForeignKey("Borrowing.Borrowing_id"), nullable=False)
    Return_date = Column(Date, nullable=False)
    Condition = Column(String(255), nullable=False)
    Employee_id = Column(String(255), ForeignKey("Employee.Employee_id"), nullable=False)

    borrowing = relationship("Borrowing", back_populates="return_record")
    employee = relationship("Employee", back_populates="returns")