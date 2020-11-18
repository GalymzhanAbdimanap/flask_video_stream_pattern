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
        
        
        
    #==================================================
    # Flush buffer in camera.
    def flushCamera(camera):
        delay = 0

        framesWithDelayCount = 0
        flushed_frames = 0

        while (framesWithDelayCount <= 1):
            timer_start = time.time()

            camera.grab()
            flushed_frames += 1

            delay = time.time() - timer_start

            if (delay > 0):
                framesWithDelayCount += 1

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        flushCamera(camera)
        #option 1
        while True:  
            try:
                ret, frame = camera.read()
                flushCamera(camera)
                if frame is None:
                    camera = cv2.VideoCapture(Camera.video_source)
                    time.sleep(2)
                    continue
                #logic
                yield cv2.imencode('.jpg', frame)[1].tobytes()
            except:
                pass
            
           
        #option 2
        while True:
            if camera.isOpened():
                for i in range(5):
                    ret, image = camera.read()
            if ret:
                if image == 'None':
                    continue
            try:
                #logic
                yield cv2.imencode('.jpg', frame)[1].tobytes()
            except:
                pass
            
          
        #option 3
        while True:
            try:
                for i in range(5):
                    ret, frame = camera.read()
                 
                if frame is None:
                    # print("frame None")
                    camera = cv2.VideoCapture(Camera.video_source)
                    yield cv2.imencode('.jpg', frame)[1].tobytes()
                    continue
                    
                #logic
                yield cv2.imencode('.jpg', frame)[1].tobytes()
            except:
                pass
