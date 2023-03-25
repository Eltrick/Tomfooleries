Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DigitToLetters = [["L", "N", "M", "C", "D", "E", "G", "O"], ["W", "F", "G", "Q", "T", "B", "I", "L"], ["H", "K", "I", "L", "Z", "R", "A", "S"], ["T", "M", "J", "Y", "S", "G", "B", "Z"], ["J", "U", "V", "P", "B", "C", "Z", "G"], ["N", "I", "F", "Z", "G", "H", "P", "U"], ["F", "G", "E", "U", "H", "W", "M", "N"], ["S", "V", "Y", "T", "F", "J", "Q", "H"], ["Z", "H", "S", "D", "P", "N", "K", "R"], ["O", "D", "W", "X", "U", "V", "H", "P"]]

def main() -> None:
    global Alphabet
    global DigitToLetters
    
    print("-------------------SETUP-------------------")
    moduleCount = int(input("Module Count: "))
    valueColumn = [0, 0, 0, 0, 0, 0, 0, 0]
    valueColumn[0] = int(input("Port count: "))
    valueColumn[1] = int(input("Starting time (in minutes): "))
    valueColumn[4] = int(input("Sum of Serial Number digits: "))
    valueColumn[6] = int(input("Battery count: "))
    valueColumn[7] = int(input("Indicator count: "))

    for i in range(0, len(DigitToLetters)):
        for j in range(0, len(DigitToLetters[i])):
            DigitToLetters[i][j] = Alphabet.index(DigitToLetters[i][j])

    while True:
        print("-------------------REPETITIVENESS-------------------")
        resultString = ""

        valueColumn[2] = int(input("Total minutes remaining: "))
        valueColumn[3] = int(input("Sum of least significant digits of two factors, or solved module count: "))
        valueColumn[5] = int(input("Current strike count: ")) + moduleCount
        referenceDigit = int(input("Digit on small display: "))
        
        moduleString = list(input("Input string of letters on module with given information: ").upper())
        for i in range(0, len(moduleString)):
            moduleString[i] = Alphabet.index(moduleString[i])
        for i in range(0, len(moduleString)):
            resultString += Alphabet[(moduleString[i] + DigitToLetters[referenceDigit][i] + valueColumn[i]) % 26]
        
        if "ABA" in resultString:
            print("ABA found in string. Press position #" + str(resultString.index("ABA") + 2))
        elif "BAB" in resultString:
            print("BAB found in string. Press position #" + str(resultString.index("BAB") + 2))
        else:
            print("Press SKIP.")

if __name__ == "__main__":
    main()