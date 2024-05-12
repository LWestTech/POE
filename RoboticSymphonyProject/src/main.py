# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Lucas West                                                   #
# 	Created:      4/15/2024, 10:08:12 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
import array
from vex import *
# from collections import OrderedDict

# Brain should be defined by default
brain=Brain()
motor = Motor(Ports.PORT5)
bumper = Bumper(brain.three_wire_port.b)
beatTime = 0.6 # Seconds
beatsPerMeasure = 8
playing = False

class Note:
    def play(self):
        strike()

class Measure:
    array = []
    def addNote(self, note):
        self.array.append(note)
    def play(self):
        for note in self.array:
            note.play()
        

def strike():
    motor.spin_to_position(4, DEGREES)
    motor.spin_to_position(-30, DEGREES)
    
def print(text):
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print(text)


def wait_beats(beats):
    i = 0
    while beats > 0:
        if beats >= 1:
            print(i + 1)
            wait(beatTime, SECONDS)
            i += 1
            beats -= 1
        else:
            print(str(beats))
            wait(beatTime * beats, SECONDS)
            beats = 0

while True:
    wait(.01, SECONDS)
    print("Waiting for button...")
    if bumper.pressing():
        motor = Motor(Ports.PORT5)
        motor.spin_to_position(-30, DEGREES)
        print("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()
        wait(3 * beatTime, SECONDS)
        print("Happy birthday to you")
        wait_beats(5) # Happy birthday to you
        strike()
        wait(3 * beatTime, SECONDS)
        print("Happy birthday dear ___")
        wait_beats(6) # Happy birthday dear ___
        print("...")
        wait_beats(1) # ...
        print("Happy birthday to you")
        wait_beats(6.1) # Happy birthday to you
        strike()
    motor = Motor(Ports.PORT20)