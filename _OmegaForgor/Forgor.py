import math

b36 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
b64 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]

ledTableIndices = ["A", "K", "B", "C", "G", "J", "L", "M", "O", "R", "S", "V", "W", "Y"]
ledTable = [[37, 18, 7, 58, 24, 72, 95, 1, 54, 73, 88, 13, 64, 83], 
            [66, 48, 50, 19, 41, 22, 84, 78, 90, 34, 3, 63, 29, 14], 
            [95, 23, 57, 98, 36, 75, 81, 42, 4, 32, 7, 91, 60, 11], 
            [47, 86, 73, 0, 16, 46, 97, 59, 26, 81, 77, 39, 65, 92], 
            [70, 24, 53, 30, 27, 6, 85, 44, 69, 38, 76, 49, 62, 99], 
            [28, 63, 14, 52, 90, 15, 2, 87, 29, 71, 45, 51, 94, 37], 
            [8, 33, 61, 20, 22, 34, 11, 89, 65, 12, 67, 4, 78, 91], 
            [40, 82, 98, 25, 95, 10, 56, 69, 44, 79, 96, 9, 40, 31], 
            [47, 3, 66, 93, 35, 85, 43, 91, 18, 55, 78, 14, 5, 60], 
            [74, 95, 21, 68, 2, 26, 90, 42, 17, 13, 80, 75, 99, 53], 
            [32, 17, 56, 74, 91, 58, 70, 92, 85, 30, 64, 72, 89, 13], 
            [41, 93, 35, 88, 11, 1, 23, 65, 49, 0, 43, 63, 87, 12], 
            [34, 71, 50, 6, 39, 27, 33, 92, 3, 52, 77, 77, 49, 10], 
            [47, 18, 94, 83, 62, 14, 86, 9, 54, 17, 89, 24, 16, 8]]

rotations = ["XY", "XZ", "YZ", "YX", "ZX", "ZY"]
stageVars = ["j", "k", "l", "m", "n"]

finalColours = ["K", "B", "C", "G", "M", "O", "P", "R", "W", "Y"]
finalValueTable = [["43", "88", "59", "25", "46", "07", "91", "70", "63", "14"], 
                   ["31", "52", "00", "94", "38", "11", "27", "62", "77", "83"], 
                   ["86", "35", "19", "16", "32", "55", "74", "80", "04", "67"], 
                   ["61", "97", "72", "99", "58", "47", "18", "30", "78", "51"], 
                   ["02", "15", "41", "40", "82", "33", "65", "60", "44", "08"], 
                   ["17", "68", "57", "28", "22", "93", "23", "24", "03", "10"], 
                   ["79", "26", "64", "42", "73", "39", "50", "20", "87", "56"], 
                   ["49", "76", "01", "53", "48", "37", "92", "06", "69", "29"], 
                   ["21", "36", "84", "75", "34", "71", "54", "85", "89", "45"], 
                   ["98", "96", "05", "90", "66", "95", "12", "13", "81", "09"]]
stageCalculations = [0, 0, 0, 0, 0]
TrueOmegaForgetValues = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
allInputs = []
TrueOmegaForget = False

def main() -> None:
    global b36
    global b64
    global ledTableIndices
    global ledTable
    global rotations
    global finalColours
    global stageCalculations
    global allInputs
    global TrueOmegaForget
    
    TrueOmegaForget = (True if input("I regret to have to ask this, but are you doing TrueOmegaForget? (Y/N): ").upper() == "Y" else False)
    stage = 0
    
    if not TrueOmegaForget:
        print("Command Format: '<Display> <LeftColour><RightColour> <Rotation>'")
    elif TrueOmegaForget:
        print("Command Format: '<Display> <LeftColour><RightColour> <Rotation1> <Rotation2> <Rotation3>'")
    print("---------------------------------<PREPARATIONS>----------------------------------")
    buttonColours = list(input("Input the module's button's colour sequence: ").upper())
    finalColours = order(finalColours, buttonColours)
    while True:
        print("-----------------------------------<NEW_STAGE>-----------------------------------")
        stageInfo = input("Input the display, the two LED colours, and the cube rotation in stage " + str(stage) + " in one command (or 'END' if there are no more stages): ").upper().split(" ")
        infoValid = infoValidator(stageInfo)
        while not infoValid:
            stageInfo = input("Input the display, the two LED colours, and the cube rotation in one command: ").upper().split(" ")
            infoValid = infoValidator(stageInfo)
        displayBase10 = b36.index(stageInfo[0][0]) * 36 + b36.index(stageInfo[0][1])
        I = bound(int(oct(displayBase10).replace("0o", "")))
        print("Display in octal (I) = " + str(I))
        C = bound(ledTable[ledTableIndices.index(stageInfo[1][1])][ledTableIndices.index(stageInfo[1][0])])
        print("Initial LED value (C) = " + str(C))
        E = 0
        if stage % 5 == 0:
            E = (I - C) % 100
        elif stage % 5 == 1:
            E = (2*C + 7) % 100
        elif stage % 5 == 2:
            E = (math.floor(((C + (C % 2)) + (I + (I % 2))) / 2)) % 100
        elif stage % 5 == 3:
            E = (3*I - 2*C - 42) % 100
        elif stage % 5 == 4:
            E = (75 - C + 2*I) % 100
        print("Final LED value (E) = " + str(E))
        D = bound(b64.index(stageInfo[0][0]) * 64 + b64.index(stageInfo[0][1]))
        print("Display from b64 to decimal = " + str(D))
        tableLookup = ""
        if not TrueOmegaForget:
            if stage % 5 == 0:
                if stageInfo[2] == "XY":
                    stageCalculations[stage % 5] = bound(I + 2 * E)
                elif stageInfo[2] == "XZ":
                    stageCalculations[stage % 5] = bound(2 * I + E)
                elif stageInfo[2] == "YZ":
                    stageCalculations[stage % 5] = bound(999 - 2 * I)
                elif stageInfo[2] == "YX":
                    stageCalculations[stage % 5] = bound(I - (99 - E))
                elif stageInfo[2] == "ZX":
                    stageCalculations[stage % 5] = bound(E - I)
                elif stageInfo[2] == "ZY":
                    stageCalculations[stage % 5] = bound(math.floor((I - (I % 2)) / 2) + D)
            elif stage % 5 == 1:
                if stageInfo[2] == "XY":
                    stageCalculations[stage % 5] = bound(stageCalculations[0] + D - I)
                elif stageInfo[2] == "XZ":
                    stageCalculations[stage % 5] = bound(I - stageCalculations[0] + D)
                elif stageInfo[2] == "YZ":
                    stageCalculations[stage % 5] = bound(stageCalculations[0] - I)
                elif stageInfo[2] == "YX":
                    stageCalculations[stage % 5] = bound(E + D + I - stageCalculations[0])
                elif stageInfo[2] == "ZX":
                    stageCalculations[stage % 5] = bound(999 - I - stageCalculations[0])
                elif stageInfo[2] == "ZY":
                    stageCalculations[stage % 5] = bound(2 * D - I + stageCalculations[0])
            elif stage % 5 == 2:
                if stageInfo[2] == "XY":
                    stageCalculations[stage % 5] = bound(I + stageCalculations[0] + stageCalculations[1])
                elif stageInfo[2] == "XZ":
                    stageCalculations[stage % 5] = bound(I - stageCalculations[1])
                elif stageInfo[2] == "YZ":
                    stageCalculations[stage % 5] = bound(stageCalculations[0] + stageCalculations[1] - I)
                elif stageInfo[2] == "YX":
                    stageCalculations[stage % 5] = bound(I * ((stageCalculations[0] % 6) + 1))
                elif stageInfo[2] == "ZX":
                    stageCalculations[stage % 5] = bound(D - (I + E) + stageCalculations[1])
                elif stageInfo[2] == "ZY":
                    stageCalculations[stage % 5] = bound(3 * D - stageCalculations[1] + I)
            elif stage % 5 == 3:
                if stageInfo[2] == "XY":
                    stageCalculations[stage % 5] = bound(stageCalculations[2] - stageCalculations[1] - stageCalculations[0] + I)
                elif stageInfo[2] == "XZ":
                    stageCalculations[stage % 5] = bound((3 * I) - (4 * D))
                elif stageInfo[2] == "YZ":
                    stageCalculations[stage % 5] = bound(I + E - D)
                elif stageInfo[2] == "YX":
                    stageCalculations[stage % 5] = bound(stageCalculations[2] - I * ((I % 4) + 1))
                elif stageInfo[2] == "ZX":
                    stageCalculations[stage % 5] = bound(stageCalculations[1] + math.floor((I + (I % 2))/2))
                elif stageInfo[2] == "ZY":
                    stageCalculations[stage % 5] = bound(0 - stageCalculations[2] - I + D)
            elif stage % 5 == 4:
                if stageInfo[2] == "XY":
                    stageCalculations[stage % 5] = bound(I - stageCalculations[3] + stageCalculations[2] - stageCalculations[1] + stageCalculations[0])
                elif stageInfo[2] == "XZ":
                    stageCalculations[stage % 5] = bound(999 - (4 * I) + stageCalculations[3])
                elif stageInfo[2] == "YZ":
                    stageCalculations[stage % 5] = bound(333 - stageCalculations[2] + I - E)
                elif stageInfo[2] == "YX":
                    stageCalculations[stage % 5] = bound(stageCalculations[0] + 15 - math.floor((I - (I % 2))/2))
                elif stageInfo[2] == "ZX":
                    stageCalculations[stage % 5] = bound(I + stageCalculations[1] - stageCalculations[3])
                elif stageInfo[2] == "ZY":
                    stageCalculations[stage % 5] = bound((5 * I) - stageCalculations[2] + (3 * D) - E)
            print("Stage Calculation (" + stageVars[stage % 5] + ") = " + str(stageCalculations[stage % 5]))
            tableLookup = str(stageCalculations[stage % 5] % 100)
        elif TrueOmegaForget:
            TrueOmegaForgetValues[stage % 5][0] = I
            X = 0
            for n in range(0, 3):
                if n == 0:
                    X = I
                else:
                    X = TrueOmegaForgetValues[stage % 5][n - 1]
                if stage % 5 == 0:
                    if stageInfo[n + 2] == "XY":
                        TrueOmegaForgetValues[stage % 5][n] = bound(X + (2 * E))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "XZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(X + I + E)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(999 - (2 * X))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(I - (99 - E) + X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(E - X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZY":
                        TrueOmegaForgetValues[stage % 5][n] = bound(math.floor((X - (X % 2)) / 2) + D)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                elif stage % 5 == 1:
                    if stageInfo[n + 2] == "XY":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[0][n] + D - X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "XZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(X - I - TrueOmegaForgetValues[0][n])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[0][2] - X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(E + D + X - TrueOmegaForgetValues[0][1])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(999 - X - TrueOmegaForgetValues[0][0])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZY":
                        TrueOmegaForgetValues[stage % 5][n] = bound((2 * D) - X + TrueOmegaForgetValues[0][n])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                elif stage % 5 == 2:
                    if stageInfo[n + 2] == "XY":
                        TrueOmegaForgetValues[stage % 5][n] = bound(X + TrueOmegaForgetValues[0][n] + TrueOmegaForgetValues[1][n])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "XZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound((n + 1) * X - TrueOmegaForgetValues[1][0])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[0][2] + TrueOmegaForgetValues[1][2] - X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(X * ((TrueOmegaForgetValues[0][n] % 6) + 1))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(D - (X + E) + TrueOmegaForgetValues[1][0])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZY":
                        TrueOmegaForgetValues[stage % 5][n] = bound((3 * D) - TrueOmegaForgetValues[1][n] + X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                elif stage % 5 == 3:
                    if stageInfo[n + 2] == "XY":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[2][n] - TrueOmegaForgetValues[1][n] - TrueOmegaForgetValues[0][n] + X)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "XZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound((3 * X) - (4 * D) + (5 * (n + 1)))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound((n + 1) * (X + E - D))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[2][1] - (X * ((I % 4) + 1)))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[1][n] + math.floor((X + (X % 2)) / 2))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZY":
                        TrueOmegaForgetValues[stage % 5][n] = bound((n + 1) - TrueOmegaForgetValues[2][2] - X + D)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                elif stage % 5 == 4:
                    if stageInfo[n + 2] == "XY":
                        TrueOmegaForgetValues[stage % 5][n] = bound(X - TrueOmegaForgetValues[3][n] + TrueOmegaForgetValues[2][n] - TrueOmegaForgetValues[1][n] + TrueOmegaForgetValues[0][n])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "XZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(999 - (4 * X) - (9 * (n + 1)) + TrueOmegaForgetValues[3][2])
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YZ":
                        TrueOmegaForgetValues[stage % 5][n] = bound(333 - TrueOmegaForgetValues[2][1] + X - E)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "YX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(TrueOmegaForgetValues[0][2] + (15 * (n + 1)) - math.floor((X - (X % 2)) / 2))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZX":
                        TrueOmegaForgetValues[stage % 5][n] = bound(I - (2 * (n + 1)) - TrueOmegaForgetValues[1][0] + (X - (5 * (n + 1))))
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
                    elif stageInfo[n + 2] == "ZY":
                        TrueOmegaForgetValues[stage % 5][n] = bound((5 * X) - (10 * (n + 1)) + (3 * D) - E)
                        print("Step #" + str(n) + "'s result: " + str(TrueOmegaForgetValues[stage % 5][n]))
            print("Stage Calculation (" + stageVars[stage % 5] + ") = " + str(TrueOmegaForgetValues[stage % 5]))
            tableLookup = str(TrueOmegaForgetValues[stage % 5][2] % 100)
        if len(tableLookup) < 2:
            tableLookup = "0" + tableLookup
        finalTableValue = finalValueTable[int(tableLookup[1])][int(tableLookup[0])]
        print("Final Value (from table) = " + finalTableValue)
        stageInput = list(finalTableValue)
        stageInput[0] = finalColours[int(stageInput[0])]
        press = stageInput[0] + stageInput[1]
        print("Decided Final Action = " + press)
        allInputs.append(press)
        stage += 1

def order(finalColours: list, buttonColours: list):
    if (buttonColours.index("W") + 1) % 10 == buttonColours.index("K") or (buttonColours.index("K") + 1) % 10 == buttonColours.index("W"): # If (W)hite and Blac(k) are adjacent, reverse the sequence
        finalColours.reverse()
        print("Rule #1 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("R") + 5) % 10 == buttonColours.index("C"): # If Red opposite Cyan, swap them in final sequence
        swap(finalColours, "R", "C")
        print("Rule #2 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("G") + 5) % 10 == buttonColours.index("M"): # If Red opposite Cyan, swap them in final sequence
        swap(finalColours, "G", "M")
        print("Rule #3 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("B") + 5) % 10 == buttonColours.index("Y"): # If Red opposite Cyan, swap them in final sequence
        swap(finalColours, "B", "Y")
        print("Rule #4 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("O") + 2) % 10 == buttonColours.index("P") or (buttonColours.index("P") + 2) % 10 == buttonColours.index("O"): # If exactly one button separates (O)range and (P)urple, swap 1st and 10th
        swap(finalColours, buttonColours[0], buttonColours[9])
        print("Rule #5 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("R") + 1) % 10 == buttonColours.index("B") or (buttonColours.index("B") + 1) % 10 == buttonColours.index("R"): # If (R)ed and (B)lue are adjacent, cycle sequence twice right
        finalColours[:] = finalColours[8:] + finalColours[:8]
        print("Rule #6 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("W") + 3) % 10 == buttonColours.index("K") or (buttonColours.index("K") + 3) % 10 == buttonColours.index("W"): # If exactly two buttons separate (W)hite and Blac(k), swap 2nd and 9th
        swap(finalColours, buttonColours[1], buttonColours[8])
        print("Rule #7 applies, final sequence: " + str(finalColours))
    if (buttonColours.index("G") + 1) % 10 == buttonColours.index("Y") or (buttonColours.index("Y") + 1) % 10 == buttonColours.index("G"): # If (Y)ellow and (G)reen are adjacent, cycle three left
        finalColours[:] = finalColours[3:] + finalColours[:3]
        print("Rule #8 applies, final sequence: " + str(finalColours))
    print("Final Sequence: " + str(finalColours))
    return finalColours

def swap(l: list, a: str, b: str) -> None:
    """A method for swapping two strings in a list (uses below method)."""
    swap_int(l, l.index(a), l.index(b))  # Gets indexes and passes to swap_int

def swap_int(l: list, a: int, b: int) -> None:
    """A method for swapping two strings in a list by using their indexes."""
    l[a], l[b] = l[b], l[a]  # Note: these small functions help reduce code size

def infoValidator(stageInfo: list) -> bool:
    if stageInfo[0] == "END":
        print("----------------------------------<FINAL_PHASE>----------------------------------")
        string = ""
        tpCommand = ""
        for x in range(0, len(allInputs)):
            string += allInputs[x]
            tpCommand += allInputs[x]
            if x != len(allInputs) - 1:
                string += ", "
                tpCommand += " "
        print("All stages' button presses are: " + string)
        print("As such, the Toiler Paper command is: " + tpCommand)
        print("That is all, goodbye. - L.V.")
        exit()
    if len(stageInfo) != 3 and not TrueOmegaForget:
        print("Expected three parameters. Try again.")
        return False
    elif len(stageInfo) != 5 and TrueOmegaForget:
        print("Expected five parameters. Try again.")
        return False
    if len(stageInfo[0]) != 2:
        print("Expected base36 number of length 2. Try again.")
        return False
    if stageInfo[0][0] not in b36 or stageInfo[0][1] not in b36:
        print("Invalid character detected. Try again.")
        return False
    if len(stageInfo[1]) != 2:
        print("Expected two LED colours. Try again.")
        return False
    if stageInfo[1][0] not in ledTableIndices or stageInfo[1][1] not in ledTableIndices:
        print("Invalid LED colour detected. Try again.")
        return False
    if stageInfo[2] not in rotations:
        print("Invalid rotation detected. Try again.")
        return False
    return True

def bound(x: int) -> int:
    y = x % 1000  # Begin by taking x modulo 1000 where the result is positive.
    if x < 0 and y != 0:  # If x was negative, and y was not 0 (y can't be negative)...
        return int(y - 1000)  # Subtract 1000 from y, putting it to -999 at the lowest.
    return int(y)  # Otherwise, just return y (if y was 0, this case holds, not the above).

if __name__ == "__main__":
    main()