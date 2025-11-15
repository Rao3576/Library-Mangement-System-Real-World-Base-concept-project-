from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Transaction(Base):
    __tablename__ = "Transaction"
    Transaction_id = Column(String(255), primary_key=True)
    Student_id = Column(String(255), ForeignKey("Student.id"), nullable=False)
    Transaction_Type = Column(String(255), nullable=False)
    Account = Column(DECIMAL(8, 2), nullable=False)
    Transaction_date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="transactions")
