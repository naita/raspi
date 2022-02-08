# Raspberry Pi Tips & Tricks - https://raspberrytips.nl

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

pin_nr = 21 # onderste rechts 
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin_nr)

print(humidity)
print(temperature)
hum = round(humidity, 2)
temp = round(temperature, 2)

while True:
   humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin_nr)
   hum = round(humidity, 2)
   temp = round(temperature, 2)
   cpu_temp = round(gz.CPUTemperature().temperature, 1)

   if humidity is not None and temperature is not None:
       f=openFile()
       now = datetime.now()
       dt = now.strftime("%Y%m%d %H:%M:%S")
       str="{}; {}; temperature; {}\n".format(dt, pin_nr, temp)
       f.write(str)
       str="{}; {}; humidity; {}\n".format(dt, pin_nr, hum)
       f.write(str)
       str="{}; {}; cpu; {}\n".format(dt, 0, cpu_temp)
       f.write(str)

       f.close()

       time.sleep(10*60)
