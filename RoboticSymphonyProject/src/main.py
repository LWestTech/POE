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
motor = Motor(Ports.PORT5)
bumper = Bumper(brain.three_wire_port.b)
beatTime = 0.6 # Seconds
motor.spin_to_position(-30, DEGREES)

def strike():
    motor.spin_to_position(4, DEGREES)
    motor.spin_to_position(-30, DEGREES)

def wait_beats(beats):
    i = 0
    while beats > 0:
        if beats >= 1:
            brain.screen.clear_line(2)
            brain.screen.set_cursor(2,1)
            brain.screen.print(i + 1)
            wait(beatTime, SECONDS)
            i += 1
            beats -= 1
        else:
            brain.screen.clear_line(2)
            brain.screen.set_cursor(2,1)
            brain.screen.print("~ " + beats)
            wait(beatTime * beats, SECONDS)

while True:
    wait(.01, SECONDS)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print ("Waiting for button...")
    if bumper.pressing():
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()
        wait(3 * beatTime, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()
        wait(3 * beatTime, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday dear ___")
        wait_beats(6) # Happy birthday dear ___
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("...")
        wait_beats(1) # ...
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday to you")
        wait_beats(6) # Happy birthday to you
        strike()