import os
from dotenv import load_dotenv

# .env फाइल लोड करें
load_dotenv()

# वैरिएबल एक्सेस करें
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

print("Cloudinary URL:", CLOUDINARY_URL)
print("Database URL:", DATABASE_URL)
