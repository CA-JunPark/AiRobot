import RPi.GPIO as GPIO
import time

# Pin definitions
A = 17  # GPIO pin connected to input A
B = 27  # GPIO pin connected to input B
C = 22  # GPIO pin connected to input C
G1 = 5  # GPIO pin connected to enable G1
G2A = 6  # GPIO pin connected to enable G2A
G2B = 13  # GPIO pin connected to enable G2B

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup GPIO pins
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(G1, GPIO.OUT)
GPIO.setup(G2A, GPIO.OUT)
GPIO.setup(G2B, GPIO.OUT)

# Enable the 74AC138
GPIO.output(G1, GPIO.HIGH)
GPIO.output(G2A, GPIO.LOW)
GPIO.output(G2B, GPIO.LOW)

def set_decoder(a, b, c):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)

try:
    while True:
        # Cycle through all output states
        for i in range(8):
            set_decoder(i & 0x01, (i >> 1) & 0x01, (i >> 2) & 0x01)
            time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
