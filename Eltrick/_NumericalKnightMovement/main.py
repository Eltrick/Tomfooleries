import math
import random

Count = 0
KnightsMoves = [[6, 9], [8, 10, 7], [9, 11, 4], [5, 10], [2, 10, 13], [3, 11, 14, 12], [0, 8, 15, 13], [1, 9, 14], [6, 14, 1], [2, 0, 7, 15], [1, 3, 4, 12], [5, 13, 2], [10, 5], [4, 6, 11], [5, 7, 8], [9, 6]] # Thanks Crunch (for crunching the numbers for us)!
Coordinates = ["A1", "B1", "C1", "D1", "A2", "B2", "C2", "D2", "A3", "B3", "C3", "D3", "A4", "B4", "C4", "D4"] # Thanks Crunch, again (for being inefficient)!!

def main() -> None:
    global KnightsMoves
    global Coordinates
    global Count

    initialState = []
    allowedFirstMoves = []
    
    infoDump = input("Initial Board State: ")
    if " " in infoDump:
        initialState = [int(x) for x in infoDump.split(" ")]
    else:
        initialState = [int(x) for x in list(infoDump)]

    check = 0
    for i in range(0, len(initialState)):
        check += initialState[i] * ((-1) ** (i + math.floor(i / 4)))
    
    for i in range(0, len(initialState)):
        if not (check == 0 or check == (-1) ** (i + math.floor(i / 4))) or initialState[i] == 0:
            continue
        allowedFirstMoves.append(i)

    random.shuffle(allowedFirstMoves)

    for i in range(0, len(allowedFirstMoves)):
        state = initialState.copy()
        state[allowedFirstMoves[i]] -= 1
        DFS(state, [allowedFirstMoves[i]])
    print(str(Count))

def DFS(state: list, lastMove: list) -> None:
    global Count
    if sum(state) == 0:
        finalCoordinates = []
        for i in range(0, len(lastMove)):
            finalCoordinates.append(Coordinates[lastMove[i]])
        print(" ".join(finalCoordinates))
        Count += 1
        return
    for i in range(0, len(KnightsMoves[lastMove[-1]])):
        if state[KnightsMoves[lastMove[-1]][i]] == 0:
            continue
        newState = state.copy()
        newState[KnightsMoves[lastMove[-1]][i]] -= 1
        newMoveList = lastMove.copy()
        newMoveList.append(KnightsMoves[lastMove[-1]][i])
        DFS(newState, newMoveList)

if __name__ == "__main__":
    main()