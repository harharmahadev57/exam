import { useState } from "react";
import axios from "axios";

export default function AdminFaceCheck() {
  const [imageBase64, setImageBase64] = useState("");

  const checkFace = async () => {
    try {
      const response = await axios.post("http://localhost:8000/check-face", { image_base64: imageBase64 });
      alert(response.data.message);
    } catch (error) {
      console.error("Error checking face:", error);
    }
  };

  return (
    <div>
      <h2>Face Recognition System</h2>
      <input type="text" placeholder="Paste Base64 Image" onChange={(e) => setImageBase64(e.target.value)} />
      <button onClick={checkFace}>Check Face</button>
    </div>
  );
}
