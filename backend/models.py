from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    __table_args__ = {"extend_existing": True}  # पहले से बनी टेबल अपडेट करने के लिए

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    class_name = Column(String, nullable=False)

    exams = relationship("Exam", back_populates="student")


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    pdf_link = Column(String, nullable=False)
    class_name = Column(String, nullable=False)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="exams")


class OMRResponse(Base):
    __tablename__ = "omr_responses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    exam_id = Column(Integer, ForeignKey("exams.id"))
    answers = Column(String, nullable=False)  # JSON format (e.g. {"Q1": "A", "Q2": "B"})
    is_checked = Column(Boolean, default=False)

    student = relationship("Student")
    exam = relationship("Exam")

# ✅ डेटाबेस से कनेक्ट करें
DATABASE_URL = "postgresql://your_username:your_password@your_db_host/your_db_name"
engine = create_engine(DATABASE_URL)

# ✅ नई टेबल बनाने से पहले टेबल्स को अपडेट करें
Base.metadata.create_all(bind=engine)  
