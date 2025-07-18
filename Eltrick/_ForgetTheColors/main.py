import math

COLORS = ["R", "O", "Y", "G", "C", "B", "P", "I", "M", "W"]
STAGES = []
end = False

def main() -> None:
    global COLORS
    global STAGES
    global end
    
    print("----------------------------------<EDGEWORK_INFORMATION>----------------------------------")
    batteryCount = int(input("Number of batteries? "))
    portCount = int(input("Number of ports? "))
    SerialNumberLastDigit = int(input("Serial Number's last digit? "))
    portPlateCount = int(input("Number of port plates? "))
    moduleCount = int(input("Number of modules? "))
    batteryHolderCount = int(input("Number of battery holders? "))
    litIndicatorCount = int(input("Number of lit indicators? "))
    unlitIndicatorCount = int(input("Number of unlit indicators? "))
    totalIndicatorCount = litIndicatorCount + unlitIndicatorCount

    print("--------------------------------------<START_MODULE>--------------------------------------")
    
    stage = 0
    solveCount = -1;
    
    while not end:
        solveCount += 1
        print("Current Solve Count: " + str(solveCount))
        stageInfo = input("Enter stage " + str(stage) + "'s information in the order shown: ").upper().split(" ")
        infoValid = infoValidator(stageInfo)
        while not infoValid:
            stageInfo = input("Invalid information entered. Try again: ").upper().split(" ")
            infoValid = infoValidator(stageInfo)
        
        if(stageInfo[0] == "QSKIP"):
            continue
        
        nixieValues = [int(x) for x in stageInfo[4]]
        
        stageCylinders = [x for x in stageInfo[1]]
        for stageCylinder in stageCylinders:
            if stageCylinder == "R":
                nixieValues[0] += 5
                nixieValues[1] -= 1
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "O":
                nixieValues[0] -= 1
                nixieValues[1] -= 6
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "Y":
                nixieValues[0] += 3
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "G":
                nixieValues[0] += 7
                nixieValues[1] -= 4
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "C":
                nixieValues[0] -= 7
                nixieValues[1] -= 5
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "B":
                nixieValues[0] += 8
                nixieValues[1] += 9
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "P":
                nixieValues[0] += 5
                nixieValues[1] -= 9
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "I":
                nixieValues[0] -= 9
                nixieValues[1] += 4
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            elif stageCylinder == "M":
                nixieValues[1] += 7
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
            else:
                nixieValues[0] -= 3
                nixieValues[1] += 5
                print("The nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))

        nixieValues[0] %= 10;
        nixieValues[1] %= 10;
        print("Finally, the nixie pair is now " + str(nixieValues[0]) + ", " + str(nixieValues[1]))
        
        edgeworkTemp = nixieValues[0] + nixieValues[1] + int(stageInfo[2])
        edgeworkRule = (COLORS.index(stageInfo[3]) - nixieValues[0] + nixieValues[1]) % 10
        
        if edgeworkRule == 0:
            edgeworkTemp += batteryCount
        elif edgeworkRule == 1:
            edgeworkTemp -= portCount
        elif edgeworkRule == 2:
            edgeworkTemp += SerialNumberLastDigit
        elif edgeworkRule == 3:
            edgeworkTemp -= solveCount
        elif edgeworkRule == 4:
            edgeworkTemp += portPlateCount
        elif edgeworkRule == 5:
            edgeworkTemp -= moduleCount
        elif edgeworkRule == 6:
            edgeworkTemp += batteryHolderCount
        elif edgeworkRule == 7:
            edgeworkTemp -= litIndicatorCount
        elif edgeworkRule == 8:
            edgeworkTemp += totalIndicatorCount
        elif edgeworkRule == 9:
            edgeworkTemp -= unlitIndicatorCount
        
        edgeworkTemp %= 10
        print("The third digit of the number is: " + str(edgeworkTemp))
        
        calculatedNumber = int(str(nixieValues[0]) + str(nixieValues[1]) + str(edgeworkTemp))
        print("So, the modified three digit number is: " + str(calculatedNumber))
        displayedNumber = int(stageInfo[0])
        
        sinAns = math.trunc(math.sin(calculatedNumber * math.pi / 180) * 100000)
        
        if sinAns < 0:
            sinAns %= 100000
            sinAns -= 100000
        else:
            sinAns %= 100000
        
        cosAns = math.trunc(abs(math.cos(displayedNumber * math.pi/180)) * 100000) % 100000
        
        if abs(sinAns) % 1000 == 999:
            if sinAns > 0:
                sinAns = (sinAns + 1) % 100000
            else:
                sinAns = (sinAns - 1) % 100000
                sinAns -= 100000
        
        if abs(cosAns) % 1000 == 999:
            cosAns = (cosAns + 1) % 100000
        
        print("Sine = " + str(sinAns))
        print("Absolute Cosine = " + str(cosAns))
        
        answer = sinAns + cosAns
        print("Answer = " + str(answer))
        STAGES.append(answer)
        
        stage += 1
        print("----------------------------------------<NEW_STAGE>----------------------------------------")

def infoValidator(stageInfo: list) -> bool:
    if stageInfo[0].upper() == "END":
        print("------------------------------------------<FINAL>------------------------------------------")
        print("Initially, the calculated values of each stage are: " + str(STAGES))
        
        finalSum = sum(STAGES);
        print("Therefore, the sum of all stages is: " + str(finalSum))
        
        finalSum = abs(finalSum / 100000) % 1
        
        print("Therefore, the sum of all values are: " + str(finalSum))
        finalAnswer = math.floor(math.acos(finalSum)/math.pi * 180)
        print("And so, the Final Answer is: " + str(finalAnswer))
        print("And that is The End! Congratulations! - L.V.")
        exit();
    elif stageInfo[0].upper() == "QSKIP":
        return True;
    elif len(stageInfo) != 5:
        print("Expected five parameters.")
        return False;
    else:
        if len(stageInfo[0]) != 3 or stageInfo[0][0] not in "0123456789" or stageInfo[0][1] not in "0123456789" or stageInfo[0][2] not in "0123456789":
            print("Expected three-digit display number as first parameter.")
            return False;
        if len(stageInfo[1]) != 3 or stageInfo[1][0] not in "ROYGCBPIMW" or stageInfo[1][1] not in "ROYGCBPIMW" or stageInfo[1][2] not in "ROYGCBPIMW":
            print("Expected three-letter cylinder colours as second parameter.")
            return False;
        if len(stageInfo[2]) != 1 or stageInfo[2] not in "0123456789":
            print("Expected gear number shown as third parameter.")
            return False;
        if len(stageInfo[3]) != 1 or stageInfo[3] not in "ROYGCBPIMW":
            print("Expected gear colour shown as fourth parameter.")
            return False;
        if len(stageInfo[4]) != 2 or stageInfo[4][0] not in "0123456789" or stageInfo[4][1] not in "0123456789":
            print("Expected nixies shown as fifth parameter.")
            return False;
    return True;

if __name__ == '__main__':
    main()
