"""
Turn on both of the bottom-side NeoPixels, and set their colors.
The numbers in parentheses represent red, green and blue, in
that order.  Each number can have a value between 0 and 255.
Higher numbers make the color darker, and lower numbers make
the color lighter.
"""

from microbit import *
from cutebot import Cutebot

bot = Cutebot()

bot.set_neopixels_both(0,255,0)
sleep(5000)
bot.set_neopixels_both(0,0,0)
