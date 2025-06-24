from flask import Flask, request, jsonify
import os
import uuid
from PIL import Image
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/var/www/images'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        image_data = file.read()
        try:
            image = Image.open(io.BytesIO(image_data))
            image_format = image.format.lower()
            if image_format not in ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg']:
                return jsonify({'error': 'Unsupported image format'}), 400
        except Exception as e:
            return jsonify({'error':f'Invalid image: {str(e)}'}), 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'wb') as f:
            f.write(image_data)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

