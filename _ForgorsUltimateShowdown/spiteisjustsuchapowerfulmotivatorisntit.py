import math

PossibleMethods = ["FMN", "SS", "FML", "FI", "AND", "FMW", "FE", "FUN"]
CWPositions = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]


def main() -> None:
    global PossibleMethods
    global CWPositions
    
    print("Possible Method names in manual order: " + ", ".join(PossibleMethods))
    
    unencryptedString = list(input("Enter the top 12-digit number: "))
    unencryptedNumbers = [int(x) for x in unencryptedString]
    supplementaryString = list(input("Enter the bottom 12-digit number: "))
    supplementaryNumbers = [int(x) for x in supplementaryString]
    thirdDigitBinary = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]
    FMWValues = [[0.2, 0.4, 0.6, 0.6, 1, 1, 1.4, 1.4, 2, 2, 2.4, 2.4], [8, 12, 16, 16, 16, 20, 20, 20, 24, 24, 24, 32], [3, 4, 9, 6, 1, 9, 7, 4, 9, 1, 7, 9]]
    
    methods = input("Input the four methods on the module, in order: ").upper().split(" ")
    for i in range(0, len(methods)):
        print("----------------------------------<ENCRYPTION #" + str(i + 1) + ">----------------------------------")
        if methods[i] == "FMN":
            largestSN = int(input("What is the largest digit in the serial number? "))
            smallestOdd = int(input("What is the smallest odd digit in the Serial Number? "))
            for j in range(0, len(unencryptedNumbers)):
                if j == 0:
                    if input("Does the bomb have an unlit CAR indicator? ").upper() == "Y":
                        unencryptedNumbers[j] += 2
                    elif input("Does the bomb have more unlit than lit indicators? ").upper() == "Y":
                        unencryptedNumbers[j] += 7
                    elif input("Are there no unlit indicators? ").upper() == "Y":
                        unencryptedNumbers[j] += int(input("How many lit indicators are there? "))
                    else:
                        unencryptedNumbers[j] += int(input("What is the last digit of the Serial Number? "))
                elif j == 1:
                    if input("Does the bomb have a Serial port? ").upper() == "Y" and input("Are there 3 or more digits in the Serial Number? ").upper() == "Y":
                        unencryptedNumbers[j] += 3
                    elif unencryptedNumbers[j - 1] % 2 == 0:
                        unencryptedNumbers[j] += unencryptedNumbers[j - 1] + 1
                    else:
                        unencryptedNumbers[j] += unencryptedNumbers[j - 1] - 1
                else:
                    if unencryptedNumbers[j - 1] == 0 or unencryptedNumbers[j - 2] == 0:
                        unencryptedNumbers[j] += largestSN
                    elif unencryptedNumbers[j - 1] % 2 == 0 and unencryptedNumbers[j - 2] % 2 == 0:
                        unencryptedNumbers[j] += smallestOdd
                    else:
                        if unencryptedNumbers[j - 1] + unencryptedNumbers[j - 2] > 9:
                            unencryptedNumbers[j] += 1
                        else:
                            unencryptedNumbers[j] += unencryptedNumbers[j - 1] + unencryptedNumbers[j - 2]
                unencryptedNumbers[j] %= 10
        elif methods[i] == "SS":
            lastDigit = int(input("What is the last digit in the serial number? "))
            numArray = [lastDigit, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(1, len(numArray)):
                lastDigit = (lastDigit + 1) % 10
                numArray[CWPositions[j]] = lastDigit
            rule = input("What is the colour rule? ").upper()
            if rule == "B":
                unencryptedNumbers.reverse()
            elif rule == "I":
                for j in range(0, len(unencryptedNumbers)):
                    unencryptedNumbers[j] = numArray[(numArray.index(unencryptedNumbers[j]) + 5) % 10]
            elif rule == "L":
                for j in range(0, len(unencryptedNumbers)):
                    unencryptedNumbers[j] = numArray[(numArray.index(unencryptedNumbers[j]) + 5) % 10]
                unencryptedNumbers.reverse()
            elif rule == "C":
                unencryptedNumbers[0] = numArray[(numArray.index(unencryptedNumbers[0]) + 5) % 10]
                unencryptedNumbers[11] = numArray[(numArray.index(unencryptedNumbers[11]) + 5) % 10]
            elif rule == "W":
                unencryptedNumbers[2] = numArray[(numArray.index(unencryptedNumbers[2]) + 5) % 10]
                unencryptedNumbers[1] = numArray[(numArray.index(unencryptedNumbers[1]) + 5) % 10]
            unencryptedNumbers[j] %= 10
        elif methods[i] == "FML":
            functionString = input("What is the sequence of functions? ").split(" ")
            functionSequence = [int(x) for x in functionString]
            lastInput = 0
            secondLastInput = 0
            for j in range(0, len(unencryptedNumbers)):
                if j == 0:
                    lastInput = unencryptedNumbers[j]
                    secondLastInput = unencryptedNumbers[j]
                elif j == 1:
                    lastInput = unencryptedNumbers[j - 1]
                    secondLastInput = unencryptedNumbers[j]
                else:
                    lastInput = unencryptedNumbers[j - 1]
                    secondLastInput = unencryptedNumbers[j - 2]
                if functionSequence[j] == 0:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j]) % 10
                elif functionSequence[j] == 1:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + 1) % 10
                elif functionSequence[j] == 2:
                    unencryptedNumbers[j] += abs((supplementaryNumbers[j] * 2)) % 10
                elif functionSequence[j] == 3:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + lastInput) % 10
                elif functionSequence[j] == 4:
                    unencryptedNumbers[j] += abs((lastInput - supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 5:
                    unencryptedNumbers[j] += abs(lastInput - secondLastInput) % 10
                elif functionSequence[j] == 6:
                    unencryptedNumbers[j] += abs((secondLastInput - supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 7:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + lastInput + 1) % 10
                elif functionSequence[j] == 8:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + secondLastInput + 1) % 10
                elif functionSequence[j] == 9:
                    unencryptedNumbers[j] += abs(lastInput + secondLastInput + 1) % 10
                elif functionSequence[j] == 10:
                    unencryptedNumbers[j] += abs(lastInput) % 10
                elif functionSequence[j] == 11:
                    unencryptedNumbers[j] += abs(lastInput + 1) % 10
                elif functionSequence[j] == 12:
                    unencryptedNumbers[j] += abs((lastInput * 2)) % 10
                elif functionSequence[j] == 13:
                    unencryptedNumbers[j] += abs(lastInput + secondLastInput) % 10
                elif functionSequence[j] == 14:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] - 1) % 10
                elif functionSequence[j] == 15:
                    unencryptedNumbers[j] += abs(lastInput - 1) % 10
                elif functionSequence[j] == 16:
                    unencryptedNumbers[j] += abs(secondLastInput - 1) % 10
                elif functionSequence[j] == 17:
                    unencryptedNumbers[j] += abs(lastInput + supplementaryNumbers[j] - 1) % 10
                elif functionSequence[j] == 18:
                    unencryptedNumbers[j] += abs(secondLastInput + supplementaryNumbers[j] - 1) % 10
                elif functionSequence[j] == 19:
                    unencryptedNumbers[j] += abs(lastInput + secondLastInput - 1) % 10
                elif functionSequence[j] == 20:
                    unencryptedNumbers[j] += abs(secondLastInput) % 10
                elif functionSequence[j] == 21:
                    unencryptedNumbers[j] += abs(secondLastInput + 1) % 10
                elif functionSequence[j] == 22:
                    unencryptedNumbers[j] += abs((secondLastInput * 2)) % 10
                elif functionSequence[j] == 23:
                    unencryptedNumbers[j] += abs(secondLastInput + supplementaryNumbers[j]) % 10
                elif functionSequence[j] == 24:
                    unencryptedNumbers[j] += abs((lastInput + secondLastInput) * 2) % 10
                elif functionSequence[j] == 25:
                    unencryptedNumbers[j] += abs((lastInput + supplementaryNumbers[j]) * 2) % 10
                elif functionSequence[j] == 26:
                    unencryptedNumbers[j] += abs((secondLastInput + supplementaryNumbers[j]) * 2) % 10
                elif functionSequence[j] == 27:
                    unencryptedNumbers[j] += abs(abs(lastInput - secondLastInput) * 2) % 10
                elif functionSequence[j] == 28:
                    unencryptedNumbers[j] += abs(abs(lastInput - supplementaryNumbers[j]) * 2) % 10
                elif functionSequence[j] == 29:
                    unencryptedNumbers[j] += abs(abs(secondLastInput - supplementaryNumbers[j]) * 2) % 10
                elif functionSequence[j] == 30:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] * 3) % 10
                elif functionSequence[j] == 31:
                    unencryptedNumbers[j] += abs(lastInput * 3) % 10
                elif functionSequence[j] == 32:
                    unencryptedNumbers[j] += abs(secondLastInput * 3) % 10
                elif functionSequence[j] == 33:
                    unencryptedNumbers[j] += abs((lastInput + secondLastInput) * 3) % 10
                elif functionSequence[j] == 34:
                    unencryptedNumbers[j] += abs(secondLastInput + (3 * lastInput)) % 10
                elif functionSequence[j] == 35:
                    unencryptedNumbers[j] += abs(lastInput + (3 * supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 36:
                    unencryptedNumbers[j] += abs(secondLastInput + (3 * supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 37:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + (3 * lastInput)) % 10
                elif functionSequence[j] == 38:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + (3 * secondLastInput)) % 10
                elif functionSequence[j] == 39:
                    unencryptedNumbers[j] += abs(lastInput + (3 * secondLastInput)) % 10
                elif functionSequence[j] == 40:
                    unencryptedNumbers[j] += abs(5 + supplementaryNumbers[j]) % 10
                elif functionSequence[j] == 41:
                    unencryptedNumbers[j] += abs(5 + lastInput) % 10
                elif functionSequence[j] == 42:
                    unencryptedNumbers[j] += abs(5 + secondLastInput) % 10
                elif functionSequence[j] == 43:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + (2 * lastInput)) % 10
                elif functionSequence[j] == 44:
                    unencryptedNumbers[j] += abs(supplementaryNumbers[j] + (2 * secondLastInput)) % 10
                elif functionSequence[j] == 45:
                    unencryptedNumbers[j] += abs(lastInput + (2 * supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 46:
                    unencryptedNumbers[j] += abs(secondLastInput + (2 * supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 47:
                    unencryptedNumbers[j] += abs(abs(secondLastInput - (2 * lastInput))) % 10
                elif functionSequence[j] == 48:
                    unencryptedNumbers[j] += abs(abs(supplementaryNumbers[j] - (2 * lastInput))) % 10
                elif functionSequence[j] == 49:
                    unencryptedNumbers[j] += abs(abs(lastInput - (2 * secondLastInput))) % 10
                elif functionSequence[j] == 50:
                    unencryptedNumbers[j] += abs(9 - supplementaryNumbers[j]) % 10
                elif functionSequence[j] == 51:
                    unencryptedNumbers[j] += abs(9 - lastInput) % 10
                elif functionSequence[j] == 52:
                    unencryptedNumbers[j] += abs(9 - secondLastInput) % 10
                elif functionSequence[j] == 53:
                    unencryptedNumbers[j] += abs(18 - (supplementaryNumbers[j] + lastInput)) % 10
                elif functionSequence[j] == 54:
                    unencryptedNumbers[j] += abs(18 - (supplementaryNumbers[j] + secondLastInput)) % 10
                elif functionSequence[j] == 55:
                    unencryptedNumbers[j] += abs(18 - (lastInput + secondLastInput)) % 10
                elif functionSequence[j] == 56:
                    unencryptedNumbers[j] += abs(18 - (2 * supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 57:
                    unencryptedNumbers[j] += abs(9 - abs(lastInput - supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 58:
                    unencryptedNumbers[j] += abs(9 - abs(secondLastInput - supplementaryNumbers[j])) % 10
                elif functionSequence[j] == 59:
                    unencryptedNumbers[j] += abs(9 - abs(secondLastInput - lastInput)) % 10
                unencryptedNumbers[j] %= 10
        elif methods[i] == "FI":
            lastDigit = int(input("What is the last digit in the serial number? "))
            positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            leftovers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            leftstr = []
            for j in range(0, len(leftovers)):
                leftovers[j] = unencryptedNumbers[j]
                leftstr = [str(x) for x in unencryptedNumbers]
            ignoreList = [(int(x) - 1) for x in input("Input the two positions to ignore: ").split(" ")]
            positions.remove(ignoreList[0])
            positions.remove(ignoreList[1])
            itemsRemoved = [unencryptedNumbers[ignoreList[0]], unencryptedNumbers[ignoreList[1]]]
            leftstr[ignoreList[0]] = "-"
            leftstr[ignoreList[1]] = "-"
            swap = False
            Original = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            FINumbers = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            count = 0
            ix = 0
            for digit in leftstr:
                if digit != "-":
                    FINumbers[ix][count] = int(digit)
                    Original[ix][count] = int(digit)
                    count += 1
                    if count == 5:
                        count = 0
                        ix = 1
            print("Groups: " + "".join([str(x) for x in FINumbers[0]]) + ", " + "".join([str(x) for x in FINumbers[1]]))
            if input("Is there an RCA port? ").upper() == "Y":
                swap = True
                swap_int(FINumbers[0], 0, 4)
                swap_int(FINumbers[0], 1, 3)
                swap_int(FINumbers[1], 0, 4)
                swap_int(FINumbers[1], 1, 3)
            batteryCount = int(input("Input the number of batteries on the bomb: "))
            for j in range(0, 2):
                for k in range(0, 5):
                    FINumbers[j][k] += batteryCount
            serialNumber = input("Input the bomb's Serial Number: ").upper()
            charCount = 0
            if (("F" in serialNumber) or ("I" in serialNumber)):
                for j in range(0, len(serialNumber)):
                    if serialNumber[j] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        charCount += 1
                for j in range(0, 2):
                    for k in range(0, 5):
                        FINumbers[j][k] -= charCount
            needyTetris = True if input("Is there a Needy Tetris present? ").upper() == "Y" else False
            ports = True if input("Are there ports on the bomb? ").upper() == "Y" else False
            duplicatePorts = False
            duplicatePortTypes = 0
            numPorts = 0
            if ports:
                numPorts = int(input("Input the number of ports on the bomb: "))
                duplicatePorts = True if input("Are there duplicate ports on the bomb? ").upper() == "Y" else False
            if duplicatePorts:
                duplicatePortTypes = int(input("Input the number of duplicate port types on the bomb: "))
            smallestSN = int(input("Input the smallest digit in the Serial Number: "))
            largestSN = int(input("Input the largest digit in the Serial Number: "))
            firstSN = int(input("Input the first digit in the Serial Number: "))
            for j in range(0, 2):
                # Digit 1
                if needyTetris:
                    FINumbers[j][0] = Original[j][0] + 7
                elif (FINumbers[j][0] > 9) and (FINumbers[j][0] % 2 == 0):
                    FINumbers[j][0] = int(FINumbers[j][0] / 2)
                elif FINumbers[j][0] < 5:
                    FINumbers[j][0] += lastDigit
                else:
                    FINumbers[j][0] += 1
                
                # Digit 2
                if duplicatePorts:
                    FINumbers[j][1] += duplicatePortTypes
                elif not ports:
                    FINumbers[j][1] += Original[j][2] + Original[j][0]
                else:
                    FINumbers[j][1] += numPorts
                
                # Digit 3
                if not swap:
                    if FINumbers[j][2] > 6:
                        FINumbers[j][2] = thirdDigitBinary[Original[j][2]]
                    elif FINumbers[j][2] < 3:
                        FINumbers[j][2] = abs(FINumbers[j][2])
                    else:
                        FINumbers[j][2] = Original[j][2] + smallestSN
                
                # Digit 4
                if FINumbers[j][3] < 0:
                    FINumbers[j][3] += largestSN
                
                # Digit 5
                if math.floor(firstSN / 2) == 0:
                    if FINumbers[j][4] % 5 == 0:
                        FINumbers[j][4] = 0
                    elif FINumbers[j][4] % 5 == 1:
                        FINumbers[j][4] = 5
                    elif FINumbers[j][4] % 5 == 2:
                        FINumbers[j][4] = Original[j][4]
                    elif FINumbers[j][4] % 5 == 3:
                        FINumbers[j][4] = 9
                    else:
                        FINumbers[j][4] = 4
                elif math.floor(firstSN / 2) == 1:
                    if FINumbers[j][4] % 5 == 0:
                        FINumbers[j][4] = 1
                    elif FINumbers[j][4] % 5 == 1:
                        FINumbers[j][4] = 6
                    elif FINumbers[j][4] % 5 == 2:
                        FINumbers[j][4] = Original[j][4] + 1
                    elif FINumbers[j][4] % 5 == 3:
                        FINumbers[j][4] = 8
                    else:
                        FINumbers[j][4] = 3
                elif math.floor(firstSN / 2) == 2:
                    if FINumbers[j][4] % 5 == 0:
                        FINumbers[j][4] = 2
                    elif FINumbers[j][4] % 5 == 1:
                        FINumbers[j][4] = 7
                    elif FINumbers[j][4] % 5 == 2:
                        FINumbers[j][4] = 9 - Original[j][4]
                    elif FINumbers[j][4] % 5 == 3:
                        FINumbers[j][4] = 5
                    else:
                        FINumbers[j][4] = 0
                elif math.floor(firstSN / 2) == 3:
                    if FINumbers[j][4] % 5 == 0:
                        FINumbers[j][4] = 3
                    elif FINumbers[j][4] % 5 == 1:
                        FINumbers[j][4] = 8
                    elif FINumbers[j][4] % 5 == 2:
                        FINumbers[j][4] = Original[j][4] - 1
                    elif FINumbers[j][4] % 5 == 3:
                        FINumbers[j][4] = 6
                    else:
                        FINumbers[j][4] = 1
                elif math.floor(firstSN / 2) == 4:
                    if FINumbers[j][4] % 5 == 0:
                        FINumbers[j][4] = 4
                    elif FINumbers[j][4] % 5 == 1:
                        FINumbers[j][4] = 9
                    elif FINumbers[j][4] % 5 == 2:
                        FINumbers[j][4] = Original[j][4] + 5
                    elif FINumbers[j][4] % 5 == 3:
                        FINumbers[j][4] = 7
                    else:
                        FINumbers[j][4] = 2
            for j in range(0, 2):
                for k in range(0, 5):
                    FINumbers[j][k] %= 10
            print("Final FI Answers: " + "".join([str(x) for x in FINumbers[0]]) + ", " + "".join([str(x) for x in FINumbers[1]]))
            unencryptedNumbers[ignoreList[0]] = itemsRemoved[0]
            unencryptedNumbers[ignoreList[1]] = itemsRemoved[1]
            for j in range(0, 10):
                unencryptedNumbers[positions[j]] = FINumbers[math.floor(j / 5)][j % 5]
        elif methods[i] == "AND":
            names = ["AND", "OR", "XOR", "NAND", "NOR", "XNOR", "R_ARR", "L_ARR", "NOT"]
            print("Possible names for gates are: " + ", ".join(names))
            sequence = input("Input the sequence of 12 logic gates: ").upper().split(" ")
            Not = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
            for j in range(0, 12):
                if sequence[j] == "AND":
                    unencryptedNumbers[j] = unencryptedNumbers[j] & supplementaryNumbers[j]
                elif sequence[j] == "OR":
                    unencryptedNumbers[j] = unencryptedNumbers[j] | supplementaryNumbers[j]
                elif sequence[j] == "XOR":
                    unencryptedNumbers[j] = unencryptedNumbers[j] ^ supplementaryNumbers[j]
                elif sequence[j] == "NOT":
                    unencryptedNumbers[j] = Not[unencryptedNumbers[j]]
                else:
                    unenc = str(bin(unencryptedNumbers[j]))
                    unenc = unenc.replace("0b", "")
                    suppl = str(bin(supplementaryNumbers[j]))
                    suppl = suppl.replace("0b", "")
                    result = ""
                    resultNum = 0
                    while len(unenc) != 4:
                        unenc = "0" + unenc
                    while len(suppl) != 4:
                        suppl = "0" + suppl
                    if sequence[j] == "NAND":
                        for k in range(0, 4):
                            if unenc[k] == "1" and suppl[k] == "1":
                                result += "0"
                            else:
                                result += "1"
                        for k in range(0, 4):
                            resultNum += int(result[k]) * (2 ** (3 - k))
                        unencryptedNumbers[j] = resultNum
                    elif sequence[j] == "NOR":
                        for k in range(0, 4):
                            if unenc[k] == "0" and suppl[k] == "0":
                                result += "1"
                            else:
                                result += "0"
                        for k in range(0, 4):
                            resultNum += int(result[k]) * (2 ** (3 - k))
                        unencryptedNumbers[j] = resultNum
                    elif sequence[j] == "XNOR":
                        for k in range(0, 4):
                            if (unenc[k] == "1" and suppl[k] == "0") or (unenc[k] == "0" and suppl[k] == "1"):
                                result += "0"
                            else:
                                result += "1"
                        for k in range(0, 4):
                            resultNum += int(result[k]) * (2 ** (3 - k))
                        unencryptedNumbers[j] = resultNum
                    elif sequence[j] == "IMP_L":
                        for k in range(0, 4):
                            if unenc[k] == "1" and suppl[k] == "0":
                                result += "0"
                            else:
                                result += "1"
                        for k in range(0, 4):
                            resultNum += int(result[k]) * (2 ** (3 - k))
                        unencryptedNumbers[j] = resultNum
                    elif sequence[j] == "IMP_R":
                        for k in range(0, 4):
                            if unenc[k] == "0" and suppl[k] == "1":
                                result += "0"
                            else:
                                result += "1"
                        for k in range(0, 4):
                            resultNum += int(result[k]) * (2 ** (3 - k))
                        unencryptedNumbers[j] = resultNum
                if (j + 1) % 2 == 0:
                    unencryptedNumbers[j] %= 10
                else:
                    if unencryptedNumbers[j] != 0:
                        unencryptedNumbers[j] = unencryptedNumbers[j] % 9
                        if unencryptedNumbers[j] == 0:
                            unencryptedNumbers[j] = 9
        elif methods[i] == "FMW":
            firstDigit = int(input("Input the first digit of the Serial Number: "))
            secondToLastCalc = int(input("Input the last digit of the Serial Number: "))
            number = int(input("Input the number displayed on the method: "))
            lastCalc = ((number - 1) % 9) + 1
            for j in range(0, len(unencryptedNumbers)):
                if j == 1:
                    secondToLastCalc = lastCalc
                    lastCalc = unencryptedNumbers[j - 1]
                elif j > 1:
                    secondToLastCalc = unencryptedNumbers[j - 2]
                    lastCalc = unencryptedNumbers[j - 1]
                if secondToLastCalc == 0 or lastCalc == 0:
                    unencryptedNumbers[j] += math.ceil(FMWValues[0][j] * firstDigit)
                elif secondToLastCalc % 2 == 0 and lastCalc % 2 == 0:
                    unencryptedNumbers[j] += abs(FMWValues[1][j] - 12)
                else:
                    unencryptedNumbers[j] += FMWValues[2][j] + lastCalc + secondToLastCalc
                unencryptedNumbers[j] %= 10
        elif methods[i] == "FE":
            rule = input("What is the true LED colour to be used for Forget Everything? ").upper()
            if rule == "R":
                for j in range(0, len(unencryptedNumbers)):
                    unencryptedNumbers[j] = supplementaryNumbers[j] + unencryptedNumbers[j]
                    unencryptedNumbers[j] %= 10
            elif rule == "Y":
                for j in range(0, len(unencryptedNumbers)):
                    unencryptedNumbers[j] = supplementaryNumbers[j] - unencryptedNumbers[j]
                    unencryptedNumbers[j] %= 10
            elif rule == "G":
                for j in range(0, len(unencryptedNumbers)):
                    unencryptedNumbers[j] = supplementaryNumbers[j] + unencryptedNumbers[j] + 5
                    unencryptedNumbers[j] %= 10
            elif rule == "B":
                for j in range(0, len(unencryptedNumbers)):
                    unencryptedNumbers[j] = unencryptedNumbers[j] - supplementaryNumbers[j]
                    unencryptedNumbers[j] %= 10
        elif methods[i] == "FUN":
            o = input("Input the numbers cycling on the display: ").split(" ")
            order = [(int(x) - 1) for x in o]
            triplets = []
            fst = [False, False, False]
            batteryCount = int(input("How many batteries are there? "))
            for j in range(0, len(unencryptedNumbers)):
                triplets.append([unencryptedNumbers[0], unencryptedNumbers[1], unencryptedNumbers[2]])
                unencryptedNumbers[:] = unencryptedNumbers[1:] + unencryptedNumbers[:1]
            if input("Are there 4 letters and 2 numbers in the Serial Number? ").upper() == "Y":
                fst[0] = True
                for j in range(0, len(triplets)):
                    triplets[j][0] = abs(triplets[j][0] - batteryCount)
            elif input("Are there 3 letters and 3 numbers in the Serial Number? ").upper() == "Y":
                fst[1] = True
                for j in range(0, len(triplets)):
                    triplets[j][1] = abs(triplets[j][1] - batteryCount)
            elif input("Are there 2 letters and 4 numbers in the Serial Number? ").upper() == "Y":
                fst[2] = True
                for j in range(0, len(triplets)):
                    triplets[j][2] = abs(triplets[j][2] - batteryCount)
            if fst[0] == True:
                for j in range(0, len(triplets)):
                    secondary = abs(triplets[j][1] - triplets[j][2])
                    unencryptedNumbers[order[j]] = (triplets[j][0] + secondary) % 10
            elif fst[1] == True:
                for j in range(0, len(triplets)):
                    secondary = abs(triplets[j][0] - triplets[j][2])
                    unencryptedNumbers[order[j]] = (triplets[j][1] + secondary) % 10
            elif fst[2] == True:
                for j in range(0, len(triplets)):
                    secondary = abs(triplets[j][0] - triplets[j][1])
                    unencryptedNumbers[order[j]] = (triplets[j][2] + secondary) % 10
        print("After Encryption #" + str(i + 1) + ": " + "".join([str(x) for x in unencryptedNumbers]))

def swap_int(l: list, a: int, b: int) -> None:
    """A method for swapping two strings in a list by using their indexes."""
    l[a], l[b] = l[b], l[a]  # Note: these small functions help reduce code size

if __name__ == "__main__":
    main()