Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main() -> None:
    global Alphabet
    
    moduleString = list(input("String of characters on the module: ").upper())
    reversedModuleString = []
    results = []

    for i in range(0, len(moduleString)):
        moduleString[i] = Alphabet.index(moduleString[i])
    reversedModuleString = moduleString[::-1]

    for i in range(0, len(moduleString)):
        results.append(Alphabet[max(DigitalRoot(moduleString[i] + reversedModuleString[i]) - 1, 0)])
    
    print("Resulting string to input into the module: " + "".join(results))

def DigitalRoot(num: int) -> int:
    res = num % 9
    if res == 0 and num > 0:
        return 9
    else:
        return res

if __name__ == "__main__":
    main()