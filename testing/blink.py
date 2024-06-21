# Jacobus Burger (2024)
# This file is to test GPIO pins with a simple LED blink program
import time
import gpiozero

led_g1 = gpiozero.LED(26)
led_g2 = gpiozero.LED(19)
led_g3 = gpiozero.LED(13)

led_y1 = gpiozero.LED(21)
led_y2 = gpiozero.LED(20)
led_y3 = gpiozero.LED(16)
led_y4 = gpiozero.LED(12)
leds = [led_g1, led_g2, led_g3, led_y1, led_y2, led_y3, led_y4]

while True:
	for led in leds:
		led.toggle()
		time.sleep(1)