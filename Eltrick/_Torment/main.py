Coordinates = ["A1", "B1", "C1", "D1", "A2", "B2", "C2", "D2", "A3", "B3", "C3", "D3", "A4", "B4", "C4", "D4"] # Thanks Crunch, again (for being inefficient)!!

def main() -> None:
    global Coordinates

    goalState = [int(x) for x in list(input("LOOK: "))]

    fall = []
    for i in range(0, len(goalState)):
        fall.append([int(x) for x in list(input("FALL #" + str(i + 1) + ": "))])
    
    j = int(input("STOP: "))
    initialState = [j] * 16
    
    for i in range(0, len(fall)):
        for j in range(i + 1, len(fall)):
            for k in range(j + 1, len(fall)):
                checksum = initialState.copy()
                for l in range(0, len(goalState)):
                    checksum[l] = (checksum[l] + fall[i][l] + fall[j][l] + fall[k][l]) % 3
                if checksum == goalState:
                    logging = Coordinates[i] + ", " + Coordinates[j] + ", " + Coordinates[k]
                    print("Solution: " + logging)

if __name__ == "__main__":
    main()