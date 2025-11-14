# routes/chat.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from repositories.chat_query import ChatQuery

router = APIRouter(prefix="/chat", tags=["Chat System"])

@router.post("/create")
def create_room(name: str, description: str = None, db: Session = Depends(get_db)):
    return ChatQuery.create_room(db, name, description)

@router.get("/rooms")
def get_rooms(db: Session = Depends(get_db)):
    return {"rooms": ChatQuery.get_rooms(db)}

@router.get("/messages/{room_id}")
def get_room_messages(room_id: int, db: Session = Depends(get_db)):
    return ChatQuery.get_room_messages(db, room_id)


