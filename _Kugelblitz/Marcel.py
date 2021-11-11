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
pivot = [0, 0, 0]
binaryStuff = ["000", "001", "010", "011", "100", "101", "110"]
storedb = []

def main() -> None:
    global numberGrid
    global truthValues
    global pivot
    global storedb
    
    cardinals = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    xtransf = [0, 1, 1, 1, 0, -1, -1, -1]
    ytransf = [-1, -1, 0, 1, 1, 1, 0, -1]
    controlSequence = "["
    tpCommand = ""
    
    print("--------------------------------------<START_MODULE>--------------------------------------")
    
    stage = 0
    FinalPhase = False
    logging = ""
    finalBinary = ""
    rotation = 1
    
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
                if x == True:
                    stageLog += "1"
                elif x == False:
                    stageLog += "0"
            print("XOR'd binary: " + stageLog)
            stage += 1
        else:
            FinalPhase = True
    print("-------------------------------------<FINAL>-------------------------------------")
    for i in range(0, 7):
        logging += ("1" if (truthValues[i] == True) else "0")
    print("Final bitstring: " + logging)
    pivot[2] = int(input("Enter the number of coloured particles on the module: "))
    truthValues = truthValues[::-1]
    if truthValues[6] == True:
        rotation *= -1
    for y in range(0, 3):
        if truthValues[y] == True:
            pivot[1] += 2 ** y
    for x in range(3, 6):
        if truthValues[x] == True:
            pivot[0] += 2 ** (x - 3)
    print("Position (" + str(pivot[0]) + ", " + str(pivot[1]) + "), [direction] = " + cardinals[pivot[2]])
    for i in range(0, 7):
        print("Starting step " + str(i))
        storedb.append(0)
        for j in range(0, i + 1):
            pivot[2] = (pivot[2] + 16) % 8
            storedb[i] += numberGrid[pivot[1]][pivot[0]]
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
        pivot[2] = pivot[2] + (rotation * 3)
        storedb[i] %= 7
    log = ""
    for x in storedb:
        log += str(x)
    print("Calculated values are: " + log)
    for x in range(0, 7):
        finalBinary += binaryStuff[storedb[x]]
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
        

if __name__ == "__main__":
    main()