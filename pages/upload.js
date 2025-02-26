import { useState } from "react";
import axios from "axios";

export default function UploadExam() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:8000/upload-exam/", formData);
      setMessage("File uploaded: " + response.data.file_url);
    } catch (error) {
      setMessage("Upload failed: " + error.message);
    }
  };

  return (
    <div>
      <h2>Upload Exam</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
}
