import math


bitStream = []
Alphabet = ["!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main() -> None:
    global bitStream
    global Alphabet

    for i in range(0, 3):
        bitString = input("Enter bitstring #" + str(i+1) + " here: ")
        if len(bitString) % 5 != 0:
            print("Expected bitstring of length that is divisible by 5, restarting...")
            main()
        bitStream.append(BitstringToBooleans(bitString))
    results = []
    results.append(BitwiseXor(bitStream[0], bitStream[1]))
    results.append(BitwiseXor(BitwiseXor(bitStream[0], bitStream[1]), bitStream[2]))
    results.append(BitwiseXor(bitStream[1], bitStream[2]))

    for i in range(0, len(results)):
        for j in range(0, len(results[i])):
            results[i][j] = ("0" if results[i][j] == False else "1")

    for i in range(0, len(results)):
        cutoff = int(len(results[i]) / 5)
        for j in range(1, 6):
            print("".join(results[i])[cutoff*(j-1):cutoff*j])
        print("")
    
    answers = []

    for i in range(0, 3):
        infoDump = input("Input the uncycled word, and the number of letters the word was cycled by: ").upper().split(" ")
        temporary = ""
        for j in range(0, len(infoDump[0])):
            temporary += LetterToBinary(infoDump[0][j])
        answers.append(BitstringToBooleans(Modifications(temporary, int(infoDump[1]) - 1)))
    
    finalAnswer = BitwiseXor(BitwiseXor(answers[0], answers[1]), answers[2])
    finalBinaries = []
    finalWord = ""

    while len(finalAnswer) != 25:
        finalAnswer.insert(0, False)
    for i in range(0, 5):
        finalBinaries.append(finalAnswer[5*i:5*(i+1)])
    for i in range(0, 5):
        temp = 0
        for j in range(4, -1, -1):
            temp += (1 if finalBinaries[i][4 - j] else 0) * (2 ** j)
        finalWord += Alphabet[temp]
    print("Final word: " + finalWord)
    
def BitwiseXor(input1: list, input2: list) -> list:
    res = []
    while len(input1) != len(input2):
        if len(input1) < len(input2):
            input1.insert(0, False)
        else:
            input2.insert(0, False)
    for i in range(0, len(input1)):
        res.append(input1[i] ^ input2[i])
    return res

def LetterToBinary(letter: str) -> str:
    intermediate = format(Alphabet.index(letter), 'b')
    while len(intermediate) != 5:
        intermediate = "0" + intermediate
    return intermediate

def Modifications(binary: str, modification: int) -> str:
    result = ""
    rule1 = math.floor(modification / 2)
    rule2 = modification % 2
    for i in range(0, len(binary)):
        x = i % 5
        y = int(i / 5)
        newX = 0
        newY = 0
        if rule1 == 1:
            newX = y
        else:
            newX = 4 - y
        if rule2 == 1:
            newY = x
        else:
            newY = 4 - x
        newIndex = newY*5 + newX
        result += binary[newIndex]
    if modification == 1 or modification == 2:
        result = "".join(list(result)[::-1])
    return result

def BitstringToBooleans(bitString: str) -> list:
    tempBitString = []
    for x in range(0, len(bitString)):
            if bitString[x] == "0":
                tempBitString.append(False)
            elif bitString[x] == "1":
                tempBitString.append(True)
    return tempBitString

def Logging(values: list) -> str:
    temp = ""
    for i in range(0, len(values)):
        if values[i]:
            temp += "1"
        else:
            temp += "0"
    return temp

if __name__ == "__main__":
    main()