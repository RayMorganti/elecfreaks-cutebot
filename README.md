# elecfreaks-cutebot

A modified MicroPython module for the Elecfreaks Cutebot on the BBC micro:bit v2.

## Overview

This project provides a revised version of the original [`cutebot.py`](https://github.com/elecfreaks/EF_Produce_MicroPython/blob/master/cutebot.py) module from the Elecfreaks [`EF_Produce_MicroPython`](https://github.com/elecfreaks/EF_Produce_MicroPython) repository.

This revision is intended specifically for the **Elecfreaks Cutebot** and is designed for use with the **BBC micro:bit v2**.

## Important compatibility note

**This module supports Cutebot only.**  Cutebot Pro is not supported.

## Main changes in this revision

- added `set_neopixel(...)`
- added `set_neopixels_both(...)`
- added `set_random_neopixel_colors(...)`
- revised `get_tracking(...)`
- renamed many classes, methods, and constants for greater clarity and consistency 

## Origin

This project is based on code from the Elecfreaks repository:

- Repository: [`EF_Produce_MicroPython`](https://github.com/elecfreaks/EF_Produce_MicroPython)
- Original file used for this revision: [`cutebot_pro.py`](https://github.com/elecfreaks/EF_Produce_MicroPython/blob/master/cutebot.py)

The Elecfreaks repository is a fork of:
- https://github.com/lionyhw/EF_Produce_MicroPython

The upstream repository uses the MIT License. The Elecfreaks fork also includes the MIT License.

## Files

- [`cutebot.py`](cutebot.py) — the main MicroPython module
- [`examples/`](examples/) — example programs
- [`docs/changes_from_original.md`](docs/changes_from_original.md) — summary of key changes from the original module
- [`LICENSE`](LICENSE) — license information

## Installation

Copy [`cutebot.py`](cutebot.py) to your BBC micro:bit using your preferred MicroPython file transfer method.

## Compatibility

Tested on actual hardware:

- BBC micro:bit v2
- Elecfreaks Cutebot

Not supported:

- Elecfreaks Cutebot Pro

## Migration warning for users of the original module

This is **not** a drop-in replacement for the original [`cutebot.py`](https://github.com/elecfreaks/EF_Produce_MicroPython/blob/master/cutebot.py) in all cases.

Because this revision renames parts of the API, existing code written for the original module may need to be updated.

Changes include:

- class names
- method names
- constant names

See [`docs/changes_from_original.md`](docs/changes_from_original.md) for a summary of major differences.

## Development note

This revised version was developed with AI assistance. Generated code and documentation were reviewed, edited, and tested on actual Elecfreaks Cutebot and BBC micro:bit v2 hardware by the repository author.

## License

This repository contains code derived from an MIT-licensed project. See the [`LICENSE`](LICENSE) file for details.
