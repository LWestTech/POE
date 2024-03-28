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
bumper = Limit(brain.three_wire_port.c)
motor_on = False
def toggleMotor ():
    global motor_on
    motor_on = not motor_on

bumper.pressed(toggleMotor)
while True:
    # brain.screen.print(potentiometer.angle(PERCENT))
    brain.screen.print(motor_on)
    print(motor_on)
    # if (potentiometer.angle(PERCENT) > 25):
    if (motor_on):
        # motor.spin(FORWARD, potentiometer.angle(PERCENT), PERCENT)
        motor.spin(FORWARD, 100, PERCENT)
    else:
        motor.stop()
    wait(30, MSEC)
    brain.screen.set_cursor(1,1)
    brain.screen.clear_screen()