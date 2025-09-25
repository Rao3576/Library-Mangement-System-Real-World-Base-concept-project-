from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Publisher(Base):
    __tablename__ = "Publisher"
    Publisher_id = Column(String(255), primary_key=True)
    Publisher_name = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Email = Column(String(255), nullable=False)
    Phone = Column(Integer, nullable=False)

    books = relationship("Book", back_populates="publisher")