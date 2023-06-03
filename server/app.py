from flask import Flask, request, jsonify
from PIL import Image, ImageFilter
import io
import base64
from flask_cors import CORS
from temp import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

@app.route('/grayscale_api', methods=['POST'])
def grayscale_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = grayscale(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/blur', methods=['POST'])
def blur():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = averaging_blur(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/oil', methods=['POST'])
def oil_painting_filter():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})
    
    try:
        # Open the image
        image = Image.open(image_file)
        # Apply the Oil Painting filter
        oil_painting = image.filter(ImageFilter.EMBOSS)

        # Adjust the intensity of the filter
        oil_painting = oil_painting.point(lambda i: i * 2)

        # Apply the brush size
        oil_painting = oil_painting.filter(ImageFilter.MaxFilter(11))

        # Save the filtered image
        buffered = io.BytesIO()
        oil_painting.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/sobel', methods=['POST'])
def sobel():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = sobel_operator(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/laplacian', methods=['POST'])
def laplacian():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = laplacian_filter(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/unsharp', methods=['POST'])
def unsharp():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = unsharp_masking(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/histogram', methods=['POST'])
def histogram():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = histogram_equalization(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/old', methods=['POST'])
def old():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = old_image(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/vignetting_api', methods=['POST'])
def vignetting_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = vignetting(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/photocopy_api', methods=['POST'])
def photocopy_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = photocopy(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/nightvision_api', methods=['POST'])
def nightvision_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = night_vision(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/mirror_api', methods=['POST'])
def mirror_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = mirror(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/posterize_api', methods=['POST'])
def posterize_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = posterize(image, request.form['numColor'])
        print(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})
    
@app.route('/rotate', methods=['POST'])
def rotate():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        format = image.format
        # Perform your image processing tasks here using the 'image' object
        image = rotate_image(image, request.form['angle'])
        print(image)
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})
    

if __name__ == '__main__':
    app.run()
