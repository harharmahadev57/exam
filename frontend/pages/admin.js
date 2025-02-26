import { useState } from "react";
import axios from "axios";

export default function AdminPanel() {
  const [title, setTitle] = useState("");
  const [classId, setClassId] = useState("");

  const handleCreateExam = async () => {
    try {
      await axios.post("http://localhost:8000/create-exam", { title, class_id: classId });
      alert("Exam Created!");
    } catch (error) {
      alert("Failed: " + error.message);
    }
  };

  return (
    <div>
      <h2>Create Exam</h2>
      <input type="text" placeholder="Exam Title" onChange={(e) => setTitle(e.target.value)} />
      <input type="number" placeholder="Class ID" onChange={(e) => setClassId(e.target.value)} />
      <button onClick={handleCreateExam}>Create</button>
    </div>
  );
}


import { useState } from "react";
import axios from "axios";

export default function AdminPanel() {
  const [className, setClassName] = useState("");
  const [classId, setClassId] = useState("");
  const [examId, setExamId] = useState("");

  // **📌 1️⃣ Class Create करने का Function**
  const createClass = async () => {
    try {
      const response = await axios.post("http://localhost:8000/create-class", { name: className });
      alert("Class Created! ID: " + response.data.class_id);
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  // **📌 2️⃣ Exam को Class से Assign करने का Function**
  const assignExam = async () => {
    try {
      await axios.post("http://localhost:8000/assign-exam-to-class", { class_id: classId, exam_id: examId });
      alert("Exam Assigned to Class!");
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  return (
    <div>
      <h2>Admin Panel</h2>
      
      <h3>Create New Class</h3>
      <input type="text" placeholder="Class Name" onChange={(e) => setClassName(e.target.value)} />
      <button onClick={createClass}>Create Class</button>

      <h3>Assign Exam to Class</h3>
      <input type="text" placeholder="Class ID" onChange={(e) => setClassId(e.target.value)} />
      <input type="text" placeholder="Exam ID" onChange={(e) => setExamId(e.target.value)} />
      <button onClick={assignExam}>Assign Exam</button>
    </div>
  );
}


import SendWhatsApp from "../components/SendWhatsApp";

export default function AdminDashboard() {
  return (
    <div>
      <h2>Admin Panel</h2>
      <SendWhatsApp />
    </div>
  );
}



import { useState } from "react";

export default function GenerateResult() {
  const [studentName, setStudentName] = useState("");
  const [studentNumber, setStudentNumber] = useState("");
  const [marks, setMarks] = useState("");
  const [totalMarks, setTotalMarks] = useState("");
  const [pdfUrl, setPdfUrl] = useState("");

  const generatePDF = async () => {
    const response = await fetch("http://localhost:8000/generate-result-pdf/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        student_name: studentName,
        student_number: studentNumber,
        marks: parseInt(marks),
        total_marks: parseInt(totalMarks),
      }),
    });

    const result = await response.json();
    if (result.pdf_url) {
      setPdfUrl(result.pdf_url);
    }
  };

  return (
    <div>
      <h3>Generate Exam Result PDF</h3>
      <input type="text" placeholder="Student Name" onChange={(e) => setStudentName(e.target.value)} />
      <input type="text" placeholder="Student Number" onChange={(e) => setStudentNumber(e.target.value)} />
      <input type="text" placeholder="Marks" onChange={(e) => setMarks(e.target.value)} />
      <input type="text" placeholder="Total Marks" onChange={(e) => setTotalMarks(e.target.value)} />
      <button onClick={generatePDF}>Generate PDF</button>
      {pdfUrl && <p><a href={pdfUrl} target="_blank">Download Result PDF</a></p>}
    </div>
  );
}


import { useState } from "react";

export default function Admin() {
  const [title, setTitle] = useState("");
  const [pdf_link, setPdfLink] = useState("");
  const [class_name, setClassName] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch("http://localhost:8000/exams", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, pdf_link, class_name }),
    });
    alert("Exam Created Successfully");
  };

  return (
    <div>
      <h1>Admin Panel - Create Exam</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Exam Title" value={title} onChange={(e) => setTitle(e.target.value)} />
        <input type="text" placeholder="PDF Link" value={pdf_link} onChange={(e) => setPdfLink(e.target.value)} />
        <input type="text" placeholder="Class Name" value={class_name} onChange={(e) => setClassName(e.target.value)} />
        <button type="submit">Create Exam</button>
      </form>
    </div>
  );
}
