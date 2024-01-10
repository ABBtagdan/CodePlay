import barcode
from flask import Flask, request, Response
import time
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)
CORS(app)


@app.route('/')
def barcodeSite():
    return Response(open('./barcode.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    file = request.files['image']
    print(file)
    filename = secure_filename("./temp/image_to_check.png")
    file.save(filename)  # get the image
    print(filename)
    seq = barcode.get_sequence_from_image(filename)
    print(seq)
    return Response(seq, status=200, content_type="text/plain")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)

    




"""
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./Index.html').read(), mimetype="text/html")

# simulate an error in the server response
@app.route('/image', methods=['POST'])
def image():
    return Response("Error uploading image!", status=500)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

"""