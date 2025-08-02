Colours = ["Y", "A", "B", "G", "O", "R", "L", "C", "N", "W", "P", "M", "I"]
Keywords = [["WIRE"], ["BUTTON", "KEY"], ["MAZE"], ["SIMON"], ["MORSE"], ["CRUEL", "COMPLICATED", "BROKEN", "CURSED", "FAULTY"], ["MATH", "NUMBER", "DIGIT", "EQUATION", "LOGIC"], ["WORD", "LETTER", "PHRASE", "TEXT", "TALK", "ALPHABET"], ["CODE", "CIPHER"], ["LIGHT", "LED"], ["SQUARE", "CIRCLE", "TRIANGLE", "CUBE", "SPHERE"], ["COLOR", "COLOUR"], ["MELODY", "HARMONY", "CHORD", "PIANO"]]
Keys = [["A", "N", "0"], ["B", "O", "1"], ["C", "P", "2"], ["D", "Q", "3"], ["E", "R", "4"], ["F", "S", "5"], ["G", "T", "6"], ["H", "U", "7"], ["I", "V", "8"], ["J", "W", "9"], ["K", "X"], ["L", "Y"], ["M", "Z"]]

def main() -> None:
    global Colours
    global Keywords
    global Keys
    
    Counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Modifieds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Stages = []
    
    AACount = int(input("AA Battery Count: "))
    portPlateCount = int(input("Port Plate Count: "))
    bombTime = int(input("Starting Bomb Time (minutes): "))
    duplicatePortTypeCount = int(input("Port Types w/duplicates Count: "))
    moduleCount = int(input("Module Count: "))
    strikes = 0 # Get on submission
    serialNumber = input("Serial Number: ").upper()
    digitTotal = 0
    letterCount = 0
    for x in range(len(serialNumber)):
        if serialNumber[x] in "0123456789":
            digitTotal += int(serialNumber[x])
        else:
            letterCount += 1
    portTypeCount = int(input("Port Type Count: "))
    litIndicatorCount = int(input("Lit Indicator Count: "))
    unlitIndicatorCount = int(input("Unlit Indicator Count: "))
    DCount = int(input("D Battery Count: "))
    
    done = False
    stage = 1
    while not done:
        print("────────────────────Stage " + str(stage) + "────────────────────")
        content = input("Colours + Module Name: ").upper()
        if not validateInput(content):
            print("Incorrect input.")
            continue
        if content == "END":
            done = True
            continue

        content = content.split(" ")
        onNess = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        for i in range(len(content[0])):
            onNess[Colours.index(content[0][i])] = True
        
        moduleName = " ".join(content[1:])
        Stages.append(moduleName)
        faulty = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        for i in range(len(Keywords)):
            for j in range(len(Keywords[i])):
                if Keywords[i][j] in moduleName != -1:
                    faulty[i] = True
        
        faultyLog = ""
        for i in range(len(faulty)):
            if faulty[i]:
                faultyLog += Colours[i]
        print("Faulty: " + faultyLog)
        
        for i in range(len(onNess)):
            onNess[i] ^= faulty[i]
        
        onLog = ""
        
        for i in range(len(onNess)):
            if onNess[i]:
                onLog += Colours[i]
                Counts[i] += 1
        
        print("Post-Inversion: " + onLog)
        
        stage += 1
    
    print("────────────────────FINAL────────────────────")
    strikes = int(input("Strike Count: "))
    Modifieds = [AACount, portPlateCount, bombTime, duplicatePortTypeCount, moduleCount, strikes, digitTotal, letterCount, portTypeCount, litIndicatorCount, Counts[Colours.index("P")], unlitIndicatorCount, DCount]
    
    for i in range(len(Colours)):
        print(Colours[i] + " count: " + str(Counts[i]))
        Totals[i] = Counts[i] * Modifieds[i]
        print("Final " + Colours[i] + " value: " + str(Totals[i]))
    
    finalTotal = SignedModulo(sum(Totals) - 1, len(Stages))
    print("Requested Stage " + str(finalTotal + 1) + ": " + Stages[finalTotal])
    requiredStage = removeDuplicates(Stages[finalTotal].replace(" ", ""))
    
    hasCut = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    cutOrder = []
    for i in range(len(requiredStage)):
        for j in range(len(Keys)):
            if requiredStage[i] in Keys[j] != -1 and not hasCut[j]:
                hasCut[j] = True
                cutOrder.append(Colours[j])
    print("Cut the wires in the following order: " + " ".join(cutOrder))

def SignedModulo(m: int, n: int) -> int:
    return (abs(m) % n)*(-1 if m < 0 else 1)

def removeDuplicates(x: str) -> str:
    res = ""
    for i in range(len(x)):
        if x[i] not in res:
            res += x[i]
    return res

def validateInput(string: str) -> bool:
    global Colours
    
    if string == "END":
        return True
    
    thing = string.split(" ")
    for i in range(len(thing[0])):
        if thing[0][i] not in Colours:
            return False
    
    return True

if __name__ == "__main__":
    main()