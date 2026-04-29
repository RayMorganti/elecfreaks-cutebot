"""
The headlights are turn on, both white.  We tell the micro:bit 
to turn off the Cutebot's headlights after a delay of 5000 
milliseconds (5 seconds).
"""

from cutebot import *

bot = Cutebot()

# Set the RGB color of the headlights.
bot.set_car_headlight(left, 255, 255, 255)
bot.set_car_headlight(right, 255, 255, 255)

# Wait for 5 seconds
sleep(5000)

# Turn off the headlights
bot.set_car_headlight(left, 0, 0, 0)
bot.set_car_headlight(right, 0, 0, 0)
