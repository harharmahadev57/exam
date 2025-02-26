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
