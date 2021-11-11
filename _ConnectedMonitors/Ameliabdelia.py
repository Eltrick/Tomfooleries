import math

MonitorColours = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
MonitorTexts = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
MonitorDisplays = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MonitorLights = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
MonitorConnections = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
Values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ValueTexts = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Blinking = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

RLightValues = [[1, -3, 3], [-3, 1, 2], [3, -1, -1], [1, -2, -3], [-2, 2, 2], [-1, 2, 3]]
BLightValues = [[2, -1, 3], [-1, 3, 3], [2, 2, 1], [-2, 1, -2], [-3, -2, 1], [-3, -1, 3]]

# R G B P O W
# WireValues[Dir][Col]
Orders = ["R", "G", "B", "P", "O", "W"]
WireValues = [[-3, 2, -2, 3, -1, 1], [3, -1, 1, 2, -3, -2], [-1, 1, 3, 2, -2, -3], [-3, 1, -1, 3, -2, 2], [3, 1, 2, -1, -2, -3], [3, -2, 2, -3, 1, -1], [3, -1, -3, 1, 2, -2], [-3, -2, 1, -1, 2, 3]]
Blinkenlights = [[2, -6, -2], [-6, 6, -6], [-4, -4, 4], [6, -2, 2], [4, -2, 6], [4, 2, -4]]

def main() -> None:
    global MonitorColours
    global MonitorDisplays
    global MonitorLights
    global MonitorConnections
    global Green
    global Values
    global Blinking
    global Primes
    global Orders
    global WireValues
    global RLightValues
    global BLightValues
    global Blinkenlights
    
    print("Welcome, and enjoy your time with this program while it lasts.")
    print("Command Format: <MonitorColour> <MonitorNumber> <MonitorLight(s)> <Blinking?(Y/N)> <Wires(Start(North))>")
    infoDump = input("Input every monitor's information in the command format above, separating each monitor with exactly ';': ").upper().split(";")
    for i in range(0, 15):
        infoDump[i] = infoDump[i].split(" ")
        MonitorColours[i] = infoDump[i][0]
        MonitorTexts[i] = infoDump[i][1]
        MonitorDisplays[i] = int(infoDump[i][1])
        MonitorLights[i] = list(infoDump[i][2].replace("-", ""))
        for j in range(0, len(infoDump[i][3])):
            Blinking[i].append(True) if infoDump[i][3][j] == "Y" else Blinking[i].append(False)
        MonitorConnections[i] = list(infoDump[i][4])
    
    # Section 1: Initial Scores
    for x in range(0, 15):
        if MonitorColours[x] == "R":
            Values[x] = 2
        if MonitorColours[x] == "O":
            Values[x] = 1
        if MonitorColours[x] == "G":
            Values[x] = 0
        if MonitorColours[x] == "B":
            Values[x] = -1
        if MonitorColours[x] == "P":
            Values[x] = -2
    print("After Section 1: " + str(Values))
    
    # Section 2: Numbers
    for m in range(0, 15):
        print("---Monitor #" + str(m + 1) + " calculations---")
        if MonitorDisplays[m] % 7 == 0:
            Values[m] += 3
            print("Divisible by 7, new value: " + str(Values[m]))
        if int(MonitorTexts[m][0]) + int(MonitorTexts[m][1]) > 10:
            Values[m] += 3
            print("a + b > 10, new value: " + str(Values[m]))
        if MonitorTexts[m][1] == "0":
            Values[m] += 3
            print("Last digit is 0, new value: " + str(Values[m]))
        if MonitorTexts[m][1] == "7":
            Values[m] += 2
            print("Last digit is 7, new value: " + str(Values[m]))
        if MonitorDisplays[m] % 9 == 0:
            Values[m] += 2
            print("Divisible by 9, new value: " + str(Values[m]))
        if MonitorTexts[m][0] == "5":
            Values[m] += 2
            print("First digit is 5, new value: " + str(Values[m]))
        if int(MonitorTexts[m][1]) - int(MonitorTexts[m][0]) < 0:
            Values[m] += 1
            print("b - a < 0, new value: " + str(Values[m]))
        if MonitorDisplays[m] in Primes:
            Values[m] += 1
            print("Prime, new value: " + str(Values[m]))
        if MonitorTexts[m][1] == "4":
            Values[m] += 1
            print("Last digit is 4, new value: " + str(Values[m]))
        if MonitorTexts[m][0] == "2":
            Values[m] += -1
            print("First digit is 2, new value: " + str(Values[m]))
        if int(MonitorTexts[m][0]) in Primes:
            Values[m] += -1
            print("a is prime, new value: " + str(Values[m]))
        if MonitorTexts[m][1] == "6":
            Values[m] += -1
            print("Last digit is 6, new value: " + str(Values[m]))
        if MonitorDisplays[m] % 6 == 0:
            Values[m] += -2
            print("Divisible by 6, new value: " + str(Values[m]))
        if MonitorTexts[m][1] == "8":
            Values[m] += -2
            print("Last digit is 8, new value: " + str(Values[m]))
        if MonitorTexts[m][0] == "3":
            Values[m] += -2
            print("First digit is 3, new value: " + str(Values[m]))
        if int(MonitorTexts[m][0]) + 1 == int(MonitorTexts[m][1]):
            Values[m] += -3
            print("a + 1 = b, new value: " + str(Values[m]))
        if MonitorDisplays[m] % 10 == 0:
            Values[m] += -3
            print("Divisible by 10, new value: " + str(Values[m]))
        if int(MonitorTexts[m][1]) in Primes:
            Values[m] += -3
            print("b is prime, new value: " + str(Values[m]))
    print("After Section 2: " + str(Values))
    
    for i in range(0, 15):
        if len(MonitorLights[i]) != 0:
            # Section 3: Number of Lights
            if MonitorDisplays[i] % 2 == 0:
                Values[i] += len(MonitorLights[i])
            else:
                Values[i] += 0 - len(MonitorLights[i])
    print("After Section 3: " + str(Values))
    
    for i in range(0, 15):
        # R G B P O W
        ColourOccurences = [0, 0, 0, 0, 0, 0]
        # Section 4: Colour of Lights
        for j in range(0, len(MonitorLights[i])):
            Values[i] += BLightValues[Orders.index(MonitorLights[i][j])][ColourOccurences[Orders.index(MonitorLights[i][j])]]
            ColourOccurences[Orders.index(MonitorLights[i][j])] += 1
            if Blinking[i][j]:
                Values[i] += Blinkenlights[Orders.index(MonitorLights[i][j])][j]
            else:
                Values[i] += RLightValues[Orders.index(MonitorLights[i][j])][j]
    print("After Section 4: " + str(Values))
    
    for i in range(0, 15):
        # Section 5: Connections
        WireOccurences = [0, 0, 0, 0, 0, 0]
        for j in range(0, len(MonitorConnections[i])):
            if MonitorConnections[i][j] == "R":
                WireOccurences[0] += 1
            elif MonitorConnections[i][j] == "G":
                WireOccurences[1] += 1
            elif MonitorConnections[i][j] == "B":
                WireOccurences[2] += 1
            elif MonitorConnections[i][j] == "P":
                WireOccurences[3] += 1
            elif MonitorConnections[i][j] == "O":
                WireOccurences[4] += 1
            elif MonitorConnections[i][j] == "W":
                WireOccurences[5] += 1
        print("Wire Occurences #" + str(i) + ": " + str(WireOccurences))
        for j in range(0, len(MonitorConnections[i])):
            if MonitorConnections[i][j] != "-":
                Values[i] += WireValues[j][Orders.index(MonitorConnections[i][j])] * WireOccurences[Orders.index(MonitorConnections[i][j])]
    print("Final Values for each monitor: " + str(Values))
    
    funnyCase = True if (input("Are any of the monitors green? (Y/N): ").upper() == "Y") else False
    while funnyCase:
        print("Command Format: <MonitorPosition> <NewMonitorNumber>")
        smallInfoDump = input("Input the position and new number of a green monitor, if it has changed: ").upper().split(" ")
        if smallInfoDump[0] == "END":
            print("The module should now solve, and that is the end. Goodbye - L.V.")
            exit()
        MonitorTexts[int(smallInfoDump[0]) - 1] = smallInfoDump[1]
        MonitorDisplays[int(smallInfoDump[0]) - 1] = int(smallInfoDump[1])
        # Section 1: Initial Scores
        for x in range(0, 15):
            if MonitorColours[x] == "R":
                Values[x] = 2
            if MonitorColours[x] == "O":
                Values[x] = 1
            if MonitorColours[x] == "G":
                Values[x] = 0
            if MonitorColours[x] == "B":
                Values[x] = -1
            if MonitorColours[x] == "P":
                Values[x] = -2
        print("After Section 1: " + str(Values))
        
        # Section 2: Numbers
        for m in range(0, 15):
            print("---Monitor #" + str(m + 1) + " calculations---")
            if MonitorDisplays[m] % 7 == 0:
                Values[m] += 3
                print("Divisible by 7, new value: " + str(Values[m]))
            if int(MonitorTexts[m][0]) + int(MonitorTexts[m][1]) > 10:
                Values[m] += 3
                print("a + b > 10, new value: " + str(Values[m]))
            if MonitorTexts[m][1] == "0":
                Values[m] += 3
                print("Last digit is 0, new value: " + str(Values[m]))
            if MonitorTexts[m][1] == "7":
                Values[m] += 2
                print("Last digit is 7, new value: " + str(Values[m]))
            if MonitorDisplays[m] % 9 == 0:
                Values[m] += 2
                print("Divisible by 9, new value: " + str(Values[m]))
            if MonitorTexts[m][0] == "5":
                Values[m] += 2
                print("First digit is 5, new value: " + str(Values[m]))
            if int(MonitorTexts[m][1]) - int(MonitorTexts[m][0]) < 0:
                Values[m] += 1
                print("b - a < 0, new value: " + str(Values[m]))
            if MonitorDisplays[m] in Primes:
                Values[m] += 1
                print("Prime, new value: " + str(Values[m]))
            if MonitorTexts[m][1] == "4":
                Values[m] += 1
                print("Last digit is 4, new value: " + str(Values[m]))
            if MonitorTexts[m][0] == "2":
                Values[m] += -1
                print("First digit is 2, new value: " + str(Values[m]))
            if int(MonitorTexts[m][0]) in Primes:
                Values[m] += -1
                print("a is prime, new value: " + str(Values[m]))
            if MonitorTexts[m][1] == "6":
                Values[m] += -1
                print("Last digit is 6, new value: " + str(Values[m]))
            if MonitorDisplays[m] % 6 == 0:
                Values[m] += -2
                print("Divisible by 6, new value: " + str(Values[m]))
            if MonitorTexts[m][1] == "8":
                Values[m] += -2
                print("Last digit is 8, new value: " + str(Values[m]))
            if MonitorTexts[m][0] == "3":
                Values[m] += -2
                print("First digit is 3, new value: " + str(Values[m]))
            if int(MonitorTexts[m][0]) + 1 == int(MonitorTexts[m][1]):
                Values[m] += -3
                print("a + 1 = b, new value: " + str(Values[m]))
            if MonitorDisplays[m] % 10 == 0:
                Values[m] += -3
                print("Divisible by 10, new value: " + str(Values[m]))
            if int(MonitorTexts[m][1]) in Primes:
                Values[m] += -3
                print("b is prime, new value: " + str(Values[m]))
        print("After Section 2: " + str(Values))
        
        for i in range(0, 15):
            if len(MonitorLights[i]) != 0:
                # Section 3: Number of Lights
                if MonitorDisplays[i] % 2 == 0:
                    Values[i] += len(MonitorLights[i])
                else:
                    Values[i] += 0 - len(MonitorLights[i])
        print("After Section 3: " + str(Values))
        
        for i in range(0, 15):
            # R G B P O W
            ColourOccurences = [0, 0, 0, 0, 0, 0]
            # Section 4: Colour of Lights
            for j in range(0, len(MonitorLights[i])):
                Values[i] += BLightValues[Orders.index(MonitorLights[i][j])][ColourOccurences[Orders.index(MonitorLights[i][j])]]
                ColourOccurences[Orders.index(MonitorLights[i][j])] += 1
                if Blinking[i][j]:
                    Values[i] += Blinkenlights[Orders.index(MonitorLights[i][j])][j]
                else:
                    Values[i] += RLightValues[Orders.index(MonitorLights[i][j])][j]
        print("After Section 4: " + str(Values))
        
        for i in range(0, 15):
            # Section 5: Connections
            WireOccurences = [0, 0, 0, 0, 0, 0]
            for j in range(0, len(MonitorConnections[i])):
                if MonitorConnections[i][j] == "R":
                    WireOccurences[0] += 1
                elif MonitorConnections[i][j] == "G":
                    WireOccurences[1] += 1
                elif MonitorConnections[i][j] == "B":
                    WireOccurences[2] += 1
                elif MonitorConnections[i][j] == "P":
                    WireOccurences[3] += 1
                elif MonitorConnections[i][j] == "O":
                    WireOccurences[4] += 1
                elif MonitorConnections[i][j] == "W":
                    WireOccurences[5] += 1
            print("Wire Occurences #" + str(i) + ": " + str(WireOccurences))
            for j in range(0, len(MonitorConnections[i])):
                if MonitorConnections[i][j] != "-":
                    Values[i] += WireValues[j][Orders.index(MonitorConnections[i][j])] * WireOccurences[Orders.index(MonitorConnections[i][j])]
        print("Final Values for each monitor: " + str(Values))
    print("The module should now solve, and that is the end. Goodbye - L.V.")
    exit()

if __name__ == "__main__":
    main()