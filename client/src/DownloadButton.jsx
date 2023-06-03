import React from "react";
import { saveAs } from "file-saver";

const DownloadButton = ({ base64Image }) => {
  const handleDownload = () => {
    // Convert base64 to Blob
    const byteCharacters = atob(base64Image);
    const byteArrays = [];

    for (let i = 0; i < byteCharacters.length; i++) {
      byteArrays.push(byteCharacters.charCodeAt(i));
    }

    const byteArray = new Uint8Array(byteArrays);
    const blob = new Blob([byteArray], { type: "image/jpg" });

    // Save the file
    saveAs(blob, "image.jpg");
  };

  return (
    <button
      className="btn btn-sm btn-outline-secondary"
      onClick={handleDownload}
    >
      <i class="bi bi-download"></i>
    </button>
  );
};

export default DownloadButton;
