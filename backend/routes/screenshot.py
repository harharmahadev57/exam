import time
import base64
import cloudinary
import cloudinary.uploader
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import StudentScreenshot

router = APIRouter()

# **📌 Cloudinary Configuration**
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# **📌 1️⃣ Screenshot Upload करने का API**
@router.post("/upload-screenshot")
def upload_screenshot(student_id: int, screenshot_base64: str, db: Session = Depends(get_db)):
    # **📌 Base64 से Image Decode करें**
    image_data = base64.b64decode(screenshot_base64)

    # **📌 Cloudinary पर Upload करें**
    result = cloudinary.uploader.upload(image_data, folder="screenshots")

    # **📌 Database में Save करें**
    new_screenshot = StudentScreenshot(student_id=student_id, image_url=result["secure_url"])
    db.add(new_screenshot)
    db.commit()

    return {"message": "Screenshot uploaded!", "url": result["secure_url"]}

# **📌 2️⃣ Admin - सभी Screenshots देखें**
@router.get("/get-screenshots/{student_id}")
def get_screenshots(student_id: int, db: Session = Depends(get_db)):
    screenshots = db.query(StudentScreenshot).filter(StudentScreenshot.student_id == student_id).all()
    return [{"id": s.id, "url": s.image_url} for s in screenshots]
