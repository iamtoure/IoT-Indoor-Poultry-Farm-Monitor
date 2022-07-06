import time
import pycom
import machine
import struct
import socket

from machine import ADC
from machine import Pin
from SI7006A20 import SI7006A20     #https://github.com/pycom/pycom-libraries

# supporting python library for Pysense 2.0 X
from pycoproc_2 import Pycoproc     #https://github.com/pycom/pycom-libraries

pycom.heartbeat(False) # Turn off heartbeat
pycom.rgbled(0x0A0A08) # white

py = Pycoproc()

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)  #create LoRa socket
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  #Set LoRaWAN data date
s.setblocking(False) #Turn off socket blocking



# Temperature and Humidity Sensor
dht = SI7006A20(py)
print("Temperature: " + str(dht.temperature())+ " deg C and Relative Humidity: " + str(dht.humidity()) + " %RH")


#Photoresistor Sensor.  https://github.com/iot-lnu/applied-iot/blob/master/sensor-examples/Photoresistor/main.py
LightSensorPin = 'P16' # Define sensor pin
lightPin = Pin(LightSensorPin, mode=Pin.IN)  # set up pin mode to input
adc = ADC(bits=10)             # create an ADC object bits=10 means range 0-1024 the lower value the less light detected
apin = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)   # create an analog pin on P16;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v
val = apin() # read an analog value
print("Value", val)




#
while True:

    temperature = dht.temperature()
    humidity = dht.humidity()
    light = apin()


    """
    Prepare data packing to send to Helium
    Payload format is: >hBH where
    h = Temperature         (2 bytes, 16 bits, signed)       Range: -32,768 to 32,767
    B = Humidity            (1 byte,  8 bits,  unsigned)     Range: 0 to 255
    H = Light               (2 bytes, 16 bits, unsigned)     Range: 0 to 65,535

    """
    package = struct.pack('>hBH',
                            int(temperature),
                            int(humidity),
                            int(light))
    s.send(package)     #Send data
    print('Sensor data sent!')     # Confirm data sent
    time.sleep(300)         # Sleep 5 minutes before uploading new data.
