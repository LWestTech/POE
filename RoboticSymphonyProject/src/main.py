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
beatTime = 0.5 # Seconds

motor.spin_to_position(15, DEGREES)

def Strike():
    motor.spin_to_position(15, DEGREES)
    motor.spin_to_position(-15, DEGREES)

while True:
    wait(beatTime * 6, SECONDS) # Happy birthday to you
    Strike()
    wait(beatTime * 6, SECONDS) # Happy birthday to you
    Strike()
    wait(beatTime * 6, SECONDS) # Happy birthday dear ___
    wait(beatTime * 2, SECONDS) # ...
    wait(beatTime * 6, SECONDS) # Happy birthday to you
    Strike()