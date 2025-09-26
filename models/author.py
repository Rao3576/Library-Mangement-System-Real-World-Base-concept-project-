from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Author(Base):
    __tablename__ = "Author"
    Author_id = Column(String(255), primary_key=True)
    Author_name = Column(String(255), nullable=False)
    Bio = Column(Text, nullable=False)
    Nationality = Column(String(255), nullable=False)

    books = relationship("BookAuthor", back_populates="author")