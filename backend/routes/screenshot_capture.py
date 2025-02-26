from fastapi import APIRouter, UploadFile, File
import cloudinary
import cloudinary.uploader
import datetime

router = APIRouter()

# **📌 Cloudinary Config**
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# **📌 1️⃣ API – Screenshot Upload करें और Save करें**
@router.post("/upload-screenshot/")
async def upload_screenshot(student_id: str, file: UploadFile = File(...)):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{student_id}_{timestamp}.png"

    # **📌 Cloudinary पर Upload करें**
    result = cloudinary.uploader.upload(file.file, public_id=f"screenshots/{file_name}")

    return {"message": "Screenshot uploaded successfully!", "url": result["secure_url"]}

