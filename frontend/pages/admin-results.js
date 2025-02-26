import { useState } from "react";
import axios from "axios";

export default function AdminResults() {
  const [studentId, setStudentId] = useState("");
  const [examId, setExamId] = useState("");

  const sendResult = async () => {
    try {
      await axios.post("http://localhost:8000/send-result-whatsapp", { student_id: studentId, exam_id: examId });
      alert("Result sent successfully!");
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  return (
    <div>
      <h2>Send Exam Result on WhatsApp</h2>
      <input type="text" placeholder="Student ID" onChange={(e) => setStudentId(e.target.value)} />
      <input type="text" placeholder="Exam ID" onChange={(e) => setExamId(e.target.value)} />
      <button onClick={sendResult}>Send Result</button>
    </div>
  );
}
