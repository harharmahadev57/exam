import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# .env फाइल लोड करें
load_dotenv(dotenv_path=".env")  # <- .env का पथ सही करें

# वेरीएबल एक्सेस करें
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

# डेटाबेस कनेक्शन सेटअप
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# डेटाबेस सेशन बनाने का फंक्शन
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# चेक करें कि वैल्यू आ रही है या नहीं
print("Cloudinary URL:", CLOUDINARY_URL)
print("Database URL:", DATABASE_URL)
