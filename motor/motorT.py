from gpiozero import *
import time 

p = PWMOutputDevice(12) # 3.3v

while True:
    p.value = 0.4
    p.frequency = 12
    time.sleep(5)
