# Jacobus Burger (2024)
# Motor Controller Module
import gpiozero

PWM_PINS = [12, 13, 18, 19]

class Motor():
    PWM: int                            # PWM speed controller pin (value between 0 and 1 for speed)
    DIR: int                            # DIRection pin (Low: on, High: off)
    BRAKE: gpiozero.DigitalOutputDevice  # BRAKE controller pin (Low: off, High: on)
    STOP: gpiozero.DigitalOutputDevice  # (Emergency) STOP pin (Low: on, High: off)
    is_moving: bool                     # whether the motor is moving or stopped

    def __init__(self, PWM_PIN, DIR_PIN, STOP_GPIO):
        if PWM_PIN not in PWM_PINS:
            raise ValueError("Assigned PWM to non-PWM pin")
        if DIR_PIN in PWM_PINS:
            raise ValueError("Assigned digital pin to PWM pin")
        self.PWM = gpiozero.PWMOutputDevice(PWM_PIN)
        self.DIR = gpiozero.DigitalOutputDevice(DIR_PIN)
        self.BRAKE = STOP_GPIO

    def move(self, speed, forward=True):
        if not self.BRAKE.is_active: # deactivate brake
            self.BRAKE.on()
        if speed < 0 or speed > 100 or type(speed) != int: # check values are correct
            raise ValueError("Motor speed must be int between 0 and 100")
        # set movement speed (must be [0, 1])
        self.PWM.value = speed / 100
        # update status
        if self.PWM.value == 0:
            is_moving = False
        else:
            is_moving = True

    def stop(self):
        if self.STOP.is_active: # activate brake
            self.STOP.off()
            self.is_moving = False