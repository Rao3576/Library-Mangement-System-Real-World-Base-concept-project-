# routes/web_soucket_auth.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories.chat_query import ChatQuery
import traceback

router = APIRouter(tags=["Chat WebSocket"])

# room_id -> list[WebSocket]
active_connections: dict[int, list[WebSocket]] = {}

@router.websocket("/ws/{room_id}/{username}")
async def websocket_chat(websocket: WebSocket, room_id: int, username: str, db: Session = Depends(get_db)):
    print(f"[WS] connection request: room_id={room_id}, username={username}")
    await websocket.accept()
    if room_id not in active_connections:
        active_connections[room_id] = []
    active_connections[room_id].append(websocket)
    print(f"[WS] client added. total in room {room_id} = {len(active_connections[room_id])}")

    # inform others
    for ws in list(active_connections[room_id]):
        try:
            if ws != websocket:
                await ws.send_text(f"👋 {username} joined the room")
        except Exception:
            print("[WS] notify join failed for one connection")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"[WS] received from {username} in room {room_id}: {data!r}")
            try:
                saved = ChatQuery.save_message(db, sender=username, content=data, room_id=room_id)
                print("[WS] message saved:", saved)
            except Exception as e:
                print("[WS] DB save error:", e)
            # broadcast to all clients in this room
            for ws in list(active_connections[room_id]):
                try:
                    await ws.send_text(f"{username}: {data}")
                except Exception as e:
                    print("[WS] send_text error, removing ws:", e)
                    try:
                        active_connections[room_id].remove(ws)
                    except:
                        pass
    except WebSocketDisconnect:
        print(f"[WS] disconnect: {username} from room {room_id}")
        try:
            active_connections[room_id].remove(websocket)
        except:
            pass
        for ws in active_connections.get(room_id, []):
            try:
                await ws.send_text(f"🚪 {username} left the room")
            except:
                pass
    except Exception as e:
        print("[WS] unknown error:", e)
        traceback.print_exc()


