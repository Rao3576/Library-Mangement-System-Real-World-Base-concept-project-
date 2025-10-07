from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class BookAuthor(Base):
    __tablename__ = "Book_Author"
    Book_id = Column(String(255), ForeignKey("Book.Book_id"), primary_key=True)
    Author_id = Column(String(255), ForeignKey("Author.Author_id"), primary_key=True)

    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")