#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, jsonify

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

# import camera driver
from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        try:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print("error : ", e)


@app.route('/face_video')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

    Camera.set_video_source('rtsp://example:password@192.168.0.1/Streaming/Channels/101')

    #Camera.set_video_source(1)
    # Camera.set_video_source('../static/demo.mp4')
    # gen(Camera())
    app.run(host='0.0.0.0', port=5006, threaded=True)
    #app.run(host='localhost', port=8844, threaded=True)
