from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
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



from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class OMRResponse(Base):
    __tablename__ = "omr_responses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    exam_id = Column(Integer, ForeignKey("exams.id"))
    answers = Column(String, nullable=False)  # JSON format (e.g. {"Q1": "A", "Q2": "B"})
    is_checked = Column(Boolean, default=False)

    student = relationship("Student")
    exam = relationship("Exam")
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# .env फाइल लोड करें
load_dotenv()

# डेटाबेस URL लोड करें
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy इंजन सेटअप करें
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base को सही से डिफाइन करें
Base = declarative_base()
