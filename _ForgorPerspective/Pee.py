import math

# FunnyTable[Colour][Number]
Colours = ["R", "B", "G", "Y", "M", "O"]
FunnyTable = [[[1, 3, 5, 4, 2, 6], [2, 3, 5, 1, 6, 4], [3, 4, 2, 1, 6, 5], [4, 5, 3, 1, 6, 2], [5, 2, 4, 1, 6, 3], [6, 5, 3, 4, 2, 1]], 
              [[1, 5, 3, 6, 4, 2], [2, 5, 3, 4, 1, 6], [3, 2, 4, 5, 1, 6], [4, 3, 5, 2, 1, 6], [5, 4, 2, 3, 1, 6], [6, 3, 5, 1, 4, 2]], 
              [[1, 6, 5, 3, 4, 2], [2, 4, 5, 3, 1, 6], [3, 5, 2, 4, 1, 6], [4, 2, 3, 5, 1, 6], [5, 3, 4, 2, 1, 6], [6, 1, 3, 5, 4, 2]], 
              [[1, 5, 2, 4, 3, 6], [2, 5, 6, 1, 3, 4], [3, 2, 6, 1, 4, 5], [4, 3, 6, 1, 5, 2], [5, 4, 6, 1, 2, 3], [6, 3, 2, 4, 5, 1]], 
              [[1, 4, 5, 6, 3, 2], [2, 1, 5, 4, 3, 6], [3, 1, 2, 5, 4, 6], [4, 1, 3, 2, 5, 6], [5, 1, 4, 3, 2, 6], [6, 4, 3, 1, 5, 2]], 
              [[1, 5, 4, 2, 6, 3], [2, 5, 1, 6, 4, 3], [3, 2, 1, 6, 5, 4], [4, 3, 1, 6, 2, 5], [5, 4, 1, 6, 3, 2], [6, 3, 4, 2, 1, 5]]]
Alphabet = ["!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Caesar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main() -> None:
    global FunnyTable
    global Alphabet
    
    CharacterShift = 0
    Answer = ""
    stage = 1
    
    print("Hello there, and prepare yourselves. We're in for a ride.")
    print("---------------------------------<PREPARATIONS>----------------------------------")
    print("Just answer these questions normally using the shortest answer you can.")
    SerialNumber = list(input("What is the serial number? ").upper())
    X = Alphabet.index(SerialNumber[4])
    Y = 0
    for char in SerialNumber:
        if char in "0123456789":
            Y += int(char)
    print("X = " + str(X) + "; Y = " + str(Y))
    NumberOfPlates = int(input("How many port plates are there? "))
    NumberOfBatteryHolders = int(input("How many battery holders are there? "))
    NumberOfLitIndicators = int(input("How many lit indicators are there? "))
    NumberOfUnlitIndicators = int(input("How many unlit indicators are there? "))
    NumberOfIndicators = NumberOfLitIndicators + NumberOfUnlitIndicators
    LitSIG = (True if input("Is there a lit SIG? (Y/N) ").upper() == "Y" else False)
    NumberOfDBatteries = int(input("How many D batteries are there? "))
    MoreThanThreeBatteries = (True if input("Are there more than 3 batteries? (Y/N) ").upper() == "Y" else False)
    RuleNumber = int(input("What is the rule number being used on this bomb? "))
    if RuleNumber == 0:
        CharacterShift = 3
    elif RuleNumber == 1:
        CharacterShift = X
    elif RuleNumber == 2:
        CharacterShift = -Y
    elif RuleNumber == 3:
        CharacterShift = Y - NumberOfPlates
    elif RuleNumber == 4:
        CharacterShift = int(SerialNumber[5])
    elif RuleNumber == 5:
        CharacterShift = -NumberOfBatteryHolders + (2 * X)
    elif RuleNumber == 6:
        CharacterShift = NumberOfLitIndicators + Y - NumberOfUnlitIndicators
    elif RuleNumber == 7:
        if LitSIG:
            CharacterShift = X
        else:
            CharacterShift = Y
    elif RuleNumber == 8:
        CharacterShift = X + Y - NumberOfIndicators + NumberOfDBatteries
    elif RuleNumber == 9:
        if MoreThanThreeBatteries:
            CharacterShift += X
        else:
            CharacterShift += -X
        if NumberOfIndicators > 3:
            CharacterShift += Y
        else:
            CharacterShift += -Y
    print("Caesar-shifting by " + str(CharacterShift))
    
    print("---------------------------------<START_MODULE>----------------------------------")
    print("Command Format: <MinutesRemaining> <ColourSequence>")
    while True:
        print("----------------------------------------<NEW_STAGE>----------------------------------------")
        infoDump = input("Enter the information given at stage " + str(stage) + ": ").upper().split(" ")
        
        if infoDump[0] == "END":
            print("---------------------------------<FINAL>---------------------------------")
            print("The full answer is: " + Answer)
            print("The End, I have no use for you anymore, goodbye.")
            exit()
        
        MinutesRemaining = int(infoDump[0])
        ColourSequence = infoDump[1]
        
        FaceNumber = 6
        if MinutesRemaining % 6 == 0:
            print("Face Rule: Divisible by 6")
            FaceNumber = 0
        elif prime(MinutesRemaining):
            print("Face Rule: Prime")
            FaceNumber = 1
        elif square(MinutesRemaining):
            print("Face Rule: Square")
            FaceNumber = 2
        elif MinutesRemaining < 10:
            print("Face Rule: Less than 10")
            FaceNumber = 3
        elif MinutesRemaining % 2 == 0:
            print("Face Rule: Even number")
            FaceNumber = 4
        else:
            print("Face Rule: Otherwise")
            FaceNumber = 5
        Cell = FunnyTable[Colours.index(ColourSequence[FaceNumber])][FaceNumber]
        PermutatedString = ""
        for i in range(0, 6):
            PermutatedString += ColourSequence[Cell[i] - 1]
        print("Permutated face colours: " + PermutatedString)
        ans = ""
        for i in range(0, 6):
            ans += Caesar[(Caesar.index(PermutatedString[i]) + CharacterShift) % 26]
        print("Answer sequence: " + ans)
        VC = ""
        
        for char in ans:
            if char in "AEIOU":
                VC += "V"
            else:
                VC += "C"
        VC += VC
        
        vowelCount = 0
        for char in ans:
            if char in "AEIOU":
                vowelCount += 1
        if vowelCount >= 3:
            Answer += ans[0]
            print("Adding " + ans[0] + " to answer string")
        elif vowelCount == 0:
            Answer += ans[4]
            print("Adding " + ans[4] + " to answer string")
        elif vowelCount == 1:
            if ans[5] in "AEIOU":
                Answer += ans[1]
                print("Adding " + ans[1] + " to answer string")
            else:
                Answer += ans[3]
                print("Adding " + ans[3] + " to answer string")
        else:
            if ans[5] in "AEIOU":
                Answer += ans[1]
                print("Adding " + ans[1] + " to answer string")
            elif "VV" in VC:
                Answer += ans[2]
                print("Adding " + ans[2] + " to answer string")
            elif "CCC" in VC:
                Answer += ans[3]
                print("Adding " + ans[3] + " to answer string")
            else:
                Answer += ans[5]
                print("Adding " + ans[5] + " to answer string")
        stage += 1

def prime(a):
    if a < 2:
        return False
    for x in range(2, int(math.sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

def square(a):
    return math.sqrt(a).is_integer()

if __name__ == "__main__":
    main()