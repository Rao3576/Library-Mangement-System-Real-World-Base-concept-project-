from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class Report(Base):
    __tablename__ = "Report"
    Report_id = Column(String(255), primary_key=True)
    Report_Type = Column(String(255), nullable=False)
    Generated_date = Column(Date, nullable=False)
    Employee_id = Column(String(255), ForeignKey("Employee.Employee_id"), nullable=False)
    Report_content = Column(Text, nullable=False)

    employee = relationship("Employee", back_populates="reports")