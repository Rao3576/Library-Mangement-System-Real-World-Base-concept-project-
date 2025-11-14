from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


# ✅ Chat Room Table
class ChatRoom(Base):
    __tablename__ = "chat_rooms"
    id = Column(String(255), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255))
    messages = relationship("Message", back_populates="room")


class Message(Base):
    __tablename__ = "messages"
    id = Column(String(255), primary_key=True)
    sender = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    room_id = Column(String(255), ForeignKey("chat_rooms.id"), nullable=False)
    room = relationship("ChatRoom", back_populates="messages")
