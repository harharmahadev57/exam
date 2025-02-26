from fastapi import APIRouter, UploadFile, File
from cloudinary_config import upload_file

router = APIRouter()

@router.post("/upload-exam/")
async def upload_exam(file: UploadFile = File(...)):
    file_url = upload_file(file.file)
    return {"message": "File uploaded successfully", "file_url": file_url}

@router.post("/create-exam")
def create_exam(title: str, class_id: int, db: Session = Depends(get_db)):
    exam = Exam(title=title, class_id=class_id)
    db.add(exam)
    db.commit()
    return {"message": "Exam created successfully"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exam, Student
from pydantic import BaseModel

router = APIRouter()

class ExamCreate(BaseModel):
    title: str
    pdf_link: str
    class_name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/exams")
def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    db_exam = Exam(title=exam.title, pdf_link=exam.pdf_link, class_name=exam.class_name)
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

@router.get("/exams/{class_name}")
def get_exams(class_name: str, db: Session = Depends(get_db)):
    return db.query(Exam).filter(Exam.class_name == class_name).all()



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exam, Student
from pydantic import BaseModel

router = APIRouter()

class ExamCreate(BaseModel):
    title: str
    pdf_link: str
    class_name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/exams")
def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    db_exam = Exam(title=exam.title, pdf_link=exam.pdf_link, class_name=exam.class_name)
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

@router.get("/exams/{class_name}")
def get_exams(class_name: str, db: Session = Depends(get_db)):
    return db.query(Exam).filter(Exam.class_name == class_name).all()
