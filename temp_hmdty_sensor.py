# getest op 7 dec 2022 en het werkt met:
# plus (+) op 3.3 of 5V (pin linkboven of rechtsboven)
# min (-) koppelen aan Ground, bijv derde rechts (buitenkant of zijkant van de Pi)
# pin out of data koppelen aan pin GPIO 4 van de Pi (pin 7) (4-de binnenkant Pi)

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import datetime
import board
import Adafruit_DHT as adafruit_dht

# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D18)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def slaop(val1, val2):
    nu = datetime.datetime.now()
    nu_dt = nu.strftime("%d-%m-%Y")
    nu_tijd = nu.strftime("%H:%M:%S")

    with open("temp_humidity.txt", mode='a') as file:
         file.write('%s; %s; %s; %s\n' % 
               (nu_dt, nu_tijd, val1, val2))

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        slaop(temperature_c, humidity)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(1.0*60*5)
    #time.sleep(2)
