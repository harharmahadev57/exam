from fastapi import APIRouter, HTTPException
import cloudinary
import cloudinary.uploader

router = APIRouter()

@router.post("/upload-screenshot")
def upload_screenshot(image: str):
    upload_result = cloudinary.uploader.upload(image, folder="exam_screenshots")
    return {"message": "Screenshot saved!", "url": upload_result["secure_url"]}
