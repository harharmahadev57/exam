import { useEffect, useRef } from "react";

export default function StudentWebcam({ studentId }) {
  const videoRef = useRef(null);

  useEffect(() => {
    const socket = new WebSocket(`ws://localhost:8000/ws/video-stream/${studentId}`);
    const constraints = { video: true };

    navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
      videoRef.current.srcObject = stream;
      const mediaRecorder = new MediaRecorder(stream, { mimeType: "video/webm" });

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          socket.send(event.data);
        }
      };

      mediaRecorder.start(1000);
    });

    return () => {
      socket.close();
    };
  }, [studentId]);

  return <video ref={videoRef} autoPlay playsInline />;
}
