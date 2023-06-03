import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import { Row, Col, ListGroup, Button } from 'react-bootstrap';
import axios from 'axios';
import LoadingOverlay from 'react-loading-overlay-ts';
import RangeSlider from 'react-bootstrap-range-slider';


function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [responseImage, setResponseImage] = useState(null);
  const [isActive, setActive] = useState(false)
  const [numColor, setNumColor] = React.useState(16);
  const [angle, setAngle] = React.useState(360);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setSelectedImage(file);
  };

  const handleBlur = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true);
        const response = await axios.post('http://localhost:5000/blur', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        setActive(false);

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  const handleSobel = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true);
        const response = await axios.post('http://localhost:5000/sobel', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        setActive(false);
        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  const handleLaplacian = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true);
        const response = await axios.post('http://localhost:5000/laplacian', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        setActive(false);
        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  const handleUnsharp = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/unsharp', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleHistogramEqualized = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/histogram', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleOld = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/old', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleVignetting = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/vignetting_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handlePhotocopy = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/photocopy_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleNightvision = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/nightvision_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleMirror = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/mirror_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleGrayscale = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/grayscale_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handlePosterize = async (e) => {
    e.preventDefault();
    // console.log(numColor);

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);
      formData.append('numColor', numColor);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/posterize_api', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleRotate = async (e) => {
    e.preventDefault();
    // console.log(numColor);

    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);
      formData.append('angle', angle);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post('http://localhost:5000/rotate', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };


  return (
    <LoadingOverlay
      active={isActive}
      spinner
      text='Loading your content...'
    >
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
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Average Blur Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleBlur}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Sobel Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleSobel}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Laplacian Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleLaplacian}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Unsharp Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleUnsharp}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Histogram Equalized Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleHistogramEqualized}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Old Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleOld}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Vignetting Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleVignetting}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Nightvision Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleNightvision}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Photocopy Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handlePhotocopy}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Mirror Image
                  </div>
                  <div className='my-3 text-center'>
                    <Button variant="outline-dark" onClick={handleMirror}>Apply</Button>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Posterize Image
                  </div>
                  <div className='my-3 text-center'>
                  <Form>
                      <Form.Group controlId="numColorInput">
                        <Form.Label>Number of Color</Form.Label>
                        <Form.Control
                          type="number"
                          value={numColor}
                          onChange={e => setNumColor(e.target.value)}
                          min={2}
                          max={255}
                          step={1}
                        />
                      </Form.Group>
                      <div className='mt-3'>
                        <Button variant="dark" type='submit' onClick={handlePosterize}>Rotate</Button>
                      </div>
                    </Form>
                  </div>
                </ListGroup.Item>
                <ListGroup.Item>
                  <div className='my-3 text-center'>
                    Rotate Image
                  </div>
                  <div className='my-3 text-center'>
                    <Form>
                      <Form.Group controlId="angleInput">
                        <Form.Label>Angle</Form.Label>
                        <Form.Control
                          type="number"
                          value={angle}
                          onChange={e => setAngle(e.target.value)}
                          min={1}
                          max={360}
                          step={1}
                        />
                      </Form.Group>
                      <div className='mt-3'>
                        <Button variant="dark" type='submit' onClick={handleRotate}>Rotate</Button>
                      </div>
                    </Form>
                  </div>
                </ListGroup.Item>
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
    </LoadingOverlay>
  );
}

export default App;
