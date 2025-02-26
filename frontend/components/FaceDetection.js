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
