import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [imageFile, setImageFile] = useState(null);
  const [responseImage, setResponseImage] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setImageFile(file);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (imageFile) {
      const formData = new FormData();
      formData.append('image', imageFile);

      try {
        const response = await axios.post('http://localhost:5000/process_image', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  return (
    <div>
      <h1>Image Processing App</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit">Process Image</button>
      </form>
      {responseImage && (
        <div>
          <h2>Processed Image</h2>
          <img src={`data:image/jpeg;base64,${responseImage}`} alt="Processed" />
        </div>
      )}
    </div>
  );
}

export default App;
