import { useEffect, useState } from "react";
import axios from "axios";

export default function StudentDashboard() {
  const [exams, setExams] = useState([]);
  const studentId = 1; // **🔹 मान लीजिए Student ID = 1 है**

  useEffect(() => {
    const fetchExams = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/student-exams/${studentId}`);
        setExams(response.data);
      } catch (error) {
        console.error("Error fetching exams:", error);
      }
    };
    fetchExams();
  }, []);

  return (
    <div>
      <h2>My Exams</h2>
      <ul>
        {exams.map((exam) => (
          <li key={exam.id}>{exam.name}</li>
        ))}
      </ul>
    </div>
  );
}
