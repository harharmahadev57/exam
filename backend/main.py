from fastapi import FastAPI
from routes import students
from models import Base
from database import engine

# Database Tables Create करें
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Exam System API"}

# Routes Include करें
app.include_router(students.router, prefix="/students")




from fastapi import FastAPI
from routes import students, exams, omr
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Exam System API"}

app.include_router(students.router)
app.include_router(exams.router)
app.include_router(omr.router)
