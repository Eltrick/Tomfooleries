base = 10

def main() -> None:
    global base
    baseDigits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    digits = []
    possibleNumbers = []
    
    base = input("Base of number: ")
    if base == "0":
        print("what the fuck, nullary?")
        exit()
    elif base.__contains__("i") or base.__contains__("-"):
        print("Negative and complex bases not supported.")
        exit()
    else:
        base = 10 if base == "" else int(base)

    number = input("Input number string: ").upper()
    for i in range(0, len(number)):
        digits.append(baseDigits.index(number[i]))

    for i in range(0, len(digits)):
        if(NumberChecker([digits[i]], digits[0])):
            possibleNumbers.append([digits[i]])
    
    for i in range(1, len(digits)):
        currentLength = len(possibleNumbers)
        for j in range(0, currentLength):
            possibleDigits = digits.copy()
            sequenceToCheck = possibleNumbers.pop(0)
            for k in range(0, len(sequenceToCheck)):
                possibleDigits.remove(sequenceToCheck[k])
            for k in range(0, len(possibleDigits)):
                sequenceToCheck.append(possibleDigits[k])
                if NumberChecker(sequenceToCheck, digits[i]):
                    possibleNumbers.append(sequenceToCheck.copy())
                sequenceToCheck.pop()
    
    b_set = set(tuple(x) for x in possibleNumbers)
    possibleNumbers = [list(x) for x in b_set]
    
    for i in range(0, len(possibleNumbers)):
        for j in range(0, len(possibleNumbers[i])):
            possibleNumbers[i][j] = baseDigits[possibleNumbers[i][j]]
        print("".join(possibleNumbers[i]))
    
def NumberChecker(number: list, modulus: int) -> bool:
    global base
    return NumberToDecimal(number, base) % modulus == 0

def NumberToDecimal(number: list, base: int) -> int:
    result = 0
    for i in range(0, len(number)):
        result = result + number[i] * (base ** (len(number) - 1 - i))
    return result

if __name__ == "__main__":
    main()

