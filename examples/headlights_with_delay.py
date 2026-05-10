'''
We tell the micro:bit to turn off the Cutebot's headlights
after a delay of 5 seconds (which is 5000 milliseconds).

**Requirements for Running Script from the Computer**

**Requirements for Running Script from the Computer**  
- cutebot.py has been uploaded to the micro:bit.
- The robot's power has been turned on.
- The micro:bit is connected to the computer,
- Your code interpreter must be set to BBC micro:bit, and
- Thonny must recognize the micro:bit.
- The robot must be placed on a block.
- Click the green Run button to run the code.
  
'''

from cutebot import *

bot = Cutebot()

# Set the RGB color of the headlights.
bot.set_headlight(left, 255, 255, 255)
bot.set_headlight(right, 255, 255, 255)

# Wait for 5 seconds
sleep(5000)

# Turn off the headlights
bot.set_headlight(left, 0, 0, 0)
bot.set_headlight(right, 0, 0, 0)
