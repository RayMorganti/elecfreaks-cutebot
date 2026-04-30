"""
Run both motors at the same time.  They stop when the sonar
sensor detects an object 12 centimeters away.  Works best
if you use a hard flat object as an obstacle.

If you place the robot on a block, and keep it connected to
a computer, information from the sonar sensor is printed in
your code editor's Shell.

**How it works:**

The robot motors start moving forward.  get_distance()
repeatedly checks information coming from the ultrasonic
sensor. When an object is detected at 12 cm or closer,
both motors stop.

By default, distance is reported in centimeters.  In
order to change the measurement to inches, type `1`
between the parentheses in get_distance().

A reading of `0` means no valid distance was detected, so
the robot keeps moving.

**Suggestion for further exploration:**
- Use a ruler to test the accuracy of the sonar.
- Type `1` between the parentheses of get_distance, and test again.

"""

from microbit import sleep  
from cutebot import Cutebot  

robot = Cutebot() 
stop_distance = 12

try:
    
    while True:  # Start an infinite loop to keep checking the ultrasonic sensor.
        distance = robot.get_distance()  # Read the ultrasonic distance in centimeters.
        print(distance)
        if distance > stop_distance:  
            robot.set_motors_speed(50, 50)  # Run both motors forward at 50% speed.
        elif distance > 0 and distance <= stop_distance: # If a valid reading is at or below the stop distance.
            robot.set_motors_speed(0,0)  # Stop both motors.
        
except Exception as error:  
    print("Ultrasonic stop demo error:", error) 
    robot.set_motors_speed(0,0) 
    