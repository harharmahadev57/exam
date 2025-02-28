import os
from dotenv import load_dotenv

# .env फाइल लोड करें
load_dotenv(dotenv_path=".env")  # <- यहाँ .env का पथ दें

# वैरिएबल एक्सेस करें
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

# चेक करें कि वैल्यू आ रही है या नहीं
print("Cloudinary URL:", CLOUDINARY_URL)
print("Database URL:", DATABASE_URL)
