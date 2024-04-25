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
bumper = Bumper(Triport(2))
beatTime = 0.5 # Seconds

def strike():
    motor.spin_to_position(30, DEGREES)
    motor.spin_to_position(0, DEGREES)

def wait_beats(beats):
    i = 0
    while i < beats:
        brain.screen.clear_line(2)
        brain.screen.set_cursor(2,1)
        brain.screen.print(i + 1)
        wait(beatTime, SECONDS)
        i += 1
        
motor.spin_to_position(0, DEGREES)

while True:
    wait(.02, SECONDS)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print ("Waiting for button...")
    if bumper.pressing():
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday dear ___")
        wait_beats(5) # Happy birthday dear ___
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("...")
        wait_beats(2) # ...
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print ("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()