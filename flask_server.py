from flask import Flask, request, redirect

import os
import json
from face_util import face_rec

app = Flask(__name__)
@app.route('/face_rec', methods=['POST'])
def face_recognition():
    if request.method == 'POST':
        try:
            file = request.files.get('file')
            name = face_rec(file)
            return json.dumps({'email':name}), 200, {'ContentType':'application/json'}

        except:
            return json.dumps({'error':'error occurred!'}), 500, {'ContentType':'application/json'}


@app.route('/')
def hello_world():
    return 'face recognition api'

if __name__ == '__main__':
    app.run(host='0.0.0.0')