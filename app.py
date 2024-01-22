#Tage

import barcode
from flask import Flask, request, Response
import flask
from werkzeug.utils import secure_filename
from flask_cors import CORS
from convertToSound import handleInput
import json
from flask import send_file
from create_song import concat_sound

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)
CORS(app)

inst = "Drums"

@app.route('/')
def barcodeSite():
    print("Requested")
    return Response(open('./barcode.html').read(), mimetype="text/html")

@app.route("/playMusic.js")
def script():
    return Response(open("./playMusic.js").read(), mimetype="text/plain")

@app.route("/sounds/<id>")
def getSound(id):
    return send_file("./sounds/"+id)

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
    sound_path_list = concat_sound(sound_path_list, inst)
    rsp = Response(json.dumps(sound_path_list), status=200, content_type="text/plain")
    rsp.cache_control.max_age = 0
    return rsp

@app.route("/instrument", methods=['POST'])
def instrument():
    global inst
    inst = str(request.data, encoding="utf-8")
    print(inst)
    return Response(status=200)

if __name__ == '__main__':
    app.run()
    
