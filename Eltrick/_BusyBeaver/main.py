state = [False, False, False, False, False, False, False, False, False, False]
stateCopy = [False, False, False, False, False, False, False, False, False, False]
pointer = 0
stage = 1

def main() -> None:
    global state
    global pointer
    global stage
    
    print("Welcome to the module solver for Busy Beaver. Have fun Beavering!")
    initialState = input("Please input the initial state on the module: ")
    pointer = int(input("Please input the initial pointer position (0-indexed): "))
    for i in range(0, 10):
        if initialState[i] == "1":
            state[i] = True
            stateCopy[i] = True
        elif initialState[i] == "0":
            state[i] = False
            stateCopy[i] = False
    
    print("This solver only works in Normal Mode. Legacy Mode will be added at some point.")
    while True:
        print("<---------------------->STAGE #" + str(stage) + "<---------------------->")
        inputLetters = input("Please input the things that you want to do, to end or to calculate based on two letters, separated by a space: ").upper().split(" ")
        if inputLetters[0] == "END":
            finalString = ""
            for i in range(0, 10):
                if state[i] == True:
                    finalString += "1"
                else:
                    finalString += "0"
            print("And so, the final tape to submit is: " + finalString)
            exit()
        else:
            ModifyValue(inputLetters[0])
            ModifyPointer(inputLetters[1])
            currentString = ""
            for i in range(0, 10):
                stateCopy[i] = state[i]
            for i in range(0, 10):
                if state[i] == True:
                    currentString += "1"
                else:
                    currentString += "0"
            print("Current tape: " + currentString + "; Pointer: " + str(pointer))
            stage += 1

def ModifyValue(character):
    global state
    global pointer
    global stage
    
    if character == "A":
        if state[pointer] == False:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "B":
        if pointer <= 4:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "C":
        if state[stage % 10] == True:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "D":
        if state[pointer] == state[(pointer + 5) % 10]:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "E":
        if state[(pointer - 1) % 10] == state[(pointer + 1) % 10]:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "F":
        if stage % 2 == 1:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "G":
        if stage % 2 == 0:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "H":
        if state[(pointer - 1) % 10] != state[(pointer + 1) % 10]:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "I":
        if state[pointer] != state[(pointer + 5) % 10]:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "J":
        if state[pointer] == True:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "K":
        if pointer > 4:
            state[pointer] = True
        else:
            state[pointer] = False
    elif character == "L":
        if state[stage % 10] == False:
            state[pointer] = True
        else:
            state[pointer] = False

def ModifyPointer(character):
    global state
    global pointer
    global stage
    
    if character == "A":
        if stateCopy[pointer] == False:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "B":
        if pointer <= 4:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "C":
        if stateCopy[stage % 10] == True:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "D":
        if stateCopy[pointer] == stateCopy[(pointer + 5) % 10]:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "E":
        if stateCopy[(pointer - 1) % 10] == stateCopy[(pointer + 1) % 10]:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "F":
        if stage % 2 == 1:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "G":
        if stage % 2 == 0:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "H":
        if stateCopy[(pointer - 1) % 10] != stateCopy[(pointer + 1) % 10]:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "I":
        if stateCopy[pointer] != stateCopy[(pointer + 5) % 10]:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "J":
        if stateCopy[pointer] == True:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "K":
        if pointer > 4:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    elif character == "L":
        if stateCopy[stage % 10] == False:
            pointer = (pointer - 1) % 10
        else:
            pointer = (pointer + 1) % 10
    

if __name__ == "__main__":
    main()