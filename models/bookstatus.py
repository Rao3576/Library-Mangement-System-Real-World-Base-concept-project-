from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class BookStatus(Base):
    __tablename__ = "Book_status"
    Status_id = Column(String(255), primary_key=True)
    Book_id = Column(String(255), ForeignKey("Book.Book_id"), nullable=False)
    Status = Column(String(255), nullable=False)
    Last_update = Column(DateTime, nullable=False)

    book = relationship("Book", back_populates="statuses")