[![Run on Repl.it](https://repl.it/badge/github/djm4556/ustores_solver)](https://repl.it/github/djm4556/ustores_solver)

# BUG REPORT: 0
This section stores known bugs if there are any. Luckily, there are none- it's all patched!

# About ustores_solver (UltraStores solver)
Semi-automatic solver for this Keep Talking and Nobody Explodes modded module:
https://ktane.timwi.de/HTML/UltraStores.html (Using rule seed 1, the default)

# FOR NEW USERS: About KTANE and UltraStores
KTANE is a video game about communicating to defuse bombs with puzzles, where (usually) the
"defuser" sees the bomb but not the manual with solutions, and the "experts" see the manual
but not the bomb. As such, the word "bomb" will be used strictly in the context of KTANE.
Strict players may consider this solver to ruin the fun, but in my personal opinion, there
is no fun to be had with this module. It's extremely difficult for both the defuser and the
expert, and is partially viewable as a "cruel" version of the _already mind-bending_ "Simon
Stores" thanks to its usage of mechanics from "The Ultracube". With one of its updates, it
even took a step ABOVE "The Ultracube" with a sixth dimension compared to "The Ultracube"
having "only" five. Rule seed 1 manuals for "Simon Stores" and "The Ultracube" are below.

https://ktane.timwi.de/HTML/Simon%20Stores.html
https://ktane.timwi.de/HTML/The%20Ultracube.html

TL:DR The "bomb" is not real, and this _devil_ exists despite all reason, so I made this.

# Basic Usage of the UltraStores Solver
First, take note of the fact that this program has no case sensitivity.

You will first be prompted for a six-character serial number that can be found on the side
of the bomb. Enter it, and be careful not to mistype, as changing the serial number will
require you to restart the program, deleting any data you put in.

After entering a valid serial number, the program will start asking for rotations, which
must be entered in the order they occur. A pause denotes the end of the rotation sequence,
meaning the first rotation comes after the pause and the last one comes before the pause.
Without advanced optical detection, there is no way to automatically detect rotations,
so it is up to the defuser to figure out which rotations are being used on the module.

**Combined Rotations**
Sometimes, two or three rotations will happen at once, appearing as one big complex
rotation and causing more than just two axes to change. I denote the smaller rotations
"sub-rotations" and the big one the "main rotation" or sometimes, just the "rotation".
To enter multiple sub-rotations, use a space between each. Remember: each of the sub-
rotations will have its own two axes that don't appear in other sub-rotations within
the same main rotation, so you shouldn't be entering one letter twice in a line here!

**Colors and Submission**
After inputting all of the rotations for a stage, you will be told to press the center
button on the module. This will cause the 6D cube to collapse and stop rotating until
you submit something, so be sure you know what the rotations were before doing this.
It will also reveal the colors of the eight buttons surrounding the center one, which
will change every submission attempt, but always have one button of each possible color.
Enter the colors' first letters (except black, which uses K) starting from the north-
most color and continuing clockwise around the module, without any spaces, to receive
an answer. (If you're lucky, you'll get an answer before even having to enter colors!)

This will be a sequence of letters that translate back to colors, just like how you
entered the button colors but in reverse. (A list of colors/letters is provided at the
bottom of this README.) Press the buttons with those colors in the given order, then
press the center button again to submit your answer. A two-tone chime can be heard if
your answer was correct, indicating you're on the next stage. If you were on stage 3
when you got a correct answer, the module's status light will turn green and the 6D
cube will be all green and stationary, indicating the module has been disarmed.

**Upon Receiving a Strike**
If you were incorrect, the module's status light will turn red, you'll hear a buzzer,
and you'll gain a strike, possibly causing the bomb to detonate. This means you have
to retry the stage you were on last, with the same rotations (and serial number), but
different colors. Re-reading the rotations is recommended, and re-inputting them into
the program is required to get to the color prompt. However, take careful note of this:

*Before entering anything else, enter "N" when prompted instead of just pressing enter,
so the program will reset that stage instead of advancing to the next one by default.
Also, the program assumes your presses begin with the white button lit (press to light).*

# Appendix: Colors and Letters Used
Red = R (primary)

Green = G (primary)

Blue = B (primary)

Cyan = C (secondary)

Magenta = M (secondary)

Yellow = Y (secondary)

White = W (neither)

blacK = K (neither)
