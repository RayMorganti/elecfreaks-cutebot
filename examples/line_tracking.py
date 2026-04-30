'''
The code will wait 2 seconds, to give you time
to move your hands aways from the robot.

Cutebot drives along a black path.  The robot
has two infrared on its underside to keep track
of the black path.  If the left sensor does not
see the path, the right motor stops, and
the robot turns to the right until the left
sensor again sees the path. If the right sensor
does not see the path, the left motor stops, and
the robot turns to the left until the right sensor
again sees the path.

NOTE:  (1) If you'd like to experiment with different
speeds, the motors do not perform well (sometimes
not at all) below a setting of 15%.  (2) We haven't
told the robot what to do if neither sensor can see
the path.  If you place the robot on a white area,
and then turn it on, it will do nothing.  If you move
the robot onto a white area after it has detected the
path, it will rotate continuously in a circle, in the
direction where it last saw the path. 
'''

from cutebot import *
from time import sleep

cutebot = Cutebot()

sleep(2)

while(True):
    # Get tracking information from the infrared sensors
    i = cutebot.get_tracking()

    # If the sensors return 10 (right sensor lost the path)
    if i == 10:
        # Stop the left motor, run the right motor at 25%.
        cutebot.set_motors_speed(0, 25)
    # If the sensors return 1 (the left sensor lost the path)
    if i == 1:
        # Stop the right motor, run the left motor at 25%.
        cutebot.set_motors_speed(25, 0)
    # If the sensors return 11 (both sensor detect the path)    
    if i == 11:
        # Keep the motors running at 25%
        cutebot.set_motors_speed(25, 25)  
