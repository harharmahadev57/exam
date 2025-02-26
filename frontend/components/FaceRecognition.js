import { useEffect } from "react";
import axios from "axios";

export default function FaceRecognition({ studentId }) {
  useEffect(() => {
    const captureFace = async () => {
      try {
        const video = document.createElement("video");
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");

        navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
          video.srcObject = stream;
          video.play();

          setTimeout(() => {
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            const imageBase64 = canvas.toDataURL("image/png").split(",")[1];

            axios.post("http://localhost:8000/check-face", { image_base64: imageBase64 }).then((res) => {
              alert(res.data.message);
            });

            stream.getTracks().forEach(track => track.stop());
          }, 5000); // **📌 5 सेकंड में Screenshot लें**
        });
      } catch (error) {
        console.error("Error capturing face:", error);
      }
    };

    // **📌 हर 1 मिनट में Face Scan करें**
    const interval = setInterval(captureFace, 60000);

    return () => clearInterval(interval);
  }, [studentId]);

  return null;
}
