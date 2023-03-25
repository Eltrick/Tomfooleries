import time

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main() -> None:
    global Alphabet
    
    frequencyTable = {}

    file = ""
    entireWordlist = True if input("Entire word list? ").upper() == "Y" else False
    damoclesLumber = True if input("Module Scramble? ").upper() == "Y" else False
    if damoclesLumber:
        file = open(r".\ModuleList.txt", 'r')
    elif entireWordlist:
        file = open(r".\vWordlist.txt", 'r')
    else:
        file = open(r".\Wordlist.txt", 'r')
    fileContent = file.readlines()
    fileContent = fileContent[0].split(", ")

    
    lettersNotPresent = []
    for i in range(0, len(Alphabet)):
        lettersNotPresent.append(Alphabet[i])
    
    moduleList = sorted(list(input("Letter string on module: ").upper()))
    for i in range(0, len(moduleList)):
        if moduleList[i] in lettersNotPresent:
            lettersNotPresent.pop(lettersNotPresent.index(moduleList[i]))
    
    for i in range(len(fileContent) - 1, -1, -1):
        nonexistentLetter = False
        for j in range(0, len(fileContent[i])):
            if fileContent[i][j] in lettersNotPresent:
                nonexistentLetter = True
        if nonexistentLetter:
            fileContent.pop(i)
    
    for i in range(0, len(Alphabet)):
        frequencyTable[Alphabet[i]] = moduleList.count(Alphabet[i])
    
    length = 0
    queue = [[]]
    timeStart = time.time()
    while len(queue) != 0:
        current = queue.pop(0)
        if len(current) > length:
            length = len(current)
            timeIntermediate = time.time()
            print("Time taken to filter through groups of length " + str(length - 1) + ": " + str(timeIntermediate - timeStart))
        currentHashmap = {}
        for i in range(0, len(Alphabet)):
            currentHashmap[Alphabet[i]] = 0
            for j in range(0, len(current)):
                currentHashmap[Alphabet[i]] += str(current[j]).count(Alphabet[i])
        var = 0
        if len(current) != 0:
            var = fileContent.index(current[-1])
        for i in range(var, len(fileContent)):
            newHashmap = {}
            safe = True
            for j in range(0, len(currentHashmap)):
                safe &= (currentHashmap[Alphabet[j]] + fileContent[i].count(Alphabet[j]) <= frequencyTable[Alphabet[j]])
                if not safe:
                    break
            if safe:
                newItem = current.copy()
                newItem.append(fileContent[i])
                if ((len(newItem) == 5 and not damoclesLumber) or (len(newItem) == 2 and damoclesLumber)) and (len("".join(newItem)) == len(moduleList)):
                    print("".join(newItem))
                else:
                    queue.append(newItem)
    timeEnd = time.time()
    print("Time taken to find solutions: " + str(timeEnd - timeStart))

if __name__ == "__main__":
    main()