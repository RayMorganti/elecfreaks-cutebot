"""
Turn on one or both of the bottom-side NeoPixels, and set their
colors, independently.  They turn off after 5000 milliseconds, i.e.
5 seconds.

The first number in parentheses represents the left or right
neopixel.  Left is 0 and right is 1.  The next three numbers in
parentheses represent red, green and blue, in that order.  Each
number can have a value between 0 and 255.  Higher numbers make
the color darker, and lower numbers make the color lighter.
"""

from microbit import *
from cutebot import Cutebot

bot = Cutebot()

bot.set_neopixel(0,0,255,0)
bot.set_neopixel(1,0,0,255)
sleep(5000)
bot.set_neopixel(0,0,0,0)
bot.set_neopixel(1,0,0,0)
