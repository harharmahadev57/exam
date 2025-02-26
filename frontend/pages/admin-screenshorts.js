import { useState, useEffect } from "react";
import axios from "axios";

export default function AdminScreenshots() {
  const [screenshots, setScreenshots] = useState([]);
  const [studentId, setStudentId] = useState("");

  const fetchScreenshots = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/get-screenshots/${studentId}`);
      setScreenshots(response.data);
    } catch (error) {
      console.error("Error fetching screenshots:", error);
    }
  };

  return (
    <div>
      <h2>Student Screenshots</h2>
      <input type="text" placeholder="Enter Student ID" onChange={(e) => setStudentId(e.target.value)} />
      <button onClick={fetchScreenshots}>Get Screenshots</button>

      <div>
        {screenshots.map((screenshot) => (
          <img key={screenshot.id} src={screenshot.url} alt="Screenshot" width="300px" />
        ))}
      </div>
    </div>
  );
}
