import cv2
from base_camera import BaseCamera
import os
import time
import random
from datetime import datetime


os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

#print(a)
class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)

        while True:
            for i in range(10):
                ret, frame = camera.read()
            try:

                # cv2.putText(frame,text,(x_sh*2-50,y_sh*2-50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),1,cv2.LINE_AA)
                yield cv2.imencode('.jpg', frame)[1].tobytes()

                # yield cv2.imencode('.jpg', frame)[1].tobytes()

            except:
                pass
