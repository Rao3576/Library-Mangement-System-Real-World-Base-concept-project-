from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Borrowing(Base):
    __tablename__ = "Borrowing"
    Borrowing_id = Column(String(255), primary_key=True)
    Student_id = Column(String(255), ForeignKey("Student.id"), nullable=False)
    Book_id = Column(String(255), ForeignKey("Book.Book_id"), nullable=False)
    Employee_id = Column(String(255), ForeignKey("Employee.Employee_id"), nullable=False)
    Borrow_date = Column(Date, nullable=False)
    Due_date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="borrowings")
    book = relationship("Book", back_populates="borrowings")
    employee = relationship("Employee", back_populates="borrowings")
    return_record = relationship("BookReturn", back_populates="borrowing", uselist=False)