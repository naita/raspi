# Raspberry Pi Tips & Tricks - https://raspberrytips.nl

import Adafruit_DHT
pinnr = 21 # onderste rechts 
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pinnr)

print(humidity)
print(temperature)
humidity = round(humidity, 2)
temperature = round(temperature, 2)

if humidity is not None and temperature is not None:

  print( 'Temperatuur: {0:0.1f}*C'.format(temperature) )
  print( 'Luchtvochtigheid: {0:0.1f}%'.format(humidity) )

else:

  print( 'Geen data ontvangen' )

