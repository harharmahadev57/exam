from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import OMRResponse, Exam, Student
from pydantic import BaseModel
import json

router = APIRouter()

class OMRSubmit(BaseModel):
    student_id: int
    exam_id: int
    answers: dict  # e.g. {"Q1": "A", "Q2": "B"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit-omr")
def submit_omr(omr_data: OMRSubmit, db: Session = Depends(get_db)):
    db_omr = OMRResponse(
        student_id=omr_data.student_id,
        exam_id=omr_data.exam_id,
        answers=json.dumps(omr_data.answers),
        is_checked=False
    )
    db.add(db_omr)
    db.commit()
    return {"message": "OMR Submitted Successfully"}

@router.get("/results/{student_id}")
def get_results(student_id: int, db: Session = Depends(get_db)):
    results = db.query(OMRResponse).filter(OMRResponse.student_id == student_id).all()
    return results
