from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from twilio.rest import Client
from database import SessionLocal
from models import Student, ExamResult
import os

router = APIRouter()

# Twilio API Credentials
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio का नंबर

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# **📌 1️⃣ Student को WhatsApp पर Result भेजना**
@router.post("/send-result-whatsapp")
def send_result(student_id: int, exam_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    exam_result = db.query(ExamResult).filter(ExamResult.student_id == student_id, ExamResult.exam_id == exam_id).first()

    if not student or not exam_result:
        return {"message": "Student or Exam Result not found"}

    message = f"Dear {student.name},\nYour result for {exam_result.exam_name} is:\nMarks: {exam_result.marks}/100\nThank you!"
    
    # **📌 Twilio API Call**
    client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=f"whatsapp:+91{student.phone}"
    )

    return {"message": "Result sent on WhatsApp!"}




from fastapi import APIRouter, HTTPException
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# **📌 Twilio API Configurations**
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# **📌 1️⃣ API – Exam Reminder WhatsApp पर भेजें**
@router.post("/send-exam-reminder/")
async def send_exam_reminder(student_number: str, exam_date: str):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            body=f"📢 Reminder: आपका एग्जाम {exam_date} को है। समय पर तैयार रहें! ✅",
            to=f"whatsapp:{student_number}"
        )
        return {"message": "Exam Reminder Sent Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# **📌 2️⃣ API – Exam Result WhatsApp पर भेजें**
@router.post("/send-exam-result/")
async def send_exam_result(student_number: str, student_name: str, marks: int, total_marks: int):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            body=f"📢 Hello {student_name}, आपका एग्जाम रिजल्ट आ गया है!\n🎯 Marks: {marks}/{total_marks}\n✅ All the Best! 🎉",
            to=f"whatsapp:{student_number}"
        )
        return {"message": "Exam Result Sent Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
