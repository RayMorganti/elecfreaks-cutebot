'''
The numbers in parentheses set the colors of the headlights.  The
numbers are for red, green and blue, in that order.  You can set
each number anywhere between 0 and 255.  0 means no color and 255
is intense color.  If you set all of the colors to 0, the lights
will remain dark.  If you set all of the numbers to 255 the headlights
turn white.  Practice changing the numbers to see how they affect the colors.
There are 16,777,216 possibilities.

**Requirements for Running Script from the Computer**

- cutebot.py has been uploaded to the micro:bit.
- The robot's power has been turned on.
- The micro:bit is connected to the computer,
- Your code interpreter must be set to BBC micro:bit, and
- Thonny must recognize the micro:bit.
- The robot must be placed on a block.
- Click the green Run button to run the code.

The headlights will glow in the colors you selected.
'''

from cutebot import *

bot = Cutebot()

bot.set_headlight(left, 255, 0, 0)
bot.set_headlight(right, 0, 0, 255)
sleep(5000)
bot.set_headlight(left, 0, 0, 0)
bot.set_headlight(right, 0, 0, 0)
