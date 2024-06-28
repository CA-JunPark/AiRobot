# this file is an abstraction to control the movement system on a high level
from motors import *

# create I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

#           DIR, STOP, BRAKE, I2C_ADDR
PINS_LEFT = ()

left = Motor(DIR, STOP, BRAKE, 0x60, i2c)
right = Motor(DIR, STOP, BRAKE, , i2c)