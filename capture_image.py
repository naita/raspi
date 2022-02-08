from picamera import PiCamera
import time
from datetime import datetime



# take foto
def captureImage(fname):
    camera = PiCamera()
    camera.resolution = (1024,768)
    camera.framerate = 30
    camera.vflip = True

    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H:%M:%S")
    print(dt)
    try:
        camera.capture("fotos/"+fname+dt+".jpg") # ,use_video_port=True)
        time.sleep(5)
    finally:
        camera.close() #sleep(10)

def captureVideo():
    camera = PiCamera()
    camera.resolution = (1024,768)
    camera.framerate = 30
    camera.vflip = True

    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    camera.start_recording("filmpje_"+str(dt)+".h264")
    time.sleep(15)
    camera.stop_recording()
    camera.close()

imagelocation='/home/pi/raspi/fotos/'
while True:
    captureImage(imagelocation+"kweekkas_")
    time.sleep(60*(60-datetime.now().minute) ) # de tweede en volgende foto's worden op het hele uur genomen

''''
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
