# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Lucas West                                                   #
# 	Created:      3/27/2024, 10:15:48 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
motor = Motor(Ports.PORT10)
potentiometer = Potentiometer(brain.three_wire_port.a)
while True:
    brain.screen.print(potentiometer.angle(PERCENT))
    if (potentiometer.angle(PERCENT) > 25):
        motor.spin(FORWARD, potentiometer.angle(PERCENT), PERCENT)
    else:
        motor.stop()
    wait(30, MSEC)
    brain.screen.set_cursor(1,1)
    brain.screen.clear_screen()