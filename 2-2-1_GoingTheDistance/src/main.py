# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Lucas West                                                   #
# 	Created:      3/25/2024, 10:09:17 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# API: https://www.robotmesh.com/studio/content/docs/vexv5-python/html/hierarchy.html

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

leftMotor = Motor(Ports.PORT1, False)
rightMotor = Motor(Ports.PORT10, True)
distanceSensor = Distance(Ports.PORT6)

while True :
    if (distanceSensor.object_distance(DistanceUnits.IN) < 2):
        leftMotor.stop()
        rightMotor.stop()
    elif (distanceSensor.object_distance(DistanceUnits.IN) < 3):
        leftMotor.spin(FORWARD, 50, PERCENT)
        rightMotor.spin(FORWARD, 50, PERCENT)
    else:
        leftMotor.spin(FORWARD, 100, PERCENT)
        rightMotor.spin(FORWARD, 100, PERCENT)
    wait(30, MSEC)