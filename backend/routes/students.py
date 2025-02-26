from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Student

router = APIRouter()

@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.post("/")
def create_student(name: str, email: str, phone: str, password: str, db: Session = Depends(get_db)):
    new_student = Student(name=name, email=email, phone=phone, password=password)
    db.add(new_student)
    db.commit()
    return {"message": "Student created successfully"}
