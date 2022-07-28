usableLetters = []

def main() -> None:
    global usableLetters
    usableLetters = input("Enter the entirety of the 6×6 grid here, with each row separated by commas: ").upper().split(",")
    wordList = ["PERCENT", "PRESENT", "ELECTRON", "ASSEMBLY", "ASSAULT", "SALVATION", "KNOWLEDGE", "EXPLOSION", "EMERGENCY", "DIGITAL", "APPLIED", "ENTHUSIASM", "TENDENCY", "MULTIPLY", "LANGUAGE", "RESTAURANT", "COMPUTER", "DESCENT", "STIMULATE", "QUOTATION", "CONFUSION", "EXAMINE", "BACKGROUND", "IMPOUND", "FASHION", "RESTROOM", "FRIENDLY", "NEUTRAL", "CUNNING", "PARTNER", "BREAKFAST", "PRESENCE", "PRIVATE", "EVALUATE", "PROBLEM", "UNPLEASANT", "DIFFICULTY", "TENSION", "PROTECTION", "ESTABLISH", "DRAMATIC", "CONVICT", "EXPLAIN", "CONTAIN", "INSTINCT", "CHARACTER", "MONOPOLY", "SELECTION", "SLIPPERY", "PASTURE", "CRIMINAL", "ACCIDENT", "CHANNEL", "DIAMOND", "MAJORITY", "BUTTOCKS", "DIRECTORY", "CHEMISTRY", "PROMOTE", "REPLACE", "CHILDISH", "PROFOUND", "SENTIMENT", "OFFSPRING", "CREATION", "PRESTIGE", "ABILITY", "PSYCHOLOGY", "BATTERY", "TEXTURE", "BROADCAST", "IMPRESS", "SERVICE", "ABSTRACT", "CEREMONY", "POSSESSION", "MISERABLE", "RECYCLE", "SHALLOW", "CHALLENGE", "CONTRARY", "PURSUIT", "REHEARSAL", "ADVENTURE", "SOFTWARE", "WARRANT", "NEIGHBOUR", "DIALOGUE", "QUARTER", "CONSTRAINT", "APPRECIATE", "MINIMUM", "PAVEMENT", "TROUBLE", "CLASSIFY", "PREOCCUPY", "LABORATORY", "INTENTION", "INHIBITION", "DISGRACE", "VANQUISH", "WILDERNESS"]
    usableWords = []
    for i in range(0, len(wordList)):
        usableCoordinates = []
        nextCoordinates = []
        nextNextCoordinates = []
        nextNextNextCoordinates = []
        nextNextNextNextCoordinates = []
        nextNextNextNextNextCoordinates = []
        nextNextNextNextNextNextCoordinates = []
        for j in range(0, len(usableLetters)):
            for k in range(0, len(usableLetters[j])):
                if wordList[i][0] == usableLetters[j][k]:
                    usableCoordinates.append([j, k])
        if len(usableCoordinates) != 0:
            for j in range(0, len(usableCoordinates)):
                checkAdjacency(usableCoordinates[j][0], usableCoordinates[j][1], wordList[i][1], nextCoordinates)
        if len(nextCoordinates) != 0:
            for j in range(0, len(nextCoordinates)):
                checkAdjacency(nextCoordinates[j][0], nextCoordinates[j][1], wordList[i][2], nextNextCoordinates)
        if len(nextNextCoordinates) != 0:
            for j in range(0, len(nextNextCoordinates)):
                checkAdjacency(nextNextCoordinates[j][0], nextNextCoordinates[j][1], wordList[i][3], nextNextNextCoordinates)
        if len(nextNextNextCoordinates) != 0:
            for j in range(0, len(nextNextNextCoordinates)):
                checkAdjacency(nextNextNextCoordinates[j][0], nextNextNextCoordinates[j][1], wordList[i][4], nextNextNextNextCoordinates)
        if len(nextNextNextNextCoordinates) != 0:
            for j in range(0, len(nextNextNextNextCoordinates)):
                checkAdjacency(nextNextNextNextCoordinates[j][0], nextNextNextNextCoordinates[j][1], wordList[i][5], nextNextNextNextNextCoordinates)
        if len(nextNextNextNextNextCoordinates) != 0:
            for j in range(0, len(nextNextNextNextNextCoordinates)):
                checkAdjacency(nextNextNextNextNextCoordinates[j][0], nextNextNextNextNextCoordinates[j][1], wordList[i][6], nextNextNextNextNextNextCoordinates)
        if len(nextNextNextNextNextNextCoordinates) != 0:
            usableWords.append(wordList[i])
    print("After evaluating all words, the usable words in depth 5 are: " + str(usableWords))

def checkAdjacency(row, col, letter, array):
    global usableLetters
    if usableLetters[(row-1+6)%6][(col-1+6)%6] == letter:
        array.append([(row-1+6)%6, (col-1+6)%6])
    if usableLetters[(row-1+6)%6][(col-0+6)%6] == letter:
        array.append([(row-1+6)%6, (col-0+6)%6])
    if usableLetters[(row-1+6)%6][(col+1+6)%6] == letter:
        array.append([(row-1+6)%6, (col+1+6)%6])
    if usableLetters[(row-0+6)%6][(col-1+6)%6] == letter:
        array.append([(row-0+6)%6, (col-1+6)%6])
    if usableLetters[(row-0+6)%6][(col+1+6)%6] == letter:
        array.append([(row-0+6)%6, (col+1+6)%6])
    if usableLetters[(row+1+6)%6][(col-1+6)%6] == letter:
        array.append([(row+1+6)%6, (col-1+6)%6])
    if usableLetters[(row+1+6)%6][(col-0+6)%6] == letter:
        array.append([(row+1+6)%6, (col-0+6)%6])
    if usableLetters[(row+1+6)%6][(col+1+6)%6] == letter:
        array.append([(row+1+6)%6, (col+1+6)%6])

if __name__ == "__main__":
    main()