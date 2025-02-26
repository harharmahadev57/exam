import { useState } from "react";

export default function SendWhatsApp() {
  const [studentNumber, setStudentNumber] = useState("");
  const [examDate, setExamDate] = useState("");

  const sendReminder = async () => {
    const response = await fetch("http://localhost:8000/send-exam-reminder/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ student_number: studentNumber, exam_date: examDate }),
    });
    const result = await response.json();
    alert(result.message);
  };

  return (
    <div>
      <h3>Send WhatsApp Exam Reminder</h3>
      <input type="text" placeholder="Student Number" onChange={(e) => setStudentNumber(e.target.value)} />
      <input type="text" placeholder="Exam Date" onChange={(e) => setExamDate(e.target.value)} />
      <button onClick={sendReminder}>Send Reminder</button>
    </div>
  );
}
