@router.get("/student-exams/{student_id}")
def get_student_exams(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    class_id = student.class_id
    exams = db.query(Exam).filter(Exam.class_id == class_id).all()
    return exams
