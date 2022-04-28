# Raspberry Pi Tips & Tricks - https://raspberrytips.nl
import numpy as np
import Adafruit_DHT
import os
import time
from datetime import datetime
import gpiozero as gz # needed to monitor the pi temperatur

def openFile():
    try:
        f = open('/home/pi/sensorreadings.csv', 'a+')
        if ( os.stat('/home/pi/sensorreadings.csv').st_size == 0 ):
            f.write('DateTime; sensor_id; sensor_type; valuee\r\n')
        return f  
    except:
       pass
       return f

pin_nrs = [20, 21] # 20 is onderste pin rechts van de pi 


def measureTempHum(pin_nr):
   tempVec = np.ones(5)*-999
   humVec = np.ones(5)*-100
   print(tempVec)
   for i in range(0,5):
       humVec[i], tempVec[i] = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin_nr)
       print(tempVec[i])
       time.sleep(1)

   return np.median(humVec), np.median(tempVec)

def measureAndWriteTempHum():

   for pin_nr in pin_nrs:
      print(pin_nr)
      humidity, temperature = measureTempHum(pin_nr)
      hum = round(humidity, 2)
      temp = round(temperature, 2)

      if humidity is not None and temperature is not None:
         f=openFile()
         now = datetime.now()
         dt = now.strftime("%Y%m%d %H:%M:%S")
         str="{}; {}; temperature; {}\n".format(dt, pin_nr, temp)
         f.write(str)
         str="{}; {}; humidity; {}\n".format(dt, pin_nr, hum)
         f.write(str)

   cpu_temp = round(gz.CPUTemperature().temperature, 1)
   str="{}; {}; cpu; {}\n".format(dt, 0, cpu_temp)
   f.write(str)

   f.close()

while True:
    measureAndWriteTempHum()
    time.sleep(10*(60-datetime.now().minute) ) # de tweede en volgende measurements worden om hh:10, hh:20, etc  genomen
