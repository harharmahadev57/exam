import { useEffect, useState } from "react";

export default function TabSwitchDetection({ studentId, onAutoSubmit }) {
  const [ws, setWs] = useState(null);
  const [tabSwitchCount, setTabSwitchCount] = useState(0);

  useEffect(() => {
    const socket = new WebSocket(`ws://localhost:8000/ws/tab-switch/${studentId}`);
    setWs(socket);

    socket.onmessage = (event) => {
      if (event.data === "warning") {
        alert("⚠️ Warning: Do not switch tabs!");
      } else if (event.data === "exam-auto-submit") {
        alert("❌ Exam Auto-Submitted due to multiple tab switches!");
        onAutoSubmit();
      }
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        socket.send("tab-switched");
        setTabSwitchCount((prev) => prev + 1);
      }
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);

    return () => {
      document.removeEventListener("visibilitychange", handleVisibilityChange);
      socket.close();
    };
  }, [studentId]);

  return null;
}
