from time import sleep
from math import sin
import gpiozero


LED = 13
led = gpiozero.PWMLED(LED)


led.on()
while True:
    for i in range(64):
        led.value = abs(sin(i / 16))
        sleep(0.1)
        print(led.value)