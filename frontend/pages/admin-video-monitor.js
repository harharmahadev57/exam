import { useEffect, useRef } from "react";

export default function AdminVideoMonitor() {
  const videoRef = useRef(null);

  useEffect(() => {
    const socket = new WebSocket(`ws://localhost:8000/ws/video-stream/admin`);

    socket.onmessage = (event) => {
      const blob = new Blob([event.data], { type: "video/webm" });
      videoRef.current.src = URL.createObjectURL(blob);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div>
      <h2>Live Webcam Monitoring</h2>
      <video ref={videoRef} autoPlay controls />
    </div>
  );
}
