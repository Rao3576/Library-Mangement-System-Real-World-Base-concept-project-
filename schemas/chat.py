from pydantic import BaseModel
from datetime import datetime

class ChatRoomCreate(BaseModel):
    name: str
    description: str | None = None

class ChatRoomOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    class Config:
        from_attributes = True

class MessageCreate(BaseModel):
    sender: str
    content: str
    room_id: int

class MessageOut(BaseModel):
    sender: str
    content: str
    timestamp: datetime
    class Config:
        from_attributes = True
