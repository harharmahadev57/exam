import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "dsuolsjlo",  
  api_key = "684851764112618",  
  api_secret = "BAYsU8wkFPUKEOB1-6xNKZdo2N8"  
)

def upload_file(file):
    result = cloudinary.uploader.upload(file)
    return result["secure_url"]
