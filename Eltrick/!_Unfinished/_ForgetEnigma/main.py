Rotors = [[["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"], ["A", "B", "C", "D*", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q*", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]], [["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"], ["A", "B", "C", "D", "E*", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R*", "S", "T", "U", "V", "W", "X", "Y", "Z"]], [["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"], ["A", "B", "C", "D", "E", "F", "G", "H", "I*", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V*", "W", "X", "Y", "Z"]], [["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G", "K", "D", "C", "M", "W", "B"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J*", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W*", "X", "Y", "Z"]], [["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J", "Q", "O", "F", "E", "C", "K"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M*", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z*"]], [["J", "P", "G", "V", "O", "U", "M", "F", "Y", "Q", "B", "E", "N", "H", "Z", "R", "D", "K", "A", "S", "X", "L", "I", "C", "T", "W"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L*", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y*", "Z"]], [["N", "Z", "J", "H", "G", "R", "C", "X", "M", "Y", "S", "W", "B", "O", "U", "F", "A", "I", "V", "L", "P", "E", "K", "Q", "D", "T"], ["A", "B", "C", "D", "E", "F", "G", "H*", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U*", "V", "W", "X", "Y", "Z"]], [["F", "K", "Q", "H", "T", "L", "X", "O", "C", "B", "J", "S", "P", "D", "Z", "R", "A", "M", "E", "W", "N", "I", "U", "Y", "G", "V"], ["A", "B", "C*", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P*", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]], [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["L", "U", "S", "N", "P", "Q", "O", "M", "J", "I", "Y", "A", "H", "D", "G", "E", "F", "X", "C", "V", "B", "T", "Z", "R", "K", "W"]], [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["X", "Q", "U", "M", "F", "E", "P", "O", "W", "L", "T", "J", "D", "Z", "H", "G", "B", "V", "Y", "K", "C", "R", "I", "A", "S", "N"]], [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["E", "S", "K", "O", "A", "Q", "M", "J", "Y", "H", "C", "P", "G", "T", "D", "L", "F", "U", "B", "N", "R", "X", "Z", "V", "I", "W"]]]
RotorIndices = "12345678ABC"
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
RotorSetup = []

def main() -> None:
    global Rotors
    global RotorIndices
    global Alphabet
    global RotorSetup

    infoDump = list(input("Initial rotor setup: ").upper())[::-1]
    for i in range(0, len(infoDump)):
        RotorSetup.append(Rotors[RotorIndices.index(infoDump[i])])
    
    letterConfig = list(input("Initial letters: ").upper())[::-1]
    for i in range(0, len(letterConfig)):
        while letterConfig[i] not in RotorSetup[i][1][0]:
            RotorSetup[i] = ShiftMini(RotorSetup[i])
    
    while True:
        unencryptedString = input("Unencrypted message: ").upper()
        print(Process(unencryptedString))
        print(RotorSetup)

def ShiftRotors(rotors: list) -> list:
    temp = rotors.copy()
    if IsTurnOver(temp[0]):
        temp[1] = ShiftMini(temp[1])
    temp[0] = ShiftMini(temp[0])
    return temp

def ShiftMini(rotor: list) -> list:
    temp = rotor.copy()
    for i in range(0, len(temp)):
        temp[i] = temp[i][1:] + temp[i][:1]
    return temp

def Process(string: str) -> str:
    global Alphabet
    global RotorSetup
    result = ""
    for i in range(0, len(string)):
        print("Encrypting not implemented")
        RotorSetup = ShiftRotors(RotorSetup)
    return result

def IsTurnOver(rotor: list) -> bool:
    if "*" in rotor[1][0]:
        return True
    return False

if __name__ == "__main__":
    main()