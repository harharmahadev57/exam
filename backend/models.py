 File "/opt/render/project/src/backend/venv/lib/python3.11/site-packages/sqlalchemy/sql/schema.py", line 462, in _new
    raise exc.InvalidRequestError(
sqlalchemy.exc.InvalidRequestError: Table 'students' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object. File "/opt/render/project/src/backend/venv/lib/python3.11/site-packages/sqlalchemy/sql/schema.py", line 462, in _new
    raise exc.InvalidRequestError(
sqlalchemy.exc.InvalidRequestError: Table 'students' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.from sqlalchemy import Column, Integer, String
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



from database import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    __table_args__ = {"extend_existing": True}  # ✅ सही तरीका

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# ✅ मैन्युअली टेबल अपडेट करें
DATABASE_URL = "postgresql://your_username:your_password@your_db_host/your_db_name"
engine = create_engine(DATABASE_URL)
Base.metadata.drop_all(bind=engine)  # 🔥 टेबल को ड्रॉप करके रीक्रिएट करेगा
Base.metadata.create_all(bind=engine)  # ✅ नई टेबल बनाएगा File "/opt/render/project/src/backend/venv/lib/python3.11/site-packages/sqlalchemy/sql/schema.py", line 462, in _new
    raise exc.InvalidRequestError(
sqlalchemy.exc.InvalidRequestError: Table 'students' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.





from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    __table_args__ = {"extend_existing": True}  # ✅ सही स्पेसिंग

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
