#micropython pico moard
from machine import ADC
import time
from math import log

potentiometer = ADC(27)     # Grove - Temperature Sensor connect to A0
B = 4275;               # B value of the thermistor
R0 = 100000;            # R0 = 100k

sensor_temp = ADC(4) # Connect to the internal temperature sensor
conversion_factor = 3.3 / (65535)

def convert(x,in_min,in_max,out_min,out_max):
    return(x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    #internal pico temperature
    reading = sensor_temp.read_u16() * conversion_factor
    tempePico = 27 - (reading - 0.706)/0.001721
    
    #Grove temperature
    tb = convert(potentiometer.read_u16(),0,65535,0,1023)
    R = ((1023.0/tb)-1.0) * R0
    tempGrove = (1.0/ (log(R/100000)/B+1/298.15) )-273.15
    print("Grove temperature  %.0f ,Pico temperature %.0f " %(tempGrove,tempePico)) 
    time.sleep(2)       
    
