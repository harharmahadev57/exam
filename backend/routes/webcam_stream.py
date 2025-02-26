from fastapi import APIRouter, WebSocket
from datetime import datetime

router = APIRouter()

# **📌 Student Video Streaming Data Store करने के लिए**
student_streams = {}

# **📌 1️⃣ WebSocket API – Live Video Data Receive करें**
@router.websocket("/ws/video-stream/{student_id}")
async def websocket_endpoint(websocket: WebSocket, student_id: str):
    await websocket.accept()
    student_streams[student_id] = websocket

    try:
        while True:
            data = await websocket.receive_bytes()
            for admin_ws in student_streams.values():
                if admin_ws != websocket:
                    await admin_ws.send_bytes(data)
    except:
        del student_streams[student_id]
