"""
Repeatedly display random colors on the underside NeoPixels.
The neo pixels are changed one at a time.  The number in
parentheses represents the time interval in milliseconds.
"""

from microbit import *
from cutebot import Cutebot

robot = Cutebot()

while True:
    robot.set_random_neopixel_colors(200)
    sleep(20)  
