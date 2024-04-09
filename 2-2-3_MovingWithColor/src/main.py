# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Lucas West                                                   #
# 	Created:      3/29/2024, 10:09:25 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
motor = Motor(Ports.PORT1)
optical = Optical(Ports.PORT5)
optical.set_light(LedStateType.ON)
redPos = 0
greenPos = 60
bluePos = 30
led = Led(Ports.PORT6)

while True:
    led.off()
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    hue = optical.hue()
    if optical.is_near_object and hue is not None:
        if hue < -30 and hue > 30:
            led.on()
    wait(100, MSEC)