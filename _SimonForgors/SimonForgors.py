import math

# ROYGCBPMIW
Stage5Values = [-4, -1, 3, -2, -5, 4, -3, 1, 5, 2]
LEDs = [False, False, False, False, False, False, False, False, False, False]
Final = ""
indicators = ""
serialPortCount = 0
serialNumber = ""
CalculatedSequences = []
batteryCount = 0
batteryHolderCount = 0
Colours = ["R", "O", "Y", "G", "C", "B", "P", "M", "I", "W"]

# Stage10Table[Color][Color]
Stage10Table = [[9, 2, 0, -1, -5, 1, 2, -2, 4, -4],
                [2, 9, 1, 4, 0, -1, -2, 2, -3, 5],
                [0, 1, 9, -1, -1, 1, -5, 4, 2, -3],
                [-1, 4, -1, 9, 3, 5, 6, -4, 0, 2],
                [-5, 0, -1, 3, 9, 0, 4, 1, -5, 2],
                [1, -1, 1, 5, 0, 9, 3, 1, -2, 1],
                [2, -2, -5, 6, 4, 3, 9, -1, 2, -3],
                [-2, 2, 4, -4, 1, 1, -1, 9, 0, 3],
                [4, -3, 2, 0, -5, -2, 2, 0, 9, 1],
                [-4, 5, -3, 2, 2, 1, -3, 3, 1, 9]]

def main() -> None:
    global LEDs
    global Final
    global indicators
    global serialPortCount
    global serialNumber
    global CalculatedSequences
    global batteryCount
    global batteryHolderCount
    global Stage5Values
    global Stage10Table
    global Colours
    
    stage = 1
    
    print("----------------------------------------<START_PHASE>----------------------------------------")
    print("Simon kinda forgor his colours, so you probably want to help him.")
    print("Command Format: <LitLEDs> <ButtonLayout> <Flashes>")
    moduleCount = int(input("How many modules are on this bomb? "))
    serialNumber = input("What's the bomb's Serial Number? ").upper()
    indicators = input("Input the indicators present on this bomb, following the format '<name>_' if unlit, and '<name>*' if lit (if there are none, just press enter): ").upper()
    serialPortCount = int(input("How many serial ports are on the bomb? "))
    batteryCount = int(input("How many batteries are on the bomb? "))
    batteryHolderCount = int(input("How many battery holders are on the bomb? "))
    firstDigit = 0
    
    if serialNumber[0] in "0123456789":
        firstDigit = int(serialNumber[0])
    elif serialNumber[1] in "0123456789":
        firstDigit = int(serialNumber[1])
    else:
        firstDigit = int(serialNumber[2])
    
    while True:
        print("-----------------------------------------<NEW_STAGE>-----------------------------------------")
        tempAns = ""
        infoDump = input("Input the information shown on the module in stage " + str(stage) + " (or 'END' if there are no more stages): ").upper().split(" ")
        infoValid = infoValidator(infoDump)
        while not infoValid:
            infoDump = input("Input the information shown on the module in stage " + str(stage) + " (or 'END' if there are no more stages): ").upper().split(" ")
            infoValid = infoValidator(infoDump)
        
        # Module Info
        LitLEDs = list(infoDump[0])
        ButtonLayout = list(infoDump[1])
        Flashes = list(infoDump[2])
        
        # Setting up the lit LED array
        for i in range(0, len(LitLEDs)):
            LEDs[Colours.index(LitLEDs[i])] = True
        
        # Section 1: Stage Sequence
        for i in range(0, len(Flashes)):
            if Flashes[i] == "R":
                if ButtonLayout.index("O") < 5:
                    if LEDs[Colours.index("Y")] == True:
                        if stage % 2 == 0:
                            tempAns += "R"
                        else:
                            tempAns += "W"
                    else:
                        if stage % 2 == 1:
                            tempAns += "C"
                        else:
                            tempAns += "O"
                else:
                    if LEDs[Colours.index("W")] == True:
                        if moduleCount % 2 == 1:
                            tempAns += "B"
                        else:
                            tempAns += "M"
                    else:
                        if moduleCount % 2 == 1:
                            tempAns += "G"
                        else:
                            tempAns += "I"
            elif Flashes[i] == "O":
                if LEDs[Colours.index("B")] == False:
                    if ButtonLayout.index("G") > 4:
                        if int(serialNumber[5]) % 2 == 0:
                            tempAns += "P"
                        else:
                            tempAns += "Y"
                    else:
                        if int(serialNumber[5]) % 2 == 1:
                            tempAns += "B"
                        else:
                            tempAns += "P"
                else:
                    if ButtonLayout.index("P") < 5:
                        if stage % 2 == 0:
                            tempAns += "W"
                        else:
                            tempAns += "R"
                    else:
                        if stage % 2 == 1:
                            tempAns += "G"
                        else:
                            tempAns += "C"
            elif Flashes[i] == "Y":
                if ButtonLayout.index("W") < 5:
                    if LEDs[Colours.index("G")] == True:
                        if stage % 2 == 0:
                            tempAns += "B"
                        else:
                            tempAns += "G"
                    else:
                        if stage % 2 == 1:
                            tempAns += "O"
                        else:
                            tempAns += "I"
                else:
                    if LEDs[Colours.index("P")] == True:
                        if moduleCount % 2 == 1:
                            tempAns += "W"
                        else:
                            tempAns += "Y"
                    else:
                        if moduleCount % 2 == 1:
                            tempAns += "R"
                        else:
                            tempAns += "M"
            elif Flashes[i] == "G":
                if LEDs[Colours.index("C")] == False:
                    if ButtonLayout.index("R") > 4:
                        if int(serialNumber[5]) % 2 == 0:
                            tempAns += "C"
                        else:
                            tempAns += "P"
                    else:
                        if int(serialNumber[5]) % 2 == 1:
                            tempAns += "B"
                        else:
                            tempAns += "I"
                else:
                    if ButtonLayout.index("Y") < 5:
                        if stage % 2 == 0:
                            tempAns += "W"
                        else:
                            tempAns += "R"
                    else:
                        if stage % 2 == 1:
                            tempAns += "G"
                        else:
                            tempAns += "M"
            elif Flashes[i] == "C":
                if ButtonLayout.index("R") < 5:
                    if LEDs[Colours.index("I")] == True:
                        if stage % 2 == 0:
                            tempAns += "O"
                        else:
                            tempAns += "I"
                    else:
                        if stage % 2 == 1:
                            tempAns += "Y"
                        else:
                            tempAns += "G"
                else:
                    if LEDs[Colours.index("B")] == True:
                        if moduleCount % 2 == 1:
                            tempAns += "B"
                        else:
                            tempAns += "W"
                    else:
                        if moduleCount % 2 == 1:
                            tempAns += "M"
                        else:
                            tempAns += "I"
            elif Flashes[i] == "B":
                if LEDs[Colours.index("G")] == False:
                    if ButtonLayout.index("C") > 4:
                        if int(serialNumber[5]) % 2 == 0:
                            tempAns += "B"
                        else:
                            tempAns += "R"
                    else:
                        if int(serialNumber[5]) % 2 == 1:
                            tempAns += "O"
                        else:
                            tempAns += "Y"
                else:
                    if ButtonLayout.index("W") < 5:
                        if stage % 2 == 0:
                            tempAns += "C"
                        else:
                            tempAns += "G"
                    else:
                        if stage % 2 == 1:
                            tempAns += "W"
                        else:
                            tempAns += "O"
            elif Flashes[i] == "P":
                if ButtonLayout.index("G") < 5:
                    if LEDs[Colours.index("Y")] == True:
                        if stage % 2 == 0:
                            tempAns += "R"
                        else:
                            tempAns += "M"
                    else:
                        if stage % 2 == 1:
                            tempAns += "P"
                        else:
                            tempAns += "B"
                else:
                    if LEDs[Colours.index("M")] == True:
                        if moduleCount % 2 == 1:
                            tempAns += "G"
                        else:
                            tempAns += "O"
                    else:
                        if moduleCount % 2 == 1:
                            tempAns += "I"
                        else:
                            tempAns += "W"
            elif Flashes[i] == "M":
                if LEDs[Colours.index("W")] == False:
                    if ButtonLayout.index("G") > 4:
                        if int(serialNumber[5]) % 2 == 0:
                            tempAns += "Y"
                        else:
                            tempAns += "R"
                    else:
                        if int(serialNumber[5]) % 2 == 1:
                            tempAns += "M"
                        else:
                            tempAns += "C"
                else:
                    if ButtonLayout.index("P") < 5:
                        if stage % 2 == 0:
                            tempAns += "P"
                        else:
                            tempAns += "B"
                    else:
                        if stage % 2 == 1:
                            tempAns += "I"
                        else:
                            tempAns += "W"
            elif Flashes[i] == "I":
                if ButtonLayout.index("B") < 5:
                    if LEDs[Colours.index("R")] == True:
                        if stage % 2 == 0:
                            tempAns += "G"
                        else:
                            tempAns += "M"
                    else:
                        if stage % 2 == 1:
                            tempAns += "R"
                        else:
                            tempAns += "W"
                else:
                    if LEDs[Colours.index("B")] == True:
                        if moduleCount % 2 == 1:
                            tempAns += "O"
                        else:
                            tempAns += "I"
                    else:
                        if moduleCount % 2 == 1:
                            tempAns += "B"
                        else:
                            tempAns += "G"
            elif Flashes[i] == "W":
                if LEDs[Colours.index("I")] == False:
                    if ButtonLayout.index("C") > 4:
                        if int(serialNumber[5]) % 2 == 0:
                            tempAns += "C"
                        else:
                            tempAns += "Y"
                    else:
                        if int(serialNumber[5]) % 2 == 1:
                            tempAns += "W"
                        else:
                            tempAns += "R"
                else:
                    if ButtonLayout.index("Y") < 5:
                        if stage % 2 == 0:
                            tempAns += "P"
                        else:
                            tempAns += "B"
                    else:
                        if stage % 2 == 1:
                            tempAns += "I"
                        else:
                            tempAns += "Y"
        print("Stage Sequence: " + tempAns)
        TPCommand = ""
        for i in range(0, len(tempAns)):
            TPCommand += str(ButtonLayout.index(tempAns[i]) + 1)
            if i != len(tempAns) - 1:
                TPCommand += " "
        print("As such, the TP Command is: " + TPCommand)
        calculatedSequence = stageCalculation(stage, stage, ButtonLayout, tempAns)
        print("Calculated Sequence for this stage is: " + calculatedSequence)
        CalculatedSequences.append(calculatedSequence)
        for i in range(0, len(calculatedSequence)):
            Final += calculatedSequence[i]
        for i in range(0, len(LEDs)):
            LEDs[i] = False
        stage += 1

def stageCalculation(rule: int, stage: int, ButtonLayout: list, tempAns: str) -> str:
    finalAns = ""
    if rule == 1:
        if len(indicators) == 0:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 5) % 10]
        elif ("CAR_" in indicators) and ("FRK*" in indicators):
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 2) % 10]
        elif ("CAR*" in indicators) or ("FRK_" in indicators):
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 4) % 10]
        elif "*" not in indicators:
            count = 0
            for char in indicators:
                if char == "_":
                    count += 1
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + count) % 10]
        else:
            count = 0
            for char in indicators:
                if char == "*":
                    count += 1
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - count) % 10]
    elif rule == 2:
        if serialPortCount > 1 and ("A" in serialNumber or "E" in serialNumber or "I" in serialNumber or "O" in serialNumber or "U" in serialNumber or "Y" in serialNumber):
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 3) % 10]
        elif serialPortCount != 0:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 6) % 10]
        elif "R" not in CalculatedSequences[stage - 2]:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("R") + 1)) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + int(serialNumber[5])) % 10]
    elif rule == 3:
        if batteryHolderCount > 3:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (batteryCount + 2)) % 10]
        elif batteryCount > 3:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + (batteryHolderCount + 1)) % 10]
        elif "B" not in CalculatedSequences[stage - 2]:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("B") + 1)) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + batteryCount) % 10]
    elif rule == 4:
        if LEDs[Colours.index("R")] == True and LEDs[Colours.index("G")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + (ButtonLayout.index("W") + 1)) % 10]
        elif LEDs[Colours.index("R")] == False and LEDs[Colours.index("G")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 1) % 10]
        elif LEDs[Colours.index("R")] == True and LEDs[Colours.index("G")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 2) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 1) % 10]
    elif rule == 5:
        shift = 0
        for i in range(0, len(LEDs)):
            if LEDs[i]:
                shift += Stage5Values[i]
        if int(serialNumber[5]) % 2 == 0:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + shift) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - shift) % 10]
    elif rule == 6:
        if LEDs[Colours.index("W")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 2) % 10]
        elif LEDs[Colours.index("R")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 3) % 10]
        elif LEDs[Colours.index("B")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 4) % 10]
        elif LEDs[Colours.index("G")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 1) % 10]
        elif LEDs[Colours.index("I")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 1) % 10]
        elif LEDs[Colours.index("Y")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 2) % 10]
        elif LEDs[Colours.index("C")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 4) % 10]
        elif LEDs[Colours.index("O")] == False:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 3) % 10]
        else:
            finalAns = tempAns
    elif rule == 7:
        if "R" in CalculatedSequences[stage - 2]:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 1) % 10]
        elif "Y" in CalculatedSequences[stage - 2]:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 3) % 10]
        elif "G" in CalculatedSequences[stage - 2]:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 2) % 10]
        elif "B" in CalculatedSequences[stage - 2]:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 1) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 3) % 10]
    elif rule == 8:
        if LEDs[Colours.index("O")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - int(serialNumber[5])) % 10]
        elif LEDs[Colours.index("I")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + stage) % 10]
        elif LEDs[Colours.index("G")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - batteryCount) % 10]
        elif LEDs[Colours.index("P")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + firstDigit) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 4) % 10]
    elif rule == 9:
        count = [0, 0, 0, 0]
        for char in serialNumber:
            if char in "STEINWAY":
                count[0] += 1
            if char in "INTIMATE":
                count[1] += 1
            if char in "ORIENTAL":
                count[2] += 1
            if char in "TACHYCARDIA":
                count[3] += 1
        if count[0] >= 2:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 4) % 10]
        elif count[1] >= 2:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 2) % 10]
        elif count[2] >= 2:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 3) % 10]
        elif count[3] >= 2:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - 7) % 10]
        else:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 2) % 10]
    elif rule == 10:
        LEDIndices = []
        for i in range(0, len(LEDs)):
            if LEDs[i]:
                LEDIndices.append(i)
        if len(LEDIndices) != 2:
            print("Something is wrong, exiting.")
        else:
            if "A" in serialNumber or "E" in serialNumber or "I" in serialNumber or "O" in serialNumber or "U" in serialNumber or "Y" in serialNumber:
                for ans in tempAns:
                    finalAns += ButtonLayout[(ButtonLayout.index(ans) + Stage10Table[LEDIndices[0]][LEDIndices[1]]) % 10]
            else:
                for ans in tempAns:
                    finalAns += ButtonLayout[(ButtonLayout.index(ans) - Stage10Table[LEDIndices[0]][LEDIndices[1]]) % 10]
    elif rule == 11:
        if LEDs[Colours.index("W")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + (ButtonLayout.index("W") + 1)) % 10]
        elif LEDs[Colours.index("O")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("R") + 1)) % 10]
        elif LEDs[Colours.index("Y")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("I") + 1)) % 10]
        elif LEDs[Colours.index("G")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + (ButtonLayout.index("P") + 1)) % 10]
        elif LEDs[Colours.index("I")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("R") + 1)) % 10]
        elif LEDs[Colours.index("C")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("O") + 1)) % 10]
        elif LEDs[Colours.index("P")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("C") + 1)) % 10]
        elif LEDs[Colours.index("M")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("B") + 1)) % 10]
        elif LEDs[Colours.index("B")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("Y") + 1)) % 10]
        elif LEDs[Colours.index("R")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) - (ButtonLayout.index("M") + 1)) % 10]
        else:
            finalAns = tempAns
    else:
        if LEDs[Colours.index("W")] == True:
            for ans in tempAns:
                finalAns += ButtonLayout[(ButtonLayout.index(ans) + 3) % 10]
        elif LEDs[Colours.index("Y")] == True:
            finalAns = stageCalculation(11, stage, ButtonLayout, tempAns)
        elif LEDs[Colours.index("I")] == True:
            finalAns = stageCalculation(8, stage, ButtonLayout, tempAns)
        elif LEDs[Colours.index("M")] == True:
            finalAns = stageCalculation(6, stage, ButtonLayout, tempAns)
        elif LEDs[Colours.index("R")] == True:
            finalAns = stageCalculation(5, stage, ButtonLayout, tempAns)
        elif LEDs[Colours.index("B")] == True:
            finalAns = stageCalculation(7, stage, ButtonLayout, tempAns)
        elif LEDs[Colours.index("G")] == True:
            finalAns = stageCalculation(10, stage, ButtonLayout, tempAns)
        else:
            finalAns = stageCalculation(4, stage, ButtonLayout, tempAns)
    return finalAns

def infoValidator(infoDump: list) -> bool:
    if infoDump[0] == "END":
        print("----------------------------------------<FINAL_PHASE>----------------------------------------")
        print("The final sequence of colours to input into the module to finish Simon off is: " + Final)
        finalButtonLayout = list(input("Enter the final button layout of the module, as you did for all the others: "))
        FinalTPCommand = ""
        for i in range(0, len(Final)):
            FinalTPCommand += str(finalButtonLayout.index(Final[i]) + 1)
            if i != len(Final) - 1:
                FinalTPCommand += " "
        print("As such, the finisher, the final TP command to finish Simon off, is: " + FinalTPCommand)
        print("I no longer have any use to you, do I? Goodbye then.")
        exit()
    if len(infoDump) != 3:
        print("I expected three arguments, try again.")
        return False
    elif len(infoDump[1]) != 10:
        print("I expected the button layout to be of length 10. Try again.")
        return False
    elif len(infoDump[2]) < 3 or len(infoDump[2]) > 5:
        print("Invalid flash length. Expected 3-5 colours. Try again.")
        return False
    return True

if __name__ == "__main__":
    main()