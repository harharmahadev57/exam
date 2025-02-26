from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Class, Exam, Student

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# **📌 1️⃣ Admin - Class Create करे**
@router.post("/create-class")
def create_class(name: str, db: Session = Depends(get_db)):
    new_class = Class(name=name)
    db.add(new_class)
    db.commit()
    return {"message": "Class created successfully!", "class_id": new_class.id}

# **📌 2️⃣ Admin - Exam को Class से जोड़ें**
@router.post("/assign-exam-to-class")
def assign_exam_to_class(class_id: int, exam_id: int, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    exam_obj = db.query(Exam).filter(Exam.id == exam_id).first()

    if not class_obj or not exam_obj:
        raise HTTPException(status_code=404, detail="Class or Exam not found")

    class_obj.exams.append(exam_obj)
    db.commit()
    return {"message": "Exam assigned to class successfully!"}
