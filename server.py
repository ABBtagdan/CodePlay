import barcode
from flask import Flask, request, Response
import time

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./Index.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    print(i)

    return Response("%s saved")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)