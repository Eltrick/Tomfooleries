import time
from collections import deque

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main() -> None:
    frequencyTable = {}

    file = ""
    entireWordlist = input("Entire word list? ").upper() == "Y"
    damoclesLumber = input("Module Scramble? ").upper() == "Y"
    if damoclesLumber:
        file = open(r".\ModuleList.txt", 'r')
    elif entireWordlist:
        file = open(r".\vWordlist.txt", 'r')
    else:
        file = open(r".\Wordlist.txt", 'r')
    fileContent = file.read().strip().split(", ")
    
    lettersNotPresent = []
    moduleList = sorted(list(input("Letter string on module: ").upper()))
    for i in range(len(Alphabet)):
        if Alphabet[i] not in moduleList:
            lettersNotPresent.append(Alphabet[i])
    
    for i in range(len(fileContent) - 1, -1, -1):
        if any([fileContent[i][j] in lettersNotPresent for j in range(len(fileContent[i]))]):
            fileContent.pop(i)
    
    for i in range(0, len(Alphabet)):
        frequencyTable[Alphabet[i]] = moduleList.count(Alphabet[i])
    
    length = 0
    queue = deque([[]])
    timeStart = time.time()
    while len(queue) != 0:
        current = queue.popleft()
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