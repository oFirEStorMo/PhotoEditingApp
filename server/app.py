from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Invalid image file'})

    try:
        # Open and process the image
        image = Image.open(image_file)
        # Perform your image processing tasks here using the 'image' object
        
        # Convert the processed image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format='JPEG')
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
