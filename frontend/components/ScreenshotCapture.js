import { useEffect } from "react";
import axios from "axios";

export default function ScreenshotCapture({ studentId }) {
  useEffect(() => {
    const captureScreenshot = async () => {
      try {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.drawImage(document.documentElement, 0, 0, canvas.width, canvas.height);

        const imageBase64 = canvas.toDataURL("image/png").split(",")[1]; // **📌 Base64 में Convert करें**
        
        // **📌 Server पर भेजें**
        await axios.post("http://localhost:8000/upload-screenshot", { 
          student_id: studentId, 
          screenshot_base64: imageBase64 
        });

        console.log("Screenshot captured & uploaded!");
      } catch (error) {
        console.error("Error capturing screenshot:", error);
      }
    };

    // **📌 हर 30 सेकंड में Screenshot ले**
    const interval = setInterval(captureScreenshot, 30000);

    return () => clearInterval(interval);
  }, [studentId]);

  return null;
}


import { useEffect } from "react";

export default function ScreenshotCapture({ studentId }) {
  useEffect(() => {
    const captureScreenshot = async () => {
      const canvas = document.createElement("canvas");
      const video = document.createElement("video");

      try {
        const stream = await navigator.mediaDevices.getDisplayMedia({ video: true });
        video.srcObject = stream;
        await video.play();

        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        stream.getTracks().forEach(track => track.stop());

        canvas.toBlob(async (blob) => {
          const formData = new FormData();
          formData.append("file", blob);
          formData.append("student_id", studentId);

          await fetch("http://localhost:8000/upload-screenshot/", {
            method: "POST",
            body: formData,
          });
        }, "image/png");
      } catch (err) {
        console.error("Screenshot capture failed:", err);
      }
    };

    const interval = setInterval(captureScreenshot, 30000); // **📌 हर 30 सेकंड में Screenshot**
    return () => clearInterval(interval);
  }, [studentId]);

  return null;
}
