# contributors:
#   Jacobus Burger (Jun 2024)
# description:
#   This is a low level wrapper for the motors (the motor control board, DAC, and associated GPIO pins). It includes only basic functionality.
import gpiozero
import board
import busio
from adafruit_mcp4725 import MCP4725



class Motor():
    def __init__(self, DIR_PIN, STOP_PIN, BRAKE_PIN, SPEED_ADDR, I2C_INTERFACE, dir_reversed=False):
    # attach digital pins for controlling features
        self.dir_reversed = dir_reversed
        self.DIR = gpiozero.DigitalOutputDevice(DIR_PIN, active_high=(not dir_reversed), initial_value=dir_reversed)
        self.STOP = gpiozero.DigitalOutputDevice(STOP_PIN, active_high=False, initial_value=True)      # 1 = off, 0 = on
        self.BRAKE = gpiozero.DigitalOutputDevice(BRAKE_PIN, active_high=False, initial_value=True)    # 1 = off, 0 = on
        # connect I2C DAC for controlling speed
        while not I2C_INTERFACE.try_lock():
            pass
        try:
            devices = I2C_INTERFACE.scan()
            print("I2C devices found:", [hex(device) for device in devices])
        except:
            print("COULDN'T CONNECT I2C DAC")
            exit()
        finally:
            I2C_INTERFACE.unlock()
        self.SPEED = MCP4725(I2C_INTERFACE, address=SPEED_ADDR)


    def move(self, speed, forward=True):
        # make sure preonditions are met
        assert(type(forward) == bool)
        assert(type(speed) == int)
        assert(0 <= speed <= 100)
        # set speed
        self.SPEED.normalized_value = speed / 100   # NOTE: minimum movement value is 0.1 - 10%
        # set direction value (when dir_reversed then forward = 1 otherwise forward = 0)
        self.DIR.value = int(forward) if self.dir_reversed else int(not forward)
        self.is_moving = True
    

    def stop(self):
        self.STOP.on()
        self.SPEED.normalized_value = 0
        self.is_moving = False


    def brake(self):
        self.BRAKE.toggle()
        self.SPEED.normalized_value = 0
        self.brake_on = bool(self.BRAKE.value)
        self.is_moving = False