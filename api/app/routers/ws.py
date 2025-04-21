import json
from fastapi import Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from fastapi import APIRouter
from app.database import get_db

ws_router = APIRouter(tags=["ws"])


@ws_router.websocket("/ws/app")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    try:
        while True:
            raw_data = await websocket.receive_text()
            data = json.loads(raw_data)

            message = data.get("message")
            
            websocket.send_json(
                {
                    "response": message,
                }
            )

    except WebSocketDisconnect:
        print("Client disconnected")
