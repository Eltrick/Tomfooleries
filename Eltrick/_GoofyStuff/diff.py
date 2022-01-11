import os
import sys
import math

goofy = open(r"E:\_Tomfooleries\_Split\Goofy", 'r')
goofyContent = goofy.readlines()

eltrick = open(r"E:\_Tomfooleries\_Split\List", 'r')
eltrickContent = eltrick.readlines()

lineCount = len(goofyContent)

for i in range(0, lineCount):
    if goofyContent[i] not in eltrickContent:
        print(goofyContent[i])