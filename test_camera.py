from picamera import PiCamera
import time
from datetime import datetime

#from gpiozero import MotionSensor

#pin_nr = 23 # GPIO nr
#pir = MotionSensor(pin_nr)


camera = PiCamera()
camera.resolution = (1024,768)
camera.framerate = 30
camera.vflip = True

#camera.start_preview()
#time.sleep(2)

# take foto
def captureImage(f):
    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    print(dt)
    try:
        camera.capture(f+str(dt)+".jpg",use_video_port=True)
        time.sleep(5)
    finally:
        camera.close() #sleep(10)

def captureVideo():
    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    camera.start_recording("filmpje_"+str(dt)+".h264")
    time.sleep(15)
    camera.stop_recording()

#captureVideo()
captureImage("testbla_")

'''
while True:
    captureImage("testbla_")
    time.sleep(1*5)
    #captureVideo()
    #time.sleep(1*5)


while True:
    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    pir.wait_for_motion()
    print("motion detected")
    camera.start_recording("filmpje_"+str(dt)+".h264")
    time.sleep(10)
    pir.wait_for_no_motion()
    print("no motion")
#    camera.stop_recording()

'''
