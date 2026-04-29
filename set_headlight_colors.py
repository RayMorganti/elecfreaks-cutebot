"""
The numbers in parentheses set the colors of the headlights.  The
numbers are for red, green and blue, in that order.  You can set
each number anywhere between 0 and 255.  0 means no color and 255
is intense color.  If you set all of the colors to 0, the lights
will remain dark.  If you set all of the numbers to 255 the headlights
turn white.
"""

from cutebot import *

bot = Cutebot()

bot.set_car_headlight(left, 255, 0, 0)
bot.set_car_headlight(right, 0, 0, 255)
sleep(5000)
bot.set_car_headlight(left, 0, 0, 0)
bot.set_car_headlight(right, 0, 0, 0)
