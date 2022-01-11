import math

b36 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
SHAPES = ["--XX--XX--XX--", "XXXX--XXXXXX-X", "-XXXX----XXXX-", "-XXXX---XXXX--", "X-XXX---XXXX-X", "-X-XXXX-XXXX--", "--XXXX---XXX--", "-XXX-XXXX-XXXX", "--XXX----XXX--", "--XXX---XXXX--", "--XXX----XXX-X", "-XX-X-X-XX-X--", "--XXXXXX-XXXX-", "-XX-X-XXXX-X--", "--XXXX---XXXX-", "--XXXX---XXXXX", "--XXXXX--XXX--", "X-XXX----XXX-X", "-XX-XXXXXX-XX-", "XXXXX-XX-XXX--", "X-XX-X-X-XX-XX", "X-XXXXXX-XXXX-", "X--X--XX-XXX-X", "X--XX-XX-XX--X", "--XXX-XX-XXX--", "--XXX----XXXXX", "--XXX-XX-XX---", "--XXX----XX-XX", "--XXXX--XXXX--", "-XX-XXXXXX-XXX", "X-XXX-XX-XXX--", "X-XX-XXX--XXXX", "X-XXX-XX--X--X", "XX-X-XXXX-X-XX", "XX-X-XXXXX-XXX", "-XXX-XXXX-XXX-"]
COLORS = ["K", "B", "G", "C", "R", "M", "Y", "W"]
CHANNELS = [0, 0, 0]
isInverted = [False, False, False]
CURRENT = [0, 0, 0]
HISTORY = []
end = False

def main() -> None:
    global b36
    global SHAPES
    global COLORS
    global CHANNELS
    global isInverted
    global CURRENT
    global HISTORY
    global end
    stage = 0
    initialInfoValid = False
    reverting = False
    
    CHANNELS = [0, 0, 0]
    isInverted = [False, False, False]
    CURRENT = [0, 0, 0]
    HISTORY = []
    end = False
    
    print("----------------------------------<INITIAL_STATES>----------------------------------")
    print("Info: When shadowing or continuing from when the program restarted, it is possible to input the starting value of the part being shadowed and continue as normal.")
    while not initialInfoValid:
        initialValues = input("Input the initial values for each colour channel (RGB-order) separated by spaces: ").upper().split(" ")
        if len(initialValues) == 3:
            initialInfoValid = True
            for x in range(0, 3):
                if len(initialValues[x]) == 2: # Two characters, meaning there must be a negative sign
                    CURRENT[x] = b36.index(initialValues[x][1]) * -1
                elif len(initialValues[x]) == 1: # One character, meaning normal value
                    CURRENT[x] = b36.index(initialValues[x])
                else: # This should never be reached
                    print("This line should not have been reached, exiting")
                    exit()
        else:
            print("The information input was not valid, please try again.")
    print("[R, G, B] = " + str(CURRENT))
    
    ANSWERSHAPES = ["", "", ""]
    ANSWERCHARS = ["", "", ""]
    
    FINALSHAPE = ""
    
    while not end:
        print("-------------------------------------<NEW_STAGE>-------------------------------------")
        displays = input("Enter each channel's displayed value in stage " + str(stage) + " in the same way the initial values were input, adding an extra color at the end for the LED (if there are no more stages, input 'END'): ").upper().split(" ")
        if displays[0].upper() == "STARTOVER":
            print("-------------------------------------<INFO>-------------------------------------")
            print("A full restart of the program has been requested, re-initialising...")
            main()
        elif displays[0].upper() == "REVERT":
            reverting = True
            if len(displays) == 2:
                if int(displays[1]) > len(HISTORY):
                    print("You are trying to access the future, which is not allowed. Fuck you.")
                elif int(displays[1]) == len(HISTORY):
                    print("You are already at the present. Why are you using the revert command to revert to the present?")
                else:
                    print("Reverting to stage " + str(displays[1]) + "...")
                    for y in range(int(displays[1]), len(HISTORY) - 1):
                        HISTORY.pop(len(HISTORY) - 1)
                    CURRENT = [HISTORY[len(HISTORY) - 1][0], HISTORY[len(HISTORY) - 1][1], HISTORY[len(HISTORY) - 1][2]]
                    print("Reverted successfully, values are now: R[R, G, B] = " + str(CURRENT))
                    stage = int(displays[1])
        elif displays[0].upper() == "END":
            print("-------------------------------------<FINAL>-------------------------------------")
            ANSWERSHAPES[0] = SHAPES[abs(CURRENT[0])]
            ANSWERSHAPES[1] = SHAPES[abs(CURRENT[1])]
            ANSWERSHAPES[2] = SHAPES[abs(CURRENT[2])]
            
            ANSWERSHAPES[0] = ANSWERSHAPES[0].replace("-", "R")
            ANSWERSHAPES[0] = ANSWERSHAPES[0].replace("X", "-")
            ANSWERSHAPES[1] = ANSWERSHAPES[1].replace("-", "G")
            ANSWERSHAPES[1] = ANSWERSHAPES[1].replace("X", "-")
            ANSWERSHAPES[2] = ANSWERSHAPES[2].replace("-", "B")
            ANSWERSHAPES[2] = ANSWERSHAPES[2].replace("X", "-")
            
            if CURRENT[0] < 0:
                ANSWERSHAPES[0] = ANSWERSHAPES[0].replace("R", "_")
                ANSWERSHAPES[0] = ANSWERSHAPES[0].replace("-", "R")
                ANSWERSHAPES[0] = ANSWERSHAPES[0].replace("_", "-")
            if CURRENT[1] < 0:
                ANSWERSHAPES[1] = ANSWERSHAPES[1].replace("G", "_")
                ANSWERSHAPES[1] = ANSWERSHAPES[1].replace("-", "G")
                ANSWERSHAPES[1] = ANSWERSHAPES[1].replace("_", "-")
            if CURRENT[2] < 0:
                ANSWERSHAPES[2] = ANSWERSHAPES[2].replace("B", "_")
                ANSWERSHAPES[2] = ANSWERSHAPES[2].replace("-", "B")
                ANSWERSHAPES[2] = ANSWERSHAPES[2].replace("_", "-")
            
            for x in range(0, 3):
                colors = ["R", "G", "B"]
                print(colors[x] + "'s shape: ")
                print("-----<" + ANSWERSHAPES[x][0] + ">-----")
                print(ANSWERSHAPES[x][1] + "  " + ANSWERSHAPES[x][2] + "  " + ANSWERSHAPES[x][3] + "  " + ANSWERSHAPES[x][4] + "  " + ANSWERSHAPES[x][5] + "  ")
                print("--<" + ANSWERSHAPES[x][6] + ">---<" + ANSWERSHAPES[x][7] + ">--")
                print(ANSWERSHAPES[x][8] + "  " + ANSWERSHAPES[x][9] + "  " + ANSWERSHAPES[x][10] + "  " + ANSWERSHAPES[x][11] + "  " + ANSWERSHAPES[x][12] + "  ")
                print("-----<" + ANSWERSHAPES[x][13] + ">-----")
                print("")
            
            for x in range(0, 14):
                temp = ""
                if ANSWERSHAPES[0][x] == "R":
                    temp += "R"
                if ANSWERSHAPES[1][x] == "G":
                    temp += "G"
                if ANSWERSHAPES[2][x] == "B":
                    temp += "B"
                if len(temp) == 0:
                    FINALSHAPE += "K"
                elif len(temp) == 1:
                    FINALSHAPE += temp
                elif len(temp) != 1:
                    if temp == "RG":
                        FINALSHAPE += "Y"
                    elif temp == "RB":
                        FINALSHAPE += "M"
                    elif temp == "GB":
                        FINALSHAPE += "C"
                    elif temp == "RGB":
                        FINALSHAPE += "W"
            print("FinalShpe: ")
            print("-----<" + FINALSHAPE[0] + ">-----")
            print(FINALSHAPE[1] + "  " + FINALSHAPE[2] + "  " + FINALSHAPE[3] + "  " + FINALSHAPE[4] + "  " + FINALSHAPE[5] + "  ")
            print("--<" + FINALSHAPE[6] + ">---<" + FINALSHAPE[7] + ">--")
            print(FINALSHAPE[8] + "  " + FINALSHAPE[9] + "  " + FINALSHAPE[10] + "  " + FINALSHAPE[11] + "  " + FINALSHAPE[12] + "  ")
            print("-----<" + FINALSHAPE[13] + ">-----")
            print("")
            print("Input this sequence of colours into the module and press Submit. The module should now solve. If it doesn't, you know who to contact and scream your lungs out. But it's also on you for using this solver blindly. - L.V.")
            exit()
        elif len(displays) == 2:
            function = displays[1]
            valuesText = ["", "", ""]
            invertedValuesText = ["", "", ""]
            for x in range(0, 14):
                if displays[0][x] in "RMYW":
                    valuesText[0] += "-"
                else:
                    valuesText[0] += "X"
                if displays[0][x] in "GCYW":
                    valuesText[1] += "-"
                else:
                    valuesText[1] += "X"
                if displays[0][x] in "BCMW":
                    valuesText[2] += "-"
                else:
                    valuesText[2] += "X"
            for y in range(0, 14):
                if valuesText[0][y] == "-":
                    invertedValuesText[0] += "X"
                elif valuesText[0][y] == "X":
                    invertedValuesText[0] += "-"
                if valuesText[1][y] == "-":
                    invertedValuesText[1] += "X"
                elif valuesText[1][y] == "X":
                    invertedValuesText[1] += "-"
                if valuesText[2][y] == "-":
                    invertedValuesText[2] += "X"
                elif valuesText[2][y] == "X":
                    invertedValuesText[2] += "-"
            for z in range(0, 3):
                if valuesText[z] in SHAPES:
                    CHANNELS[z] = SHAPES.index(valuesText[z])
                    isInverted[z] = False
                elif invertedValuesText[z] in SHAPES:
                    CHANNELS[z] = SHAPES.index(invertedValuesText[z])
                    isInverted[z] = True
        elif len(displays) == 4:
            function = displays[3]
            for x in range(0, 3):
                if len(displays[x]) == 2: # Two characters, meaning there must be a negative sign
                    CHANNELS[x] = b36.index(displays[x][1])
                    isInverted[x] = True
                elif len(displays[x]) == 1: # One character, meaning normal value
                    CHANNELS[x] = b36.index(displays[x])
                    isInverted[x] = False
                else: # This should never be reached
                    print("This line should not have been reached, exiting")
                    exit()
        else:
            print("The information input were not valid. Starting over.")
            
        if not reverting:
            log = "["
            for x in range(0, 3):
                if isInverted[x] == True:
                    log += "-" + str(CHANNELS[x])
                else:
                    log += str(CHANNELS[x])
                if x != 2:
                    log += ", "
                else:
                    log += "]"
            print("D[R, G, B] = " + log)
            
            if function.upper() == "W":
                for x in range(0, 3):
                    if not isInverted[x]:
                        CURRENT[x] = bound(CURRENT[x] + CHANNELS[x])
                    else:
                        CURRENT[x] = bound(CURRENT[x] - CHANNELS[x])
            elif function.upper() == "R":
                for x in range(0, 3):
                    if not isInverted[x]:
                        CURRENT[x] = bound(CURRENT[x] + 2 * CHANNELS[x])
                    else:
                        CURRENT[x] = bound(CURRENT[x] - 2 * CHANNELS[x])
            elif function.upper() == "G":
                for x in range(0, 3):
                    CURRENT[x] = bound(CURRENT[x] + CHANNELS[x])
            elif function.upper() == "B":
                for x in range(0, 3):
                    if not isInverted[x]:
                        CURRENT[x] = bound(2 * CURRENT[x] + CHANNELS[x])
                    else:
                        CURRENT[x] = bound(2 * CURRENT[x] - CHANNELS[x])
            elif function.upper() == "C":
                for x in range(0, 3):
                    if not isInverted[x]:
                        CURRENT[x] = bound(CURRENT[x] + 2 * CHANNELS[x])
                    else:
                        CURRENT[x] = bound(CURRENT[x] - CHANNELS[x])
            elif function.upper() == "M":
                for x in range(0, 3):
                    CURRENT[x] = bound(CURRENT[x] - CHANNELS[x])
            elif function.upper() == "Y":
                for x in range(0, 3):
                    if not isInverted[x]:
                        CURRENT[x] = bound(CURRENT[x] + CHANNELS[x])
                    else:
                        CURRENT[x] = bound(CURRENT[x] - 2 * CHANNELS[x])
            elif function.upper() == "K":
                for x in range(0, 3):
                    if not isInverted[x]:
                        CURRENT[x] = bound(CURRENT[x] - CHANNELS[x])
                    else:
                        CURRENT[x] = bound(CURRENT[x] + CHANNELS[x])
            else:
                print("Function not valid, displaying current values.")
            print("R[R, G, B] = " + str(CURRENT))
            
            HISTORY.append([CURRENT[0], CURRENT[1], CURRENT[2]])
        stage += 1
        reverting = False
                    
def bound(x: int) -> int:
    """
    Takes the result of a function and takes it modulo 365,
    but if the original number was negative and the result
    of the modulo wasn't zero, subtracts 365 from the result.
    This puts the number between -364 and 364 inclusive.
    :param x: The number to bound
    :return: The bounded number
    """
    y = x % 36  # Begin by taking x modulo 36 where the result is positive.
    if x < 0 < y:  # If x was negative, and y was not 0 (y can't be negative)...
        return int(y - 36)  # Subtract 36 from y, putting it to -35 at the lowest.
    return int(y)  # Otherwise, just return y (if y was 0, this case holds, not the above).

if __name__ == '__main__':
    main()