'''
The numbers in parentheses set the speed of the motors.
The first number sets the speed of the left motor and
the second number controls the speed of the right motor.
Theoretically, you can set the numbers between 0 and 100.
but the motors typically will not move at settings lower
than 15.  The numbers can be positive or negative.  Positive
numbers make the motors spin forward and negative numbers
make the motors spin backward.
'''

from microbit import sleep
from cutebot import Cutebot

bot = Cutebot()

bot.set_motors_speed(60, 60)
sleep(5000)
bot.set_motors_speed(0, 0)
