import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# This is a mock implementation of the computer vision model
def identify_candy(image):
    # Replace this with your actual computer vision model
    return 'skittle'

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    # Check if an image was uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    # Get the uploaded image file
    image = request.files['image']

    # Check if the file is a valid image
    if not image.filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return jsonify({'error': 'Invalid image file type'}), 400

    # Identify the candy in the image
    candy = identify_candy(image)

    # Return the name of the candy
    return jsonify({'candy': candy})

@app.route('/validationSuccess', methods=['POST'])
def validation_success():
    # Replace with your code to handle successful validation
    image = request.files['image']
    candy = request.form['candy']
    save_path = 'validated/' + candy + '/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = save_path + image.filename
    if os.path.exists(file_path):
        # Append a number to the filename to make it unique
        file_name, file_ext = os.path.splitext(image.filename)
        i = 1
        while os.path.exists(save_path + file_name + '_' + str(i) + file_ext):
            i += 1
        file_path = save_path + file_name + '_' + str(i) + file_ext
    image.save(file_path)
    return 'Success'

@app.route('/validationFailed', methods=['POST'])
def validation_failed():
    # Replace with your code to handle failed validation
    image = request.files['image']
    candy = request.form['candy']
    save_path = 'failed/' + candy + '/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = save_path + image.filename
    if os.path.exists(file_path):
        # Append a number to the filename to make it unique
        file_name, file_ext = os.path.splitext(image.filename)
        i = 1
        while os.path.exists(save_path + file_name + '_' + str(i) + file_ext):
            i += 1
        file_path = save_path + file_name + '_' + str(i) + file_ext
    image.save(file_path)
    return 'Success'

if __name__ == '__main__':
    # Create the uploads directory if it doesn't exist
    os.makedirs('failed/m&m', exist_ok=True)
    os.makedirs('failed/m&m crispy', exist_ok=True)
    os.makedirs('failed/skittle', exist_ok=True)
    os.makedirs('failed/smarty', exist_ok=True)
    os.makedirs('validated/m&m', exist_ok=True)
    os.makedirs('validated/m&m crispy', exist_ok=True)
    os.makedirs('validated/skittle', exist_ok=True)
    os.makedirs('validated/smarty', exist_ok=True)
    # Start the Flask application
    app.run(host="localhost", port=5050)
