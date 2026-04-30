# docs/changes_from_original.md`

# Changes from the original module

This project provides a revised version of the original [`Cutebot.py`](https://github.com/elecfreaks/EF_Produce_MicroPython/blob/master/Cutebot.py) module from the Elecfreaks [`EF_Produce_MicroPython`](https://github.com/elecfreaks/EF_Produce_MicroPython) repository.

## Summary of major changes

### 1. Added new functionality

The following changes were made to expose control of the robot's neopixels, which was not available through the original module:
    
- added two imports:
    - neopixel
    - random
- added self.__np = neopixel.NeoPixel(pin15, 2) to
  __init__(...)
- added new methods:
    - set_neopixel(...)
    - set_neopixels_both(...)
    - set_random_neopixel_colors(...)

### 2. Renamed parts of the API

The name of the CUTEBOT() class was changed to Cutebot() to make it more Pythonic.

The following method was renamed for improved clarity and consistency:

- set_car_light() method renamed to set_car_headlight()

The name-main idiom at the end of the module was changed in order to reflect these renamings.

Because of these renamings, code written for the original module will need modification before it will work with this revised module. 

## Compatibility

Supported:

- Elecfreaks Cutebot
- BBC micro:bit v2

Not supported:

- Elecfreaks Cutebot Pro
