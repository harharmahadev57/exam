from sqlalchemy import create_engine
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

# ✅ get_db फंक्शन को सही से डिफाइन करें
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
