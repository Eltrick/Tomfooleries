Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main() -> None:
    global Alphabet

    # Initial Prepping With Serial Number
    serialNumber = list(input("Input the Serial Number: ").upper())
    for i in range(0, len(serialNumber)):
        if serialNumber[i] in Alphabet:
            serialNumber[i] = Alphabet.index(serialNumber[i]) + 1
        else:
            serialNumber[i] = int(serialNumber[i])

    # Module Letter
    initialLetter = input("Input the initial letter on the module: ").upper()
    usedLetters = []
    for i in range(0, 18):
        if i == 0:
            tempLetter = Alphabet[(Alphabet.index(initialLetter) + serialNumber[i % 6]) % 26]
            while tempLetter == initialLetter or tempLetter in usedLetters:
                tempLetter = Alphabet[(Alphabet.index(tempLetter) + 1) % 26]
            usedLetters.append(tempLetter)
        else:
            tempLetter = Alphabet[(Alphabet.index(usedLetters[i - 1]) + serialNumber[i % 6]) % 26]
            while tempLetter == initialLetter or tempLetter in usedLetters:
                tempLetter = Alphabet[(Alphabet.index(tempLetter) + 1) % 26]
            usedLetters.append(tempLetter)
    print("The mapped letters, in order, are: " + "".join(usedLetters))

if __name__ == "__main__":
    main()