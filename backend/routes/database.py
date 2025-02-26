from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://exam_db_848p_user:4KtEKvxuF6R4LkQZAiUimku8EkgBLqZs@dpg-cutfgqbtq21c73bemns0-a.oregon-postgres.render.com/exam_db_848p"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
