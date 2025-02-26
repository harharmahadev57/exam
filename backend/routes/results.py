from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ExamResult, Student

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit-result")
def submit_result(student_id: int, exam_id: int, correct_answers: int, total_questions: int, db: Session = Depends(get_db)):
    score = (correct_answers / total_questions) * 100
    result = ExamResult(student_id=student_id, exam_id=exam_id, score=score)
    db.add(result)
    db.commit()
    return {"message": "Result saved!", "score": score}


from fastapi import APIRouter, HTTPException
from fpdf import FPDF
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# **📌 Cloudinary Config**
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# **📌 Exam Result PDF Generate और Upload API**
@router.post("/generate-result-pdf/")
async def generate_result_pdf(student_name: str, student_number: str, marks: int, total_marks: int):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="Exam Result", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Name: {student_name}", ln=True)
        pdf.cell(200, 10, txt=f"Phone Number: {student_number}", ln=True)
        pdf.cell(200, 10, txt=f"Marks: {marks}/{total_marks}", ln=True)

        pdf_path = f"{student_name}_Result.pdf"
        pdf.output(pdf_path)

        # **📌 PDF को Cloudinary में अपलोड करें**
        upload_response = cloudinary.uploader.upload(pdf_path, resource_type="raw")
        pdf_url = upload_response.get("url")

        return {"message": "Result PDF Generated!", "pdf_url": pdf_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
