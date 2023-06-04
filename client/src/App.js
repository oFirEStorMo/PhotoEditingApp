import React, { useState, useRef } from "react";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import { Row, Col, ListGroup, Button } from "react-bootstrap";
import axios from "axios";
import LoadingOverlay from "react-loading-overlay-ts";
import RangeSlider from "react-bootstrap-range-slider";
import DownloadButton from "./DownloadButton";

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [responseImage, setResponseImage] = useState(null);
  const [isActive, setActive] = useState(false);
  const [numColor, setNumColor] = React.useState(16);
  const [angle, setAngle] = React.useState(360);
  const [brightness, setBrightness] = useState(0);
  const [contrast, setContrast] = useState(1);
  const [imageFormat, setImageFormat] = useState('');
  const fileInputRef = useRef(null);

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImageFormat(file.type)
    setSelectedImage(file);
  };

  const handleBlur = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true);
        const response = await axios.post(
          "http://localhost:5000/blur",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        setActive(false);

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  const handleSobel = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true);
        const response = await axios.post(
          "http://localhost:5000/sobel",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        setActive(false);
        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  const handleLaplacian = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true);
        const response = await axios.post(
          "http://localhost:5000/laplacian",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        setActive(false);
        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  const handleUnsharp = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/unsharp",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleHistogramEqualized = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/histogram",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleOld = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/old",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleVignetting = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/vignetting_api",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handlePhotocopy = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/photocopy_api",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleNightvision = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/nightvision_api",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleMirror = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/mirror_api",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleGrayscale = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/grayscale_api",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleOilPainting = async (e) => {
    e.preventDefault();

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/oil",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        console.log(response.data);

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
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
      formData.append("image", selectedImage);
      formData.append("numColor", numColor);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/posterize_api",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
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
      formData.append("image", selectedImage);
      formData.append("angle", angle);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/rotate",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleBrightness = async (e) => {
    e.preventDefault();
    // console.log(numColor);

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);
      formData.append("factor", brightness);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/brightness",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        console.log(response);
        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleContrast = async (e) => {
    e.preventDefault();
    // console.log(numColor);

    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);
      formData.append("factor", contrast);

      try {
        setActive(true); // Set active to true at the beginning of the try block

        const response = await axios.post(
          "http://localhost:5000/contrast",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        setResponseImage(response.data.image);
        // console.log(response.data.image)
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setActive(false); // Set active to false at the end of the axios function
      }
    }
  };

  const handleOnClick = e => {
    // setImageType('edit');
    const base64Data = responseImage.replace(/^data:image\/(png|jpeg|jpg);base64,/, '');

  // Decode the base64 data
  const binaryData = atob(base64Data);

  // Create an ArrayBuffer from the binary data
  const arrayBuffer = new ArrayBuffer(binaryData.length);
  const uint8Array = new Uint8Array(arrayBuffer);
  for (let i = 0; i < binaryData.length; i++) {
    uint8Array[i] = binaryData.charCodeAt(i);
  }

  // Create a Blob object from the ArrayBuffer
  const blob = new Blob([uint8Array], { type: imageFormat }); // Change the MIME type if necessary
    setSelectedImage(blob);
  }

  return (
    <LoadingOverlay active={isActive} spinner text="Loading your content...">
      <div className="mx-3">
        {selectedImage && (
          <div className="text-center my-3">
            <h1>GhoshaMaja</h1>
          </div>
        )}

        {!selectedImage && (
          <Form>
            <Form.Group>
              <Form.Control
                type="file"
                accept="image/*"
                ref={fileInputRef}
                style={{ display: "none" }}
                onChange={handleImageChange}
              />
              <div
                style={{ minHeight: "80vh" }}
                className="d-flex justify-content-center align-items-center"
              >
                <div class="card p-5">
                  <h3 class="card-header text-center">GhoshaMaja</h3>
                  <div class="card-body text-center p-5">
                    <h5 class="card-title">
                      Easily Upload and Enhance Your Photos with our Simple and
                      Reliable GhoshaMaja App!
                    </h5>
                    <Button
                      className="mt-3"
                      variant="outline-success"
                      onClick={handleButtonClick}
                    >
                      Browse & Upload
                    </Button>
                  </div>
                </div>
              </div>
            </Form.Group>
          </Form>
        )}
        {selectedImage && (
          <Row>
            <Col xs={12} md={2}>
              <div className="text-center">
                <h4>Filters</h4>
              </div>
              <div className="listgroup-container border border-2 rounded-2 mt-3">
                <ListGroup>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Change Image</div>
                    <div className="my-3 text-center">
                      <Form.Control
                        type="file"
                        accept="image/*"
                        ref={fileInputRef}
                        style={{ display: "none" }}
                        onChange={handleImageChange}
                      />
                      <Button
                        variant="outline-success"
                        onClick={handleButtonClick}
                      >
                        Choose
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Brightness</div>
                    <div className="my-3 text-center">
                      <RangeSlider min={-100} max={100} value={brightness} onChange={e=>{setBrightness(e.target.value)}} onAfterChange={handleBrightness} />
                      {/* <Button
                        variant="outline-success"
                        onClick={handleBrightness}
                      >
                        Apply
                      </Button> */}
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Contrast</div>
                    <div className="my-3 text-center">
                    <RangeSlider min={0.1} max={4} step={0.1} value={contrast} onChange={e=>{setContrast(e.target.value)}} onAfterChange={handleContrast} />
                      {/* <Button
                        variant="outline-success"
                        onClick={handleContrast}
                      >
                        Apply
                      </Button> */}
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Grayscale Image</div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handleGrayscale}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  {/* <ListGroup.Item>
                    <div className="my-3 text-center">Oil Painting Filter</div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handleOilPainting}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item> */}
                  <ListGroup.Item>
                    <div className="my-3 text-center">Average Blur Image</div>
                    <div className="my-3 text-center">
                      <Button variant="outline-success" onClick={handleBlur}>
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Sobel Image</div>
                    <div className="my-3 text-center">
                      <Button variant="outline-success" onClick={handleSobel}>
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Laplacian Image</div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handleLaplacian}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Unsharp Image</div>
                    <div className="my-3 text-center">
                      <Button variant="outline-success" onClick={handleUnsharp}>
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">
                      Histogram Equalized Image
                    </div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handleHistogramEqualized}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Old Image</div>
                    <div className="my-3 text-center">
                      <Button variant="outline-success" onClick={handleOld}>
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Vignetting Image</div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handleVignetting}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Nightvision Image</div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handleNightvision}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Photocopy Image</div>
                    <div className="my-3 text-center">
                      <Button
                        variant="outline-success"
                        onClick={handlePhotocopy}
                      >
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Mirror Image</div>
                    <div className="my-3 text-center">
                      <Button variant="outline-success" onClick={handleMirror}>
                        Apply
                      </Button>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Posterize Image</div>
                    <div className="my-3 text-center">
                      <Form>
                        <Form.Group controlId="numColorInput">
                          <Form.Label>Number of Color</Form.Label>
                          <Form.Control
                            type="number"
                            value={numColor}
                            onChange={(e) => setNumColor(e.target.value)}
                            min={2}
                            max={255}
                            step={1}
                          />
                        </Form.Group>
                        <div className="mt-3">
                          <Button
                            variant="outline-success"
                            type="submit"
                            onClick={handlePosterize}
                          >
                            Apply
                          </Button>
                        </div>
                      </Form>
                    </div>
                  </ListGroup.Item>
                  <ListGroup.Item>
                    <div className="my-3 text-center">Rotate Image</div>
                    <div className="my-3 text-center">
                      <Form>
                        <Form.Group controlId="angleInput">
                          <Form.Label>Angle</Form.Label>
                          <Form.Control
                            type="number"
                            value={angle}
                            onChange={(e) => setAngle(e.target.value)}
                            min={1}
                            max={360}
                            step={1}
                          />
                        </Form.Group>
                        <div className="mt-3">
                          <Button
                            variant="outline-success"
                            type="submit"
                            onClick={handleRotate}
                          >
                            Rotate
                          </Button>
                        </div>
                      </Form>
                    </div>
                  </ListGroup.Item>
                </ListGroup>
              </div>
            </Col>
            <Col xs={12} md={5}>
              <div className="text-center">
                <h4>Selected Image</h4>
              </div>
              {selectedImage && (
                <div className="mt-3 text-center border border-4 rounded">
                  <img
                    src={URL.createObjectURL(selectedImage)}
                    style={{ maxHeight: "80vh" }}
                    alt="Selected"
                    className="img-fluid"
                  />
                </div>
              )}
            </Col>
            <Col xs={12} md={5}>
              {responseImage && (
                <>
                  <div className="d-flex justify-content-center">
                    <h4 className="me-3">Processed Image</h4>
                    <div>
                      <DownloadButton base64Image={responseImage} />
                      <button className="btn btn-sm ms-3 btn-outline-success" onClick={handleOnClick}>Save and Apply More</button>
                    </div>
                  </div>
                  <div className="mt-2 text-center border border-4 rounded">
                    <img
                      src={`data:image/jpeg;base64,${responseImage}`}
                      style={{ maxHeight: "80vh" }}
                      alt="Processed"
                      className="img-fluid"
                    />
                  </div>
                </>
              )}
            </Col>
          </Row>
        )}
      </div>
    </LoadingOverlay>
  );
}

export default App;
