import cv2
import numpy as np
from deepface import DeepFace
from fastapi import APIRouter, HTTPException
import base64

router = APIRouter()

# **📌 1️⃣ Face Detection Function**
def detect_faces(image_base64):
    # **📌 Base64 को Image में Convert करें**
    image_data = base64.b64decode(image_base64)
    np_arr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # **📌 OpenCV से Face Detect करें**
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    return len(faces)  # **📌 कितने चेहरे हैं?**

# **📌 2️⃣ API – Face Check करें**
@router.post("/check-face")
def check_face(image_base64: str):
    face_count = detect_faces(image_base64)

    if face_count == 1:
        return {"message": "Only one person detected ✅"}
    elif face_count > 1:
        return {"message": "Multiple faces detected! ❌ Cheating Alert!"}
    else:
        return {"message": "No face detected! ❌"}


import cv2
import numpy as np
import face_recognition
from fastapi import APIRouter, UploadFile, File
import cloudinary
import cloudinary.uploader

router = APIRouter()

# **📌 Cloudinary Config**
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# **📌 1️⃣ API – Face Recognition के लिए**
@router.post("/face-recognition/")
async def recognize_faces(student_id: str, file: UploadFile = File(...)):
    img_bytes = np.frombuffer(await file.read(), np.uint8)
    frame = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)

    faces = face_recognition.face_locations(frame)
    if len(faces) > 1:
        return {"alert": "Multiple faces detected! Possible cheating!"}

    return {"message": "Face verified successfully."}
