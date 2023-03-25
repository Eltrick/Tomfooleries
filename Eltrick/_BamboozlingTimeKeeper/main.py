import math

ColourOrder = ["K", "B", "G", "C", "R", "M", "Y", "W"]
ManualOperationsList = [[ "STOP", "+1", "-10", "B1", "B3", "+559", "*3", "B1", "-65", "B1", "*10", "+84", "/4", "+485", "+459", "+45", "*2", "+456", "+45", "B3", "STOP", "+45", "-512", "*5", "*5", "*2", "*2", "B1", "/5", "-1", "+10", "B3", "*4", "-559", "+3", "STOP", "+65", "B2", "/10", "-84", "+4", "-485", "-459", "-45", "/2", "-456", "-45", "+0", "*2", "+330", "+512", "/5", "/5", "/2", "/2", "STOP" ], [ "*5", "STOP", "+25", "/2", "B2", "-58", "/3", "+158", "+46", "B1", "/10", "-46", "*3", "+84", "-485", "-90", "+256", "-98", "*5", "B3", "-59", "STOP", "+128", "/5", "*12", "*5", "/2", "B2", "-50", "+1", "-25", "*2", "/4", "+58", "STOP", "B3", "-46", "B2", "*10", "+46", "-3", "-84", "+485", "+90", "-256", "+98", "/5", "-25", "/2", "-330", "-126", "*5", "/12", "/5", "STOP", "B1"], [ "+50", "-1", "STOP", "*2", "B1", "+25", "*6", "B2", "-415", "B1", "*10", "+94", "/3", "+95", "-458", "+30", "-32", "-485", "/9", "B3", "/3", "-89", "STOP", "*10", "-120", "*7", "*2", "B3", "*2", "B3", "+25", "/2", "+4", "STOP", "/3", "-158", "+415", "B2", "/10", "-94", "+3", "-95", "+458", "-30", "+32", "+485", "*9", "+25", "*5", "+90", "/2", "/10", "+120", "STOP", "*2", "B3"], [ "/2", "B2", "-25", "STOP", "B2", "-48", "/6", "-264", "+48", "B1", "/10", "+54", "*4", "+24", "+478", "+120", "+64", "+741", "+45", "B3", "+55", "*7", "*2", "STOP", "-60", "+21", "/2", "B3", "+25", "B2", "-66", "B1", "STOP", "-25", "*3", "B1", "-48", "B2", "*10", "-54", "-4", "-24", "-478", "-120", "-64", "-741", "-45", "-25", "/5", "-90", "*5", "*10", "STOP", "/7", "/2", "B2"], [ "-25", "B1", "+66", "B2", "STOP", "+99", "+9", "*56", "-56", "B1", "*10", "+49", "/2", "-48", "+0", "-150", "-64", "-46", "-5", "B3", "-20", "/5", "/5", "/10", "STOP", "/2", "*2", "B2", "B1", "/3", "+512", "STOP", "-4", "+48", "/6", "+264", "+56", "B2", "/10", "-49", "+2", "+48", "+0", "+150", "+64", "+46", "+5", "+25", "*10", "/3", "/5", "STOP", "+60", "-21", "*2", "B1"], [ "B3", "*3", "-512", "/9", "B3", "STOP", "-6", "/7", "-99", "B1", "/10", "+21", "*2", "-78", "-45", "+15", "+32", "+155", "+46", "B3", "+23", "+48", "*5", "+1", "+180", "STOP", "/2", "B3", "B2", "*3", "STOP", "*9", "*4", "-99", "*6", "/56", "+99", "B2", "*10", "-21", "-2", "+78", "+45", "-15", "-32", "-155", "-46", "-25", "/10", "*3", "STOP", "-1", "-180", "*2", "/2", "B3"], [ "B1", "/3", "+12", "*6", "B1", "-454", "STOP", "B3", "+284", "B1", "-100", "+86", "/6", "-459", "*5", "+15", "-256", "-45", "+78", "B3", "+59", "+89", "/2", "-151", "/5", "/5", "STOP", "B1", "B3", "STOP", "-12", "/6", "/4", "+454", "-9", "*7", "-284", "B2", "+100", "-86", "-6", "+459", "/5", "-15", "+256", "+45", "-78", "+25", "+20", "STOP", "*2", "+151", "*5", "*5", "*2", "B2"], [ "B2", "B3", "/5", "B3", "B2", "*5", "-3", "STOP", "-54", "B1", "-100", "*11", "*6", "-101", "/5", "+15", "/2", "+485", "-87", "B3", "-41", "-78", "+155", "+150", "/12", "/7", "+40", "STOP", "STOP", "B1", "*5", "B2", "+0", "/5", "+6", "B2", "+54", "B2", "+100", "/11", "+6", "+101", "*5", "-15", "*2", "-485", "+87", "+0", "STOP", "/10", "-155", "-150", "*12", "*7", "-40", "B1"] ]
StartingPhrases = ["SOME#NUMBERS", "THE#NUMBERS", "NUMBERS", "TWO#NUMBERS", "THREE#NUMBERS", "FOUR#NUMBERS", "SOME#NUMBER(S)", "THE#NUMBER(S)", "NUMBER(S)", "2#NUMBERS", "3#NUMBERS", "4#NUMBERS", "SOME#NUMBER", "THE#NUMBER", "NUMBER", "ONE#NUMBER", "A#NUMBER", "1#NUMBER"]
WordsToNumbers = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "TEN": 10,
    "ELEVEN": 11,
    "TWELVE": 12,
    "THIRTEEN": 13,
    "FOURTEEN": 14,
    "FIFTEEN": 15,
    "SIXTEEN": 16,
    "SEVENTEEN": 17,
    "EIGHTEEN": 18,
    "NINETEEN": 19,
    "TWENTY": 20,
    "THIRTY": 30,
    "FOURTY": 40,
    "FIFTY": 50,
    "SIXTY": 60,
    "SEVENTY": 70,
    "EIGHTY": 80,
    "NINETY": 90
}
ButtonPressIndices = [15, 15]
Base36 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
TableRowIndices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "30", "40", "50", "60", "70", "80", "90", "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN", "TWENTY", "THIRTY", "FOURTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
TableColumnIndices = ["RED", "YELLOW", "GREEN", "CYAN", "BLUE", "MAGENTA", "WHITE", "BLACK"]
Words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
ButtonPositions = ["LEFT", "MIDDLE", "RIGHT"]
ButtonStates = ["TAP", "HOLD"]

def main() -> None:
    global ManualOperationsList
    global StartingPhrases
    global ColourOrder
    global WordsToNumbers
    global ButtonPressIndices
    global Base36
    global TableRowIndices
    global TableColumnIndices
    global Words
    global ButtonPositions
    global ButtonStates

    infoDump = [[], []]
    buttonInfoDump = [[], []]

    startingValues = [0, 0]
    stageValues = [0, 0]
    scaleFactors = [0, 0]
    states = [2, 2]

    serialNumber = list(input("Serial number: ").upper())
    serialNumberOriginal = []
    for i in range(0, len(serialNumber)):
        serialNumberOriginal.append(serialNumber[i])
        serialNumber[i] = Base36.index(serialNumber[i])

    
    portCount = int(input("Number of ports on bomb: "))
    portPlateCount = int(input("Number of port plates on bomb: "))
    
    forgetModuleCount = max(1, int(input("Number of Forget modules on bomb (FTA = 5, FMW = 2): ")))
    spevilModuleCount = max(1, int(input("Number of Speakingevil mods considered by BTK on bomb (UStores = 5, SStores = 2): ")))
    RTControlledCount = int(input("Number of RT Controlled mods considered by BTK on bomb: "))
    batteryCount = int(input("Number of batteries on bomb: "))
    step9 = [False, False]
    dayOfMonth = int(input("Day of month bomb started: "))
    litIndicatorCount = int(input("Number of lit indicators on bomb: "))
    unlitIndicatorCount = int(input("Number of unlit indicators on bomb: "))
    threeStageModuleCount = max(1, int(input("Number of 3-stage modules on bomb: ")))
    moddedPortCount = int(input("Number of modded ports on bomb: "))
    hundredIncluded = False

    simonStopsOnBomb = input("Is there a Simon Stops on the bomb? (Y/N): ").upper() == "Y"

    for i in range(0, len(infoDump)):
        print("----------------------------------------Stage_" + str(i+1) + "----------------------------------------")
        print("----------------------------------------Buttons----------------------------------------")

        # Get button information
        print("Command format: <Colour> <Digit>")
        for j in range(0, 3): # 3 buttons per stage
            buttonInfoDump[i].append(input("Enter button #" + str(j+1) + "'s information: ").upper().split(" "))
        
        print("-----------------------------------------Texts-----------------------------------------")
        # Get text information
        print("Command format: <Text_Colour> <Text>")
        print("<Text> MUST use # in place of spaces!!")
        endOfPhrase = False
        textNumber = 0
        while not endOfPhrase:
            infoDump[i].append(input("Enter text #" + str(textNumber+1) + "'s information: ").upper().split(" "))
            textNumber += 1
            if infoDump[i][-1][1] == "POINT#ZERO":
                endOfPhrase = True

        # Calculates number from given displays - Step 1, all
        for j in range(1, len(infoDump[i]) - 1):
            if j == 1:
                if infoDump[i][j][1] in WordsToNumbers:
                    startingValues[i] = WordsToNumbers[infoDump[i][j][1]]
                else:
                    startingValues[i] = int(infoDump[i][j][1])
            else:
                if infoDump[i][j][1] in WordsToNumbers:
                    startingValues[i] += WordsToNumbers[infoDump[i][j][1]]
                elif infoDump[i][j][1] == "HUNDRED":
                    if i == 0:
                        hundredIncluded = True
                    startingValues[i] *= 100
                else:
                    startingValues[i] += int(infoDump[i][j][1])
        print("Initial value for stage " + str(i + 1) + " is: " + str(startingValues[i]))
        stageValues[i] = startingValues[i]

    for i in range(0, len(infoDump)):
        print("----------------------------------------Stage_" + str(i+1) + "----------------------------------------")
        # Step 2, all
        for j in range(0, len(serialNumber) - 3):
            stageValues[i] -= serialNumber[j]
        print("Step 2_ALL: " + str(stageValues[i]))

        # Step 3, all
        stageValues[i] += 4 * (portCount + portPlateCount)
        print("Step 3_ALL: " + str(stageValues[i]))

        # Step 4, all
        stageValues[i] *= abs(forgetModuleCount - spevilModuleCount)
        print("Step 4_ALL: " + str(stageValues[i]))

        # Step 5, all
        if not simonStopsOnBomb:
            stageValues[i] = math.floor(stageValues[i] / 2)
        else:
            stageValues[i] = math.floor(stageValues[i] * 1.5)
        print("Step 5_ALL: " + str(stageValues[i]))

        # Step 6, all
        if buttonInfoDump[i][0] == buttonInfoDump[i][1] and buttonInfoDump[i][0] == buttonInfoDump[i][2]:
            ButtonPressIndices[i] = i
            print("Step 6_ALL applies, setting correct button to button " + str(ButtonPressIndices[i]))
        
        # Step 7, all
        if infoDump[i][1][0] != "RED" and ("RED" in buttonInfoDump[i][0][0] or "RED" in buttonInfoDump[i][1][0] or "RED" in buttonInfoDump[i][2][0]):
            stageValues[i] += startingValues[1 - i]
        print("Step 7_ALL: " + str(stageValues[i]))
        
        # Step 8, all
        stageValues[i] += (RTControlledCount * batteryCount)
        print("Step 8_ALL: " + str(stageValues[i]))

        # Step 9, all
        if buttonInfoDump[i][1][0] == "GREEN" or buttonInfoDump[i][1][0] == "MAGENTA":
            step9[i] = True
            ButtonPressIndices[i] = 1
            print("Step 9_ALL applies, setting correct button to button " + str(ButtonPressIndices[i]))
        
        # Step 10, all
        if stageValues[i] % 1176 <= 10 or stageValues[i] % 1176 >= 1166:
            print("Step 10_ALL applies, ending calcs for this stage.")
            continue

        # Step 11, all
        stageValues[i] += dayOfMonth
        print("Step 11_ALL: " + str(stageValues[i]))

        # Step 12, all
        stageValues[i] = stageValues[i] + 20 * (litIndicatorCount - unlitIndicatorCount)
        print("Step 12_ALL: " + str(stageValues[i]))

        # Step 13, all
        if startingValues[i] < 5000:
            stageValues[i] *= threeStageModuleCount
        else:
            stageValues[i] += threeStageModuleCount
        print("Step 13_ALL: " + str(stageValues[i]))

        # Step 14, all
        stageValues[i] -= 6 * moddedPortCount
        print("Step 14_ALL: " + str(stageValues[i]))

        if i == 0: # Stage 1 calcs
            # Step 17, stage 1
            for j in range(0, len(infoDump[i])):
                if infoDump[i][j][1] in TableRowIndices:
                    if ManualOperationsList[TableColumnIndices.index(infoDump[i][j][0])][TableRowIndices.index(infoDump[i][j][1])] == "STOP":
                        print("(" + infoDump[i][j][1] + ", " + infoDump[i][j][0] + ") = STOP, stopping this step.")
                        continue
                    else:
                        stageValues[i] = PerformOperation(stageValues[i], ManualOperationsList[TableColumnIndices.index(infoDump[i][j][0])][TableRowIndices.index(infoDump[i][j][1])], i)
                        print("(" + infoDump[i][j][1] + ", " + infoDump[i][j][0] + ") = " + ManualOperationsList[TableColumnIndices.index(infoDump[i][j][0])][TableRowIndices.index(infoDump[i][j][1])] + ", performing operation gives: " + str(stageValues[i]))

            # Step 18, stage 1
            if StartingPhrases.index(infoDump[i][0][1]) % 6 > 2:
                firstLetterUnlit = list(input("Input first letters of each unlit indicator, as one string: ").upper())
                for j in range(0, len(firstLetterUnlit)):
                    stageValues[i] += Base36.index(firstLetterUnlit[j]) - 9
            print("Step 18_1: " + str(stageValues[i]))
            
            # Step 19, stage 1
            if hundredIncluded:
                stageValues[i] = math.floor(stageValues[i] / 100)
            print("Step 19_1: " + str(stageValues[i]))
            
            # Step 20, stage 1
            if input("Is there a Simon's Stages on the bomb? (Y/N): ").upper() == "N" and input("Is there an Ubermodule on the bomb? (Y/N): ").upper() == "Y":
                print("Step 20_1 applies, ending stage 1 calcs.")
                continue

            # Step 21, stage 1
            if input("Are there needy modules on the bomb? (Y/N): ").upper() == "Y":
                stageValues[i] += 99 * int(input("Input number of needy modules on the bomb: "))
            print("Step 21_1: " + str(stageValues[i]))

            # Step 22, stage 1
            if "(" in infoDump[i][0][1] or "1" in infoDump[i][0][1] or "2" in infoDump[i][0][1] or "3" in infoDump[i][0][1] or "4" in infoDump[i][0][1]:
                for j in range(0, len(buttonInfoDump[i])):
                    stageValues[i] = PerformOperation(stageValues[i], ManualOperationsList[TableColumnIndices.index(buttonInfoDump[i][j][0])][TableRowIndices.index(buttonInfoDump[i][j][1])], i)
                    print("(" + buttonInfoDump[i][j][1] + ", " + buttonInfoDump[i][j][0] + ") = " + ManualOperationsList[TableColumnIndices.index(buttonInfoDump[i][j][0])][TableRowIndices.index(buttonInfoDump[i][j][1])] + ", performing operation gives: " + str(stageValues[i]))
            print("Step 22_1: " + str(stageValues[i]))

            # Step 23, stage 1
            if stageValues[i] < 0:
                stageValues[i] *= -6
            print("Step 23_1: " + str(stageValues[i]))

            # Step 24, stage 1
            for j in range(3, len(serialNumber)):
                stageValues[i] += serialNumber[j]
            print("Step 24_1: " + str(stageValues[i]))
            print("Ending calculations for stage 1.")
        elif i == 1: # Stage 2 calcs
            # Step 18, stage 2
            if StartingPhrases.index(infoDump[i][0][1]) % 6 > 2:
                stageValues[i] = PerformOperation(stageValues[i], ManualOperationsList[TableColumnIndices.index(infoDump[i][1][0])][TableRowIndices.index(infoDump[i][1][1])], i)
            print("Step 18_2: " + str(stageValues[i]))
            
            # Step 19, stage 2
            if StartingPhrases.index(infoDump[i][0][1]) >= 12:
                if infoDump[i][-2][1] == "HUNDRED":
                    stageValues[i] *= 100
                else:
                    stageValues[i] = PerformOperation(stageValues[i], ManualOperationsList[TableColumnIndices.index(infoDump[i][-2][0])][TableRowIndices.index(infoDump[i][-2][1])], i)
            print("Step 19_2: " + str(stageValues[i]))

            # Step 20+21, stage 2
            if "(" in infoDump[i][0][1] or "1" in infoDump[i][0][1] or "2" in infoDump[i][0][1] or "3" in infoDump[i][0][1] or "4" in infoDump[i][0][1]:
                if ManualOperationsList[7 - TableColumnIndices.index(buttonInfoDump[i][1][0])][(TableRowIndices.index(infoDump[0][1][1]) + TableRowIndices.index(infoDump[1][1][1])) % 56] == "STOP":
                    continue
                stageValues[i] = PerformOperation(stageValues[i], ManualOperationsList[7 - TableColumnIndices.index(buttonInfoDump[i][1][0])][(TableRowIndices.index(infoDump[0][1][1]) + TableRowIndices.index(infoDump[1][1][1])) % 56], i)
                print("1: " + ManualOperationsList[7 - TableColumnIndices.index(buttonInfoDump[i][1][0])][(TableRowIndices.index(infoDump[0][1][1]) + TableRowIndices.index(infoDump[1][1][1])) % 56])
                if ManualOperationsList[(TableColumnIndices.index(buttonInfoDump[i][2][0]) + TableColumnIndices.index(buttonInfoDump[i][0][0])) % 8][abs(TableRowIndices.index(infoDump[0][1][1]) - TableRowIndices.index(infoDump[1][1][1]))] == "STOP":
                    continue
                print("2: " + ManualOperationsList[(TableColumnIndices.index(buttonInfoDump[i][2][0]) + TableColumnIndices.index(buttonInfoDump[i][0][0])) % 8][abs(TableRowIndices.index(infoDump[0][1][1]) - TableRowIndices.index(infoDump[1][1][1]))])
                stageValues[i] = PerformOperation(stageValues[i], ManualOperationsList[(TableColumnIndices.index(buttonInfoDump[i][2][0]) + TableColumnIndices.index(buttonInfoDump[i][0][0])) % 8][abs(TableRowIndices.index(infoDump[0][1][1]) - TableRowIndices.index(infoDump[1][1][1]))], i)
            print("Step 20+21_2: " + str(stageValues[i]))

            # Step 22, stage 2
            if buttonInfoDump[i][0][0] == buttonInfoDump[i][2][0] and buttonInfoDump[i][0][0] == infoDump[i][1][0] and buttonInfoDump[i][0][0] != buttonInfoDump[i][1][0]:
                ButtonPressIndices[i] = 1
                print("Step 22_2 applies, setting correct button to middle.")

            # Step 23, stage 2
            if step9[0]:
                stageValues[i] += 25
            elif step9[1]:
                stageValues[i] += 150
            else:
                stageValues[i] -= 250
            print("Step 23_2: " + str(stageValues[i]))

            # Step 24, stage 2
            stageValues[i] -= (int(input("Input number of Kritzy modules considered by BTK: ")) * 10)
            print("Step 24_2: " + str(stageValues[i]))

            # Step 25, stage 2
            if stageValues[i] < 0:
                stageValues[i] *= -65
                print("Step 25_2 applies, value is now " + str(stageValues[i]) + ", and END")
                continue
            
            # Step 26, stage 2
            if (len(buttonInfoDump[i][0][0]) + len(buttonInfoDump[i][1][0]) + len(buttonInfoDump[i][2][0])) > 12:
                sumOfLengths = 0
                for j in range(0, len(infoDump[i])):
                    if infoDump[i][j][0] != "WHITE":
                        print(infoDump[i][j][0] + ": " + str(len(infoDump[i][j][0])))
                        sumOfLengths += len(infoDump[i][j][0])
                if sumOfLengths == 0:
                    stageValues[i] *= 2
                else:
                    stageValues[i] = math.floor(stageValues[i] / sumOfLengths)
            print("Step 26_2: " + str(stageValues[i]))

            # Step 27, stage 2
            twoFactorCount = int(input("Input the number of Two Factor widgets on the bomb: "))
            if twoFactorCount != 0:
                stageValues[i] += (50 * twoFactorCount)
            print("Step 27_2: " + str(stageValues[i]))

            # Step 28, stage 2
            if len(infoDump[i]) == 7:
                stageValues[i] = math.floor(stageValues[i] / 7)
            print("Step 28_2: " + str(stageValues[i]))

            # Step 29, stage 2
            letterCounts = [len(buttonInfoDump[i][0][0]), len(buttonInfoDump[i][1][0]), len(buttonInfoDump[i][2][0])]
            maxLetterCount = max(letterCounts)
            tieQuestionMark = 0
            for j in range(0, len(buttonInfoDump)):
                if len(buttonInfoDump[j][0]) == maxLetterCount:
                    tieQuestionMark += 1
            if tieQuestionMark != 1 or input("Is there an RT sensitive module considered by BTK on the bomb? (Y/N): ").upper() == "Y":
                ButtonPressIndices[i] = letterCounts.index(maxLetterCount)
                print("Step 29_2 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
            
            # Step 30, stage 2
            stageValues[i] = math.floor(stageValues[i] / 3)
            print("Step 30_2: " + str(stageValues[i]))

            # Step 31, stage 2
            stageValues[i] += 10 * int(input("Input number of indicators that has a letter in \"Speakingevil\": "))
            print("Step 31_2: " + str(stageValues[i]))
    for i in range(0, len(stageValues)):
        while stageValues[i] < 10:
            stageValues[i] += 16
    print("Final values = " + str(stageValues))
    print("--------------------------------------SCALE_FACTOR--------------------------------------")
    unicorn = (input("Look at page 6, do you have the unicorn? (Y/N): ").upper() == "Y")
    if unicorn:
        for i in range(0, len(scaleFactors)):
            scaleFactors[i] == 2
            print("Unicorn occured, scale factors are 2")
    else:
        bombStartingTime = False
        for i in range(0, len(scaleFactors)):
            print("----------------------------------------Stage_" + str(i+1) + "----------------------------------------")
            # Scale factor, stage 1
            if i == 0:
                # If starting value < 5000 -> +1
                if startingValues[i] < 5000:
                    scaleFactors[i] += 1
                    print("Starting value less than 5000, adding 1: " + str(scaleFactors[i]))
                
                # Subtract 1 per 2 batteries
                scaleFactors[i] -= math.floor(batteryCount / 2)
                print("Subtracting battery/2 (" + str(math.floor(batteryCount / 2)) + "): " + str(scaleFactors[i]))
                
                # FT present -> +1
                if input("Is Forget This present? (Y/N): ").upper() == "Y":
                    scaleFactors[i] += 1
                    print("FT present, adding 1: " + str(scaleFactors[i]))
                
                # 4 or more SN digits -> +3
                digitCount = 0
                for j in range(0, len(serialNumberOriginal)):
                    if serialNumberOriginal[j] in "0123456789":
                        digitCount += 1
                if digitCount >= 4:
                    scaleFactors[i] += 3
                    print(">= 4 digits, adding 3: " + str(scaleFactors[i]))
                
                # TTK present -> +2
                if input("Is The Time Keeper present? (Y/N): ").upper() == "Y":
                    scaleFactors[i] += 2
                    print("TTKeeper present, adding 2: " + str(scaleFactors[i]))
                
                # Starting phrase considered undefinable -> +2
                if StartingPhrases.index(infoDump[i][0][1]) % 6 < 3:
                    scaleFactors[i] += 2
                    print("Starting Phrase not definable, adding 2: " + str(scaleFactors[i]))
                
                # Bomb starting time >= 30:00 -> +2
                bombStartingTime = (input("Is the bomb starting time 30:00 or higher? (Y/N): ").upper() == "Y")
                if bombStartingTime:
                    scaleFactors[i] += 2
                    print("Bomb starting time >= 30:00, adding 2: " + str(scaleFactors[i]))
                
                # 3 SN letters -> +2
                serialLetterCount = 0
                for j in range(0, len(serialNumberOriginal)):
                    if serialNumberOriginal[j] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        serialLetterCount += 1
                if serialLetterCount == 3:
                    scaleFactors[i] += 2
                    print("Serial Number contains exactly 3 letters, adding 2: " + str(scaleFactors[i]))
                
                # FMN present -> +1
                if input("Is Forget Me Not present? (Y/N): ").upper() == "Y":
                    scaleFactors[i] += 1
                    print("FMN present, adding 1: " + str(scaleFactors[i]))
                
                # Final value >= 10000 -> /2
                if stageValues[i] >= 10000:
                    scaleFactors[i] = math.floor(scaleFactors[i] / 2)
                    print("Final value >= 10000, dividing by 2: " + str(scaleFactors[i]))
            else: # Scale factor, stage 2
                # If starting value < 5000 -> +1
                if startingValues[i] < 5000:
                    scaleFactors[i] += 1
                    print("Starting value less than 5000, adding 1: " + str(scaleFactors[i]))

                scaleFactors[i] -= int(input("Input number of battery holders: "))
                print("Subtracting battery holder count: " + str(scaleFactors[i]))

                # FN present -> +1
                if input("Is Forget Enigma present? (Y/N): ").upper() == "Y":
                    scaleFactors[i] += 1
                    print("FN present, adding 1: " + str(scaleFactors[i]))
                
                # 3 SN letters -> +2
                serialLetterCount = 0
                for j in range(0, len(serialNumberOriginal)):
                    if serialNumberOriginal[j] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        serialLetterCount += 1
                if serialLetterCount >= 4:
                    scaleFactors[i] += 3
                    print(">= 4 letters, adding 3: " + str(scaleFactors[i]))
                
                # TTKey present -> +2
                if input("Is Turn The Key present? (Y/N): ").upper() == "Y":
                    scaleFactors[i] += 2
                    print("TTKey present, adding 2: " + str(scaleFactors[i]))
                
                # Starting phrase considered definable -> +2
                if StartingPhrases.index(infoDump[i][0][1]) % 6 >= 3:
                    scaleFactors[i] += 2
                    print("Starting Phrase definable, adding 2: " + str(scaleFactors[i]))

                # Bomb starting time >= 30:00 -> +2
                if bombStartingTime:
                    scaleFactors[i] += 2
                    print("Bomb starting time >= 30:00, adding 2: " + str(scaleFactors[i]))

                # 3 SN digits -> +3
                digitCount = 0
                for j in range(0, len(serialNumberOriginal)):
                    if serialNumberOriginal[j] in "0123456789":
                        digitCount += 1
                if digitCount == 3:
                    scaleFactors[i] += 2
                    print("Exactly 3 SN digits, adding 2: " + str(scaleFactors[i]))
                
                # FIN present -> +1
                if input("Is Forget It Not present? (Y/N): ").upper() == "N":
                    scaleFactors[i] += 1
                    print("FIN not present, adding 1: " + str(scaleFactors[i]))
                
                # Final value >= 10000 -> /2
                if stageValues[i] >= 10000:
                    scaleFactors[i] = math.floor(scaleFactors[i] / 2)
                    print("Final value >= 10000, dividing by 2: " + str(scaleFactors[i]))
            if scaleFactors[i] < 2:
                scaleFactors[i] = 2
            if scaleFactors[i] > 4:
                scaleFactors[i] = 4
        print("Scale factors are: " + str(scaleFactors))

    # If correct button has not been assigned
    print("--------------------------------------BACKUP_BUTTON--------------------------------------")
    haveReachedBefore = False
    parallelPortPresent = False
    rcaPortPresent = False
    blackCipherPresent = False
    for i in range(0, len(ButtonPressIndices)):
        if ButtonPressIndices[i] > 2:
            print("--------------------------------------STAGE_" + str(i+1) + "--------------------------------------")
            someRuleApplied = False
            # Rule 1
            if stageValues[i] > 0 and stageValues[i] < 10000:
                ButtonPressIndices[i] = 0
                someRuleApplied = True
                print("Rule 1 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                continue
            
            # Rule 2
            if not haveReachedBefore:
                parallelPortPresent = input("Is a parallel port present? (Y/N)").upper() == "Y"
            if parallelPortPresent:
                magentaButtonCount = 0
                magentaButtons = []
                for j in range(0, len(buttonInfoDump[i])):
                    if buttonInfoDump[i][j][0] == "MAGENTA":
                        magentaButtons.append(j)
                        magentaButtonCount += 1
                if magentaButtonCount == 1 and not someRuleApplied:
                    ButtonPressIndices[i] = magentaButtons[0]
                    someRuleApplied = True
                    print("Rule 2 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                    continue
            
            # Rule 3
            if not haveReachedBefore:
                rcaPortPresent = input("Is there an RCA port? (Y/N): ").upper() == "Y"
            if rcaPortPresent:
                whiteRedButtons = []
                whitePresent = False
                redPresent = False
                for j in range(0, len(buttonInfoDump[i])):
                    if buttonInfoDump[i][j][0] == "RED":
                        redPresent = True
                        whiteRedButtons.append(j)
                    elif buttonInfoDump[i][j][0] == "WHITE":
                        whitePresent = True
                        whiteRedButtons.append(j)
                if whitePresent and redPresent and len(whiteRedButtons) == 2 and not someRuleApplied:
                    for j in range(0, len(buttonInfoDump[i])):
                        if j not in whiteRedButtons:
                            ButtonPressIndices[i] = j
                    someRuleApplied = True
                    print("Rule 3 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                    continue
            
            # Rule 4
            if not haveReachedBefore:
                blackCipherPresent = input("Is Black Cipher present on bomb? (Y/N): ").upper() == "Y"
            if blackCipherPresent:
                blackButtonCount = 0
                blackButtons = []
                for j in range(0, len(buttonInfoDump[i])):
                    if buttonInfoDump[i][j][0] == "MAGENTA":
                        blackButtons.append(j)
                        blackButtonCount += 1
                if blackButtonCount == 1 and not someRuleApplied:
                    ButtonPressIndices[i] = blackButtons[0]
                    someRuleApplied = True
                    print("Rule 4 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                    continue
            
            # Rule 5
            noSharedColours = True
            for j in range(0, len(buttonInfoDump[i])):
                for k in range(0, len(infoDump[i])):
                    if buttonInfoDump[i][j] == infoDump[i][k][0] and buttonInfoDump[i][j] != "WHITE":
                        noSharedColours = False
            if noSharedColours and not someRuleApplied:
                ButtonPressIndices[i] = 2
                someRuleApplied = True
                print("Rule 5 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                continue
            
            # Rule 6
            oopsAllWhite = True
            for j in range(0, len(infoDump[i])):
                if infoDump[i][j][0] != "WHITE":
                    oopsAllWhite = False
            if oopsAllWhite:
                buttonsPresent = []
                for j in range(0, len(buttonInfoDump[i])):
                    for k in range(0, len(infoDump[i])):
                        if buttonInfoDump[i][j][0] == infoDump[i][k][0]:
                            buttonsPresent.append(j)
                        elif Words[int(buttonInfoDump[i][j][0])] == infoDump[i][k][0]:
                            buttonsPresent.append(j)
                if len(buttonsPresent) == 2 and not someRuleApplied:
                    for j in range(0, len(buttonInfoDump[i])):
                        if j not in buttonsPresent:
                            ButtonPressIndices[i] = j
                            someRuleApplied = True
                            print("Rule 6 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                            continue
            
            # Rule 7
            redPresent = False
            greenPresent = False
            bluePresent = False
            blueIndex = 0
            for j in range(0, len(buttonInfoDump[i])):
                if buttonInfoDump[i][j][0] == "RED":
                    redPresent = True
                elif buttonInfoDump[i][j][0] == "GREEN":
                    greenPresent = True
                elif buttonInfoDump[i][j][0] == "BLUE":
                    blueIndex = j
                    bluePresent = True
            if redPresent and greenPresent and bluePresent and not someRuleApplied:
                ButtonPressIndices[i] = blueIndex
                someRuleApplied = True
                print("Rule 7 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                continue
            
            # Rule 8
            leftAndRight = False
            if not haveReachedBefore:
                leftAndRight = input("Is Left And Right on the bomb? (Y/N): ").upper() == "Y"
            if leftAndRight and not someRuleApplied:
                ButtonPressIndices[i] = 1
                someRuleApplied = True
                print("Rule 8 applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
                continue
            
            # Rules 9+10
            if i == 0 and not someRuleApplied:
                ButtonPressIndices[i] = stageValues[i] % 3
                someRuleApplied = True
                print("Final rule applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
            elif i == 1 and not someRuleApplied:
                ButtonPressIndices[i] = 2 - (stageValues[i] % 3)
                someRuleApplied = True
                print("Final rule applies, setting correct button to button " + str(ButtonPressIndices[i] + 1))
            haveReachedBefore = True
    print("--------------------------------------BACKUP_DONE--------------------------------------")

    # Determine hold or press
    print("--------------------------------------DETERMINING_STATE--------------------------------------")
    rule1 = False
    haveReachedBefore = False
    for i in range(0, len(states)):
        someRuleApplied = False
        print("--------------------------------------STAGE_" + str(i+1) + "--------------------------------------")
        # Rule 1
        if not haveReachedBefore:
            rule1 = input("Is there The Very Annoying Button or Multitask on the bomb? (Y/N): ").upper() == "Y"
        if rule1:
            states[i] = 0
            someRuleApplied = True
            print("Rule 1 applies, setting state to tap.")
            continue
        
        # Rule 2
        labelsPresent = [False, False, False]
        for j in range(0, len(buttonInfoDump[i])):
            if j != ButtonPressIndices[i]:
                for k in range(0, len(infoDump[i])):
                    if buttonInfoDump[i][j][1] == infoDump[i][k][1] or Words[int(buttonInfoDump[i][j][1])] == infoDump[i][k][1]:
                        labelsPresent[j] = True
        unusedPos = []
        for j in range(0, len(labelsPresent)):
            if j != ButtonPressIndices[i]:
                unusedPos.append(j)
        if labelsPresent[unusedPos[0]] and labelsPresent[unusedPos[1]] and not someRuleApplied:
            states[i] = 1
            someRuleApplied = True
            print("Rule 2 applies, setting state to hold.")
            continue
        
        # Rule 3
        for k in range(0, len(infoDump[i])):
            if buttonInfoDump[i][ButtonPressIndices[i]][1] == infoDump[i][k][1] or Words[int(buttonInfoDump[i][ButtonPressIndices[i]][1])] == infoDump[i][k][1] and not someRuleApplied:
                states[i] = 0
                someRuleApplied = True
                print("Rule 3 applies, setting state to tap.")
                continue

        # Rule 4
        if (int(buttonInfoDump[i][0][1]) <= int(buttonInfoDump[i][1][1]) and int(buttonInfoDump[i][1][1]) <= int(buttonInfoDump[i][2][1])) or (int(buttonInfoDump[i][0][1]) >= int(buttonInfoDump[i][1][1]) and int(buttonInfoDump[i][1][1]) >= int(buttonInfoDump[i][2][1])) and not someRuleApplied:
            states[i] = 1
            someRuleApplied = True
            print("Rule 4 applies, setting state to hold.")
            continue

        # Rule 5
        posOthers = []
        for j in range(0, len(buttonInfoDump[i])):
            if j != ButtonPressIndices[i]:
                posOthers.append(j)
        positiveDifference = abs(int(buttonInfoDump[i][posOthers[0]][1]) - int(buttonInfoDump[i][posOthers[1]][1]))
        if abs(positiveDifference - int(buttonInfoDump[i][ButtonPressIndices[i]][1])) <= 2 and not someRuleApplied:
            states[i] = 0
            someRuleApplied = True
            print("Rule 5 applies, setting state to tap.")
            continue

        # Rule 6
        digitToCheck = (int(buttonInfoDump[i][posOthers[0]][1]) + int(buttonInfoDump[i][posOthers[1]][1])) % 10
        if int(buttonInfoDump[i][ButtonPressIndices[i]][1]) == digitToCheck and not someRuleApplied:
            states[i] = 1
            someRuleApplied = True
            print("Rule 6 applies, setting state to hold.")
            continue

        # Rule 7
        digitToCheck = (int(buttonInfoDump[i][posOthers[0]][1]) * int(buttonInfoDump[i][posOthers[1]][1])) % 10
        if int(buttonInfoDump[i][ButtonPressIndices[i]][1]) == digitToCheck and not someRuleApplied:
            states[i] = 0
            someRuleApplied = True
            print("Rule 7 applies, setting state to tap.")
            continue
        
        # Otherwise, Rule 8
        if states[i] > 1 and not someRuleApplied:
            states[i] = 1
            someRuleApplied = True
            print("No rules applied, setting state to hold.")
    
    # Summary
    print("--------------------------------------SUMMARY--------------------------------------")
    for i in range(0, len(states)):
        print("--------------------------------------STAGE_" + str(i+1) + "--------------------------------------")
        logButton = ButtonPositions[ButtonPressIndices[i]]
        logState = ButtonStates[states[i]]
        possibleTimes = []
        possibleLoggingTimes = []
        for j in range(0, 14): # Outputs as many values as range.max to interact with button for
            possibleTimes.append(stageValues[i] * (scaleFactors[i] ** j))
            hours = str(math.floor(possibleTimes[j] / 3600))
            minutes = str(math.floor((possibleTimes[j] % 3600) / 60))
            seconds = str(math.floor(possibleTimes[j] % 60))
            possibleLoggingTimes.append(hours + ":" + minutes + ":" + seconds)
        print("For stage " + str(i+1) + ", you need to " + logState + " the " + logButton + " button on any of the following times: " + ", ".join(possibleLoggingTimes) + ", or " + str(possibleTimes))
    print("Okay, you're on your own now, tough luck if you have to hold a button. Bye!")

def PerformOperation(value: int, operation: str, stage: int) -> int:
    if operation == "STOP":
        if stage != 1:
            return 2754179645498984654625135587956362163165459687966619546898798746363165959498986646
        else:
            return math.floor(value / 17)
    elif "B" in operation:
        if stage != 1:
            ButtonPressIndices[stage] = int(operation[1:]) - 1
            return value
        else:
            return value * (int(operation[1:]) + 1)
    elif "+" in operation:
        return value + int(operation[1:])
    elif "-" in operation:
        return value - int(operation[1:])
    elif "*" in operation:
        return value * int(operation[1:])
    elif "/" in operation:
        return math.floor(value / int(operation[1:]))

if __name__ == "__main__":
    main()