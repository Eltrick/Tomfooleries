import os
import sys
import math

file = open(r".\List", 'r')
fileContent = file.readlines()
lineCount = len(fileContent)

for i in range(0, math.ceil(lineCount / 20)):
    newFile = open(r".\_Split\VR" + str(i + 1) + ".json", 'w')
    newFile.write("{" + '\n' + '  \"DisabledList\": [' + '\n')
    for j in range(0, lineCount):
        if math.floor(j / 20) != i:
            newFile.write(fileContent[j])
    newFile.write('\n' + "  ]," + '\n' + "  \"Operation\": 1" + '\n' + "}")
    newFile.close()