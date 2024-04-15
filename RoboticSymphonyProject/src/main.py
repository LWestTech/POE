# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Lucas West                                                   #
# 	Created:      4/15/2024, 10:08:12 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

motor = Motor(Ports.PORT1)

while True:
    motor.spin_to_position(15, DEGREES)
    motor.spin_to_position(0, DEGREES)
    wait(1, SECONDS)