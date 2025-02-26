from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("postgresql://exam_db_848p_user:4KtEKvxuF6R4LkQZAiUimku8EkgBLqZs@dpg-cutfgqbtq21c73bemns0-a.oregon-postgres.render.com/exam_db_848p")

engine = create_engine(CLOUDINARY_URL=cloudinary://684851764112618:BAYsU8wkFPUKEOB1-6xNKZdo2N8@dsuolsjlo)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
