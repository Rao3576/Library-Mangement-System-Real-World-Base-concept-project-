from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models import *

class Book(Base):
    __tablename__ = "Book"
    Book_id = Column(String(255), primary_key=True)
    Title = Column(String(255), nullable=False)
    Publication_Year = Column(Integer, nullable=False)
    Edition = Column(String(255), nullable=False)
    Publisher_id = Column(String(255), ForeignKey("Publisher.Publisher_id"), nullable=False)

    publisher = relationship("Publisher", back_populates="books")
    authors = relationship("BookAuthor", back_populates="book")
    statuses = relationship("BookStatus", back_populates="book")
    borrowings = relationship("Borrowing", back_populates="book")