import math

numberGrid = [
    [5, 1, 3, 6, 4, 0, 2], 
    [1, 2, 6, 4, 0, 5, 3], 
    [4, 0, 5, 1, 3, 2, 6], 
    [3, 5, 2, 0, 1, 6, 4], 
    [0, 3, 4, 2, 6, 1, 5], 
    [6, 4, 0, 5, 2, 3, 1], 
    [2, 6, 1, 3, 5, 4, 0]
]

truthValues = [False, False, False, False, False, False, False]
otherKugels = [False, False, False, False, False, False, False]
pivot = [0, 0, 0]
binaryStuff = ["000", "001", "010", "011", "100", "101", "110"]
storedb = []

def main() -> None:
    global numberGrid
    global truthValues
    global pivot
    global storedb
    global otherKugels
    
    red = [0, 0, 0, 0, 0, 0, 0]
    orangeValues = [False, False, False, False, False, False, False]
    yellowValues = [False, False, False, False, False, False, False]
    green = [0, 0, 0, 0, 0, 0, 0]
    blue = [0, 0, 0, 0, 0, 0, 0]
    finalBlueValues = [3, 3, 3, 3, 3, 3]
    indigoValues = [False, False, False, False, False, False, False]
    finalIndigoValues = [False, False, False, False, False, False]
    violet = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    
    cardinals = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    xtransf = [0, 1, 1, 1, 0, -1, -1, -1]
    ytransf = [-1, -1, 0, 1, 1, 1, 0, -1]
    controlSequence = "["
    tpCommand = ""
    
    # Hello Obvious, if you are reading this, it means that you have access to this github repository. You can now projectile vomit at the scripts I made.
    print("--------------------------------------<START_MODULE>--------------------------------------")
    
    stage = 0
    FinalPhase = False
    logging = ""
    finalBinary = ""
    rotation = 1
    
    otherColouredKugelsPresent = list(input("Input the other Kugelblitz's colours (if any): ").upper())
    if len(otherColouredKugelsPresent) != 0:
            colourString = "ROYGBIV"
            for i in range(0, len(otherColouredKugelsPresent)):
                otherKugels[colourString.index(otherColouredKugelsPresent[i])] = True
    
    while not FinalPhase:
        tempTruthValues = [False, False, False, False, False, False, False]
        stageInfo = ""
        infoValid = False
        if stage != 0:
            print("-------------------------------------<NEW_STAGE>-------------------------------------")
        while not infoValid:
            stageInfo = input("Enter the 7-digit binary shown on stage " + str(stage) + " in ROYGBIV-order, or 'END' if there are no more stages: ").upper()
            if len(stageInfo) == 7 or len(stageInfo) == 3:
                infoValid = True
                print("Information valid, proceeding...")
            else:
                print("Information invalid, enter it again you buffoon.")
        stageLog = ""
        if stageInfo != "END":
            for i in range(0, 7):
                if stageInfo[i] == "1":
                    tempTruthValues[i] = True
                elif stageInfo[i] == "0":
                    tempTruthValues[i] = False
                truthValues[i] ^= tempTruthValues[i]
            for x in truthValues:
                if x:
                    stageLog += "1"
                else:
                    stageLog += "0"
            print("XOR'd binary: " + stageLog)
            if otherKugels[0]:
                redInfo = input("Enter the 7-digit binary shown on the red Kugelblitz on stage " + str(stage) + ": ").upper()
                for i in range(0, len(redInfo)):
                    if redInfo[i] == "1":
                        red[i] = (red[i] + 1) % 7
            if otherKugels[1]:
                orangeInfo = input("Enter the 7-digit binary shown on the orange Kugelblitz on stage " + str(stage) + ": ").upper()
                tempOrangeTruthValues = [False, False, False, False, False, False, False]
                for i in range(0, len(orangeInfo)):
                    if orangeInfo[i] == "1":
                        tempOrangeTruthValues[i] = True
                    orangeValues[i] ^= tempOrangeTruthValues[i]
            if otherKugels[2]:
                yellowInfo = input("Enter the 7-digit binary shown on the yellow Kugelblitz on stage " + str(stage) + ": ").upper()
                tempYellowTruthValues = [False, False, False, False, False, False, False]
                for i in range(0, len(yellowInfo)):
                    if yellowInfo[i] == "1":
                        tempYellowTruthValues[i] = True
                    yellowValues[i] ^= tempYellowTruthValues[i]
            if otherKugels[3]:
                greenInfo = input("Enter the 7-digit binary shown on the green Kugelblitz on stage " + str(stage) + ": ").upper()
                for i in range(0, len(greenInfo)):
                    if greenInfo[i] == "1":
                        green[i] = (green[i] + 1) % 7
            if otherKugels[4]:
                blueInfo = input("Enter the 7-digit binary shown on the blue Kugelblitz on stage " + str(stage) + ": ").upper()
                for i in range(0, len(blueInfo)):
                    if blueInfo[i] == "1":
                        blue[i] = (blue[i] + 1) % 3
            if otherKugels[5]:
                indigoInfo = input("Enter the 7-digit binary shown on the indigo Kugelblitz on stage " + str(stage) + ": ").upper()
                tempIndigoTruthValues = [False, False, False, False, False, False, False]
                for i in range(0, len(indigoInfo)):
                    if indigoInfo[i] == "1":
                        tempIndigoTruthValues[i] = True
                    indigoValues[i] ^= tempIndigoTruthValues[i]
                    finalIndigoValues[0] = indigoValues[0] ^ indigoValues[5]
                    finalIndigoValues[1] = indigoValues[1] ^ indigoValues[5]
                    finalIndigoValues[2] = indigoValues[2] ^ indigoValues[5]
                    finalIndigoValues[3] = indigoValues[3] ^ indigoValues[5]
                    finalIndigoValues[4] = indigoValues[4] ^ indigoValues[5]
                    finalIndigoValues[5] = indigoValues[6] ^ indigoValues[5]
            if otherKugels[6]:
                violetInfo = input("Enter the 7-digit binary shown on the violet Kugelblitz on stage " + str(stage) + ": ").upper()
                for i in range(0, len(violetInfo)):
                    if violetInfo[i] == "1":
                        violet[stage % 2][i] = (violet[stage % 2][i] + 1) % 7
            stage += 1
        else:
            FinalPhase = True
    print("-------------------------------------<FINAL>-------------------------------------")
    if otherKugels[4]:
        finalBlueValues[0] = ((blue[4] + blue[0]) + 2) % 3 + 1
        finalBlueValues[1] = ((blue[4] + blue[1]) + 2) % 3 + 1
        finalBlueValues[2] = ((blue[4] + blue[2]) + 2) % 3 + 1
        finalBlueValues[3] = ((blue[4] + blue[3]) + 2) % 3 + 1
        finalBlueValues[4] = ((blue[4] + blue[5]) + 2) % 3 + 1
        finalBlueValues[5] = ((blue[4] + blue[6]) + 2) % 3 + 1
    for i in range(0, 7):
        logging += ("1" if (truthValues[i]) else "0")
    print("Final bitstring: " + logging)
    pivot[2] = int(input("Enter the number of coloured particles on the module: "))
    truthValues = truthValues[::-1]
    if truthValues[6]:
        rotation *= -1
    for y in range(0, 3):
        if truthValues[y]:
            pivot[1] += 2 ** y
    for x in range(3, 6):
        if truthValues[x]:
            pivot[0] += 2 ** (x - 3)
    print("Position (" + str(pivot[0]) + ", " + str(pivot[1]) + "), [direction] = " + cardinals[pivot[2]])
    for i in range(0, 7):
        print("Starting step " + str(i))
        storedb.append(0)
        for j in range(0, ((green[i] + i) % 7) + 1):
            pivot[2] = (pivot[2] + 16) % 8
            storedb[i] += numberGrid[pivot[1]][pivot[0]] + violet[0][pivot[0]] + violet[1][pivot[1]]
            print("Adding " + str(numberGrid[pivot[1]][pivot[0]]))
            pivot[0] += xtransf[pivot[2]]
            pivot[1] += ytransf[pivot[2]]
            if (not (0 <= pivot[0] and pivot[0] < 7)):
                print("Flipping vertical.")
                pivot[1] = 6 - pivot[1]
                pivot[0] = (pivot[0] + 7) % 7
                rotation = rotation * -1
                pivot[2] = 4 - pivot[2]
            if (not (0 <= pivot[1] and pivot[1] < 7)):
                print("Flipping horizontal.")
                pivot[0] = 6 - pivot[0]
                pivot[1] = (pivot[1] + 7) % 7
                rotation = rotation * -1
                pivot[2] = 0 - pivot[2]
        if i != 6:
            rotation *= (-1 if finalIndigoValues[i] else 1)
            pivot[2] = pivot[2] + (rotation * finalBlueValues[i])
        storedb[i] = (storedb[i] + red[i]) % 7
    log = ""
    for x in storedb:
        log += str(x)
    print("Calculated values are: " + log)
    for x in range(0, 7):
        appendedBinary = ""
        if otherKugels[2]:
            if yellowValues[x]:
                appendedBinary += "1"
            else:
                appendedBinary += "0"
        appendedBinary += binaryStuff[storedb[x]]
        if otherKugels[1]:
            if orangeValues[x]:
                appendedBinary = appendedBinary.replace("0", "-")
                appendedBinary = appendedBinary.replace("1", "0")
                appendedBinary = appendedBinary.replace("-", "1")
        finalBinary += appendedBinary
    print("Number converted to binary is: 1" + finalBinary)
    k = 1
    h = True
    for i in range(0, len(finalBinary)):
        if finalBinary[i] == "1":
            if k >= 3:
                k = 0
                controlSequence += "-"
                if k > -1:
                    k = -1
                else:
                    k += -1
            else:
                if h:
                    controlSequence += "]"
                else:
                    controlSequence += "["
                h = not h
                if k < 1:
                    k = 1
                else:
                    k += 1
        else:
            if k <= -2 or (k <= -1 and not h):
                k = 0
                if h:
                    controlSequence += "]"
                else:
                    controlSequence += "["
                h = not h
                if k < 1:
                    k = 1
                else:
                    k += 1
            else:
                controlSequence += "-"
                if k > -1:
                    k = -1
                else:
                    k += -1
    if h:
        controlSequence += "]--"
    else:
        while (controlSequence[len(controlSequence) - 1] != "-" or controlSequence[len(controlSequence) - 2] != "-"):
            controlSequence += "-"
    controlSequence = controlSequence.replace("]--", "]")
    tpCommand = controlSequence.replace("[", "i")
    tpCommand = tpCommand.replace("]", "i")
    tpCommand = tpCommand.replace("-", "p")
    print("The Input Sequence is: " + controlSequence)
    print("As such, the TP command is: " + tpCommand)
    print("Goodbye, now you probably don't have any more use for me, do you?")
    exit()

if __name__ == "__main__":
    main()