from gpiozero import MotionSensor
from datetime import datetime
import os
import time
from picamera import PiCamera


pin_nr = 23 # GPIO nr
pir = MotionSensor(pin_nr)

def openFile():
  try:
    f = open('/home/pi/sensorreadings.csv', 'a+')
    if ( os.stat('/home/pi/sensorreadings.csv').st_size == 0 ):
       f.write('DateTime; sensor_id; sensor_type; value\r\n')
    return f
  except:
    pass
    return f

videoduur=10  # seconden

def captureVideo(fname):
    camera = PiCamera()
    camera.resolution = (1024,768)
    camera.framerate = 30
    camera.vflip = True
    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    print(dt)
    try:
        camera.start_recording(fname+dt+".h264")
        #camera.capture(fname+dt+".jpg")
        time.sleep(videoduur)
    finally:
        camera.stop_recording()
        #camera.stop()
        camera.close() 


lasttakenphoto = datetime.now()
threshold_duur = 600 # als er gedurende meer dan 10 min geen beweging is

videolocation='/home/pi/raspi/videos/'
while True:
    f=openFile()
    pir.wait_for_motion()
    now = datetime.now()
    dt = now.strftime("%Y%m%d %H:%M:%S")
    print("motion detected at "+dt)
    if ( (now-lasttakenphoto).total_seconds() > threshold_duur ):
       captureVideo(videolocation+"video_")
       lasttakenphoto = now
       str="{}; {}; video; {}\n".format(dt, 0, videoduur)
       f.write(str)
    str="{}; {}; motion; 1\n".format(dt, pin_nr)
    f.write(str)

    pir.wait_for_no_motion()
    now = datetime.now()
    dt = now.strftime("%Y%m%d %H:%M:%S")
    print("NO motion at "+dt)
    str="{}; {}; motion; 0\n".format(dt, pin_nr)
    f.write(str)
    f.close()

