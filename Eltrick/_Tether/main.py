import time

fileContent = ""

def main() -> None:
    global fileContent

    # Getting the word list.
    file = open(r".\wordlist.txt", 'r')
    fileContent = file.readlines()
    fileContent = fileContent[0].split(", ")

    initialWord = input("Initial word: ").upper()
    finalWord = input("Final word: ").upper()
    initialTime = time.time()
    DFS([initialWord], finalWord, initialTime)

def DFS(wordsInChain: list, finalWord: str, initialTime) -> None:
    last = wordsInChain[-1]
    lastThreeCharacters = last[-3:]
    if len(wordsInChain) != 5:
        for i in range(0, len(fileContent)):
            if fileContent[i] in wordsInChain or finalWord == fileContent[i]:
                continue
            if fileContent[i][:3] == lastThreeCharacters:
                newWords = wordsInChain.copy()
                newWords.append(fileContent[i])
                DFS(newWords, finalWord, initialTime)
        return
    if lastThreeCharacters == finalWord[:3]:
        print("Elapsed time: " + str(time.time() - initialTime))
        print(", ".join(wordsInChain) + ", " + finalWord)

if __name__ == "__main__":
    main()