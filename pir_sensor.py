from gpiozero import MotionSensor
from datetime import datetime


pin_nr = 23 # GPIO nr
pir = MotionSensor(pin_nr)


while True:
    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    pir.wait_for_motion()
    print("motion detected at "+str(dt))
    pir.wait_for_no_motion()
    now = datetime.now()
    dt = now.strftime("%Y%m%d_%H%M%S")
    print("no motion at "+ str(dt))
