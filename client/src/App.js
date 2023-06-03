import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import { Row, Col, ListGroup, Button } from 'react-bootstrap';
import axios from 'axios';

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [responseImage, setResponseImage] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setSelectedImage(file);
  };

  const handleGrayscale = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        const response = await axios.post('http://localhost:5000/grayscale_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  return (
    <div>
      <Container>
        <Row>
          <Col xs={3} md={2}>
            <div className='text-center my-5'>
              <h1>Filters</h1>
            </div>
            <ListGroup>
              <ListGroup.Item>
                <div className='my-3 text-center'>
                  Grayscale Image
                </div>
                <div className='my-3 text-center'>
                  <Button variant="outline-dark" onClick={handleGrayscale}>Apply</Button>
                </div>
              </ListGroup.Item>
              <ListGroup.Item>Dapibus ac facilisis in</ListGroup.Item>
              <ListGroup.Item>Morbi leo risus</ListGroup.Item>
              <ListGroup.Item>Porta ac consectetur ac</ListGroup.Item>
              <ListGroup.Item>Vestibulum at eros</ListGroup.Item>
            </ListGroup>
          </Col>
          <Col xs={12} md={8}>
            <div className='text-center my-5'>
              <h1>Image Input</h1>
            </div>
            <Form>
              <Form.Group>
                <Form.Control
                  type="file"
                  accept="image/*"
                  onChange={handleImageChange}
                />
                <div className='text-center my-5'>
                  <h1>Selected Image</h1>
                </div>
                {selectedImage && (
                  <div className="mt-3 text-center">
                    <img
                      src={URL.createObjectURL(selectedImage)}
                      alt="Selected"
                      className="img-fluid"
                    />
                  </div>
                )}
                <div className='text-center my-5'>
                  <h1>Processed Image</h1>
                </div>
                {responseImage && (
                  <div className="mt-3 text-center">
                    <img
                      src={`data:image/jpeg;base64,${responseImage}`}
                      alt="Processed"
                      className="img-fluid"
                    />
                  </div>
                )}
              </Form.Group>
            </Form>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
