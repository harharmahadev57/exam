import { useState } from "react";
import axios from "axios";

export default function ResultPage() {
  const [studentId, setStudentId] = useState("");
  const [examId, setExamId] = useState("");
  const [correctAnswers, setCorrectAnswers] = useState("");
  const [totalQuestions, setTotalQuestions] = useState("");
  const [score, setScore] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:8000/submit-result", {
        student_id: studentId,
        exam_id: examId,
        correct_answers: parseInt(correctAnswers),
        total_questions: parseInt(totalQuestions),
      });
      setScore(response.data.score);
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  return (
    <div>
      <h2>Submit Exam Result</h2>
      <input type="text" placeholder="Student ID" onChange={(e) => setStudentId(e.target.value)} />
      <input type="text" placeholder="Exam ID" onChange={(e) => setExamId(e.target.value)} />
      <input type="number" placeholder="Correct Answers" onChange={(e) => setCorrectAnswers(e.target.value)} />
      <input type="number" placeholder="Total Questions" onChange={(e) => setTotalQuestions(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
      {score && <p>Score: {score}%</p>}
    </div>
  );
}



import { useEffect, useState } from "react";

export default function Results() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/results/1")
      .then((res) => res.json())
      .then((data) => setResults(data));
  }, []);

  return (
    <div>
      <h1>Your Exam Results</h1>
      <ul>
        {results.map((result) => (
          <li key={result.id}>
            Exam ID: {result.exam_id}, Answers: {JSON.stringify(result.answers)}
          </li>
        ))}
      </ul>
    </div>
  );
}
