import math

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
dataTape = [0]
pointer = 0
serialNumber = ""
batteryCount = 0

def main() -> None:
    global Alphabet
    global dataTape
    global pointer
    global serialNumber
    global batteryCount

    serialNumber = list(input("Bomb Serial Number: ").upper())
    for i in range(0, len(serialNumber)):
        if serialNumber[i] in Alphabet:
            serialNumber[i] = Alphabet.index(serialNumber[i]) + 1
        else:
            serialNumber[i] = int(serialNumber[i])
    
    batteryCount = int(input("Battery count: "))

    end = False
    while not end:
        commandQueue = input("Current sequence of commands: ").upper()
        if commandQueue == "END":
            end = True
        else:
            Command(commandQueue)

def Command(commands: str) -> None:
    global dataTape
    global pointer
    global serialNumber
    global batteryCount
    loopstart = 0
    looptimes = 0
    for i in range(0, len(commands)):
        if commands[i] == ">":
            pointer += 1
            if len(dataTape) >= pointer:
                dataTape.append(0)
        elif commands[i] == "<":
            if pointer != 0:
                pointer -= 1
            else:
                pointer += 1
                if pointer >= len(dataTape):
                    dataTape.append(0)
        elif commands[i] == "+":
            dataTape[pointer] += 1
        elif commands[i] == "-":
            if dataTape[pointer] - 1 < 0:
                dataTape[pointer] += 1
            else:
                dataTape[pointer] -= 1
        elif commands[i] == ",":
            cellToConsider = 0
            if pointer == 0:
                if pointer + 1 >= len(dataTape):
                    dataTape.append(0)
                cellToConsider = dataTape[pointer + 1]
            else:
                cellToConsider = dataTape[pointer - 1]
            cellToConsider %= 6
            dataTape[pointer] = serialNumber[cellToConsider]
        elif commands[i] == "[":
            loopstart = i
            looptimes = 0
            print("Start of loop.")
        elif commands[i] == "]":
            if dataTape[pointer] == 0 or looptimes == batteryCount:
                print("End of loop.")
            else:
                looptimes += 1
                i = loopstart
                print("Looped " + str(looptimes) + " times. Going to start of loop.")
        elif commands[i] == ".":
            print("Current Answer: " + str(dataTape[pointer]))
        print(str(commands[i]) + " : " + str(dataTape) + " ; pointer (0-indexed): " + str(pointer))

if __name__ == "__main__":
    main()