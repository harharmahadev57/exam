import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/students")
      .then((res) => setStudents(res.data))
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      <h2>Student Dashboard</h2>
      <ul>
        {students.map((student) => (
          <li key={student.id}>{student.name} - {student.email}</li>
        ))}
      </ul>
    </div>
  );
}
