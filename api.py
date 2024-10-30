from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes


import logging
logging.getLogger('flask_cors').level = logging.DEBUG

# Define the directory where your images are stored
IMAGE_DIRECTORY = 'images'

@app.route('/image/<filename>')
def serve_image(filename):
    image_path = os.path.join(IMAGE_DIRECTORY, filename)
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True)
