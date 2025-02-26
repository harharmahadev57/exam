import { useEffect, useState } from "react";
import axios from "axios";

export default function ExamPage() {
  const [alertMessage, setAlertMessage] = useState("");

  // **📌 1️⃣ Tab Switching Detection**
  useEffect(() => {
    const handleVisibilityChange = () => {
      if (document.hidden) {
        setAlertMessage("⚠️ Tab Switching Detected!");
      }
    };
    document.addEventListener("visibilitychange", handleVisibilityChange);
    return () => document.removeEventListener("visibilitychange", handleVisibilityChange);
  }, []);

  // **📌 2️⃣ Automatic Screenshot Capture (हर 30 सेकंड में)**
  useEffect(() => {
    const captureScreenshot = async () => {
      try {
        const canvas = document.createElement("canvas");
        const video = document.createElement("video");
        video.srcObject = await navigator.mediaDevices.getDisplayMedia({ video: true });
        video.play();
        setTimeout(() => {
          canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
          const imageUrl = canvas.toDataURL("image/png");
          axios.post("http://localhost:8000/upload-screenshot", { image: imageUrl });
        }, 3000);
      } catch (error) {
        console.error("Screenshot Error:", error);
      }
    };

    const interval = setInterval(captureScreenshot, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Exam Interface</h2>
      {alertMessage && <p style={{ color: "red" }}>{alertMessage}</p>}
    </div>
  );
}


import { useState } from "react";
import TabSwitchDetection from "../components/TabSwitchDetection";

export default function ExamPage() {
  const [submitted, setSubmitted] = useState(false);

  const handleAutoSubmit = () => {
    setSubmitted(true);
  };

  return (
    <div>
      <h2>Online Exam</h2>
      {!submitted ? (
        <>
          <TabSwitchDetection studentId="student123" onAutoSubmit={handleAutoSubmit} />
          <p>📖 Exam is running... Don't switch tabs!</p>
          <button onClick={() => setSubmitted(true)}>Submit Exam</button>
        </>
      ) : (
        <h3>✅ Exam Submitted Successfully!</h3>
      )}
    </div>
  );
}


import ScreenshotCapture from "../components/ScreenshotCapture";

export default function ExamPage() {
  return (
    <div>
      <h2>Online Exam</h2>
      <ScreenshotCapture studentId="student123" />
      <p>📖 Exam is running... Stay focused!</p>
    </div>
  );
}



import { useEffect } from "react";

export default function FaceDetection({ studentId }) {
  useEffect(() => {
    const captureFace = async () => {
      const video = document.createElement("video");

      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        await video.play();

        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        stream.getTracks().forEach(track => track.stop());

        canvas.toBlob(async (blob) => {
          const formData = new FormData();
          formData.append("file", blob);
          formData.append("student_id", studentId);

          const response = await fetch("http://localhost:8000/face-recognition/", {
            method: "POST",
            body: formData,
          });

          const result = await response.json();
          if (result.alert) {
            alert(result.alert);
          }
        }, "image/png");
      } catch (err) {
        console.error("Face capture failed:", err);
      }
    };

    const interval = setInterval(captureFace, 60000); // **📌 हर 1 मिनट में Face चेक होगा**
    return () => clearInterval(interval);
  }, [studentId]);

  return null;
}


import { useState, useEffect } from "react";

export default function Exams() {
  const [exams, setExams] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/exams/class10")
      .then((res) => res.json())
      .then((data) => setExams(data));
  }, []);

  return (
    <div>
      <h1>Available Exams</h1>
      <ul>
        {exams.map((exam) => (
          <li key={exam.id}>
            {exam.title} - <a href={exam.pdf_link}>Download PDF</a>
          </li>
        ))}
      </ul>
    </div>
  );
}



import { useState } from "react";

export default function ExamPage() {
  const [answers, setAnswers] = useState({});

  const handleOptionChange = (question, option) => {
    setAnswers((prev) => ({ ...prev, [question]: option }));
  };

  const handleSubmit = async () => {
    await fetch("http://localhost:8000/submit-omr", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        student_id: 1,
        exam_id: 101,
        answers: answers,
      }),
    });
    alert("OMR Submitted Successfully");
  };

  return (
    <div>
      <h1>Exam OMR Sheet</h1>
      <div>
        <p>Q1: What is 2+2?</p>
        <button onClick={() => handleOptionChange("Q1", "A")}>A) 3</button>
        <button onClick={() => handleOptionChange("Q1", "B")}>B) 4</button>
      </div>
      <div>
        <p>Q2: What is 5+3?</p>
        <button onClick={() => handleOptionChange("Q2", "A")}>A) 7</button>
        <button onClick={() => handleOptionChange("Q2", "B")}>B) 8</button>
      </div>
      <button onClick={handleSubmit}>Submit OMR</button>
    </div>
  );
}
