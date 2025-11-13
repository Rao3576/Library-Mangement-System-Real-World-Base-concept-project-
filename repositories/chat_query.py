# repositories/chat_query.py
from sqlalchemy.orm import Session
from models.chat import ChatRoom, Message
from fastapi import HTTPException
import traceback

class ChatQuery:

    @staticmethod
    def create_room(db: Session, name: str, description: str = None):
        try:
            print(f"[ChatQuery] create_room called: name={name!r}, desc={description!r}")
            existing = db.query(ChatRoom).filter(ChatRoom.name == name).first()
            if existing:
                raise HTTPException(status_code=400, detail="Room already exists")
            room = ChatRoom(name=name, description=description)
            db.add(room)
            db.commit()
            db.refresh(room)
            print(f"[ChatQuery] room created id={room.id}")
            return {"id": room.id, "name": room.name, "description": room.description}
        except Exception as e:
            print("[ChatQuery] create_room ERROR:", e)
            traceback.print_exc()
            raise

    @staticmethod
    def get_rooms(db: Session):
        rooms = db.query(ChatRoom).all()
        print(f"[ChatQuery] get_rooms -> {len(rooms)} rooms")
        return [{"id": r.id, "name": r.name, "description": r.description} for r in rooms]

    @staticmethod
    def save_message(db: Session, sender: str, content: str, room_id: int):
        try:
            print(f"[ChatQuery] save_message: room_id={room_id}, sender={sender}, content={content}")
            message = Message(sender=sender, content=content, room_id=room_id)
            db.add(message)
            db.commit()
            db.refresh(message)
            print(f"[ChatQuery] saved message id={message.id}")
            return {"id": message.id, "sender": message.sender, "content": message.content, "timestamp": str(message.timestamp)}
        except Exception as e:
            print("[ChatQuery] save_message ERROR:", e)
            traceback.print_exc()
            raise

    @staticmethod
    def get_room_messages(db: Session, room_id: int):
        msgs = db.query(Message).filter(Message.room_id == room_id).order_by(Message.timestamp).all()
        print(f"[ChatQuery] get_room_messages: room_id={room_id} -> {len(msgs)} messages")
        return [{"sender": m.sender, "content": m.content, "timestamp": str(m.timestamp)} for m in msgs]

