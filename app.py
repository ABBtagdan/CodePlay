#Tage

import barcode
from flask import Flask, request, Response
import flask
from werkzeug.utils import secure_filename
from flask_cors import CORS
from convertToSound import handleInput
import json

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)
CORS(app)


@app.route('/')
def barcodeSite():
    print("Requested")
    return Response(open('./barcode.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    file = request.files['image']
    print(file)
    filename = secure_filename("temp_image_to_check.png")
    file.save(filename)  # get the image
    print(filename)
    seq = barcode.get_sequence_from_image(filename)
    print(seq)
    if seq[0] not in ["0", "1", "2", "3", "4"]:
        return Response("ERROR: "+seq, status=200, content_type="text/plain")
    sound_path_list = handleInput(seq)
    return Response(json.dumps(sound_path_list), status=200, content_type="text/plain")

if __name__ == '__main__':
    app.run()
    
