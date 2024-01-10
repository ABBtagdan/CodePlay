import barcode
from flask import Flask, request, Response
import time
import os
from werkzeug.utils import secure_filename

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./Index.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    file = request.files['image']
    print(file)
    filename = secure_filename(file.filename)
    file.save(filename)  # get the image
    print(filename)
    barcode.get_sequence_from_image(filename)

    return Response("%s saved")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)