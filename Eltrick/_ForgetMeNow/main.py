import math

def main() -> None:
    debug = False

    FMWValues = [[0.2, 0.4, 0.6, 0.6, 1, 1, 1.4, 1.4, 2, 2, 2.4, 2.4, 3, 3, 3, 3, 3, 3, 3, 3], [8, 12, 16, 16, 16, 20, 20, 20, 24, 24, 24, 32, 32, 32, 40, 40, 40, 40, 48, 48], [3, 4, 9, 6, 1, 9, 7, 4, 9, 1, 7, 9, 5, 6, 9, 8, 0, 9, 0, 0]]
    unencryptedNumbers = [int(x) for x in list(input("Enter funny number string: "))]
    unencryptedArray = [str(x) for x in unencryptedNumbers]
    print("Number of stages: " + str(len(unencryptedArray)))
    firstDigit = int(input("Input the first digit of the Serial Number: ")) % 10
    secondToLastCalc = int(input("Input the last digit of the Serial Number: ")) % 10
    lastCalc = int(input("Number pressed to activate module: ")) % 10
    for j in range(0, len(unencryptedNumbers)):
        if j == 1:
            secondToLastCalc = lastCalc
            lastCalc = unencryptedNumbers[j - 1]
        elif j > 1:
            secondToLastCalc = unencryptedNumbers[j - 2]
            lastCalc = unencryptedNumbers[j - 1]
        if secondToLastCalc == 0 or lastCalc == 0:
            unencryptedNumbers[j] += math.ceil(FMWValues[0][min(j, 19)] * firstDigit)
        elif secondToLastCalc % 2 == 0 and lastCalc % 2 == 0:
            unencryptedNumbers[j] += abs(FMWValues[1][min(j, 19)] - len(unencryptedNumbers))
        else:
            unencryptedNumbers[j] += FMWValues[2][min(j, 19)] + lastCalc + secondToLastCalc
        unencryptedNumbers[j] %= 10
        if debug:
            print("Answers: " + "".join(str(unencryptedNumbers)))
    string = [str(x) for x in unencryptedNumbers]
    print("Final: " + "".join(string))

if __name__ == "__main__":
    main()