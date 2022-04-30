import random

def main() -> None:
    trials = []
    digits = []
    possibleNumbers = []
    
    number = input("Input number string: ")
    for i in range(0, len(number)):
        digits.append(int(number[i]))
    for i in range(1, 10):
        if (i in digits) and (i % digits[0] == 0):
            trials.append(i)
    for i in range(0, len(digits)):
        possibleNumbers.append(digits[i])
    
    notDone = True
    while notDone:
        random.shuffle(possibleNumbers)
        if int(str(possibleNumbers[0])) % digits[0] == 0:
            if int(str(possibleNumbers[0]) + str(possibleNumbers[1])) % digits[1] == 0:
                if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2])) % digits[2] == 0:
                    if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3])) % digits[3] == 0:
                        if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3]) + str(possibleNumbers[4])) % digits[4] == 0:
                            if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3]) + str(possibleNumbers[4]) + str(possibleNumbers[5])) % digits[5] == 0:
                                if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3]) + str(possibleNumbers[4]) + str(possibleNumbers[5]) + str(possibleNumbers[6])) % digits[6] == 0:
                                    if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3]) + str(possibleNumbers[4]) + str(possibleNumbers[5]) + str(possibleNumbers[6]) + str(possibleNumbers[7])) % digits[7] == 0:
                                        if int(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3]) + str(possibleNumbers[4]) + str(possibleNumbers[5]) + str(possibleNumbers[6]) + str(possibleNumbers[7]) + str(possibleNumbers[8])) % digits[8] == 0:
                                            print(str(possibleNumbers[0]) + str(possibleNumbers[1]) + str(possibleNumbers[2]) + str(possibleNumbers[3]) + str(possibleNumbers[4]) + str(possibleNumbers[5]) + str(possibleNumbers[6]) + str(possibleNumbers[7]) + str(possibleNumbers[8]))
                                            notDone = False

if __name__ == "__main__":
    main()

