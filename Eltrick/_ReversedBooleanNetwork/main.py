NodeNames = ["A", "B", "C", "D", "E", "F"]

def main() -> None:
    global NodeNames

    answers = []
    counts = [0, 0, 0, 0, 0, 0]

    colours = list(input("Colours of the nodes, in order: ").upper())

    finalState = list(input("Final state of the module: ").upper())
    for i in range(0, len(finalState)):
        if finalState[i] == "1":
            finalState[i] = True
        elif finalState[i] == "0":
            finalState[i] = False
    
    connections = []
    for i in range(0, len(finalState)):
        connections.append(input("Input the connections of node " + "ABCDEF"[i] + ": ").upper().split(" "))
    
    for i in range(0, 64):
        iterations = [[], [], [], []]
        iterations[0] = BinaryConverter(i)
        logging = ""
        for j in range(0, len(iterations[0])):
            if iterations[0][j]:
                logging += "1"
            else:
                logging += "0"
        for j in range(1, len(iterations)):
            currentConnections = [[], [], [], [], [], []]
            for k in range(0, len(currentConnections)):
                for l in range(0, len(connections[k])):
                    currentConnections[k].append(GetValue(connections[k][l], iterations[j - 1]))
            for k in range(0, len(finalState)):
                if colours[k] == "R":
                    iterations[j].append(Red(currentConnections[k]))
                elif colours[k] == "G":
                    iterations[j].append(Green(currentConnections[k]))
                elif colours[k] == "B":
                    iterations[j].append(Blue(currentConnections[k]))
        answerValid = True
        logEndStates = ""
        for j in range(0, len(iterations[3])):
            if iterations[3][j]:
                logEndStates += "1"
            else:
                logEndStates += "0"
        for j in range(0, len(finalState)):
            if iterations[3][j] != finalState[j] and finalState[j] != "-":
                answerValid = False
        if answerValid:
            answers.append(iterations[0])
            print("Initial State " + logging + " has End State " + logEndStates + ", which is VALID. Adding to solution set.")
        else:
            print("Initial State " + logging + " has End State " + logEndStates + ", which is INVALID. Ignoring.")
    for i in range(0, len(answers)):
        for j in range(0, len(answers[i])):
            if answers[i][j]:
                counts[j] += 1
    print("Counts: " + str(counts))

def BinaryConverter(num: int) -> list:
    intermediary = format(num, 'b')
    result = []
    while len(intermediary) != 6:
        intermediary = "0" + intermediary
    for i in range(0, len(intermediary)):
        result.append(True if intermediary[i] == "1" else False)
    return result

def Red(inputs: list) -> bool:
    allOnes = True
    for i in range(0, len(inputs)):
        if inputs[i] != True:
            allOnes = False
    return allOnes

def Green(inputs: list) -> bool:
    noOnes = True
    for i in range(0, len(inputs)):
        if inputs[i] == True:
            noOnes = False
    return not noOnes

def Blue(inputs: list) -> bool:
    oneCount = 0
    for i in range(0, len(inputs)):
        if inputs[i] == True:
            oneCount += 1
    return oneCount > (len(inputs) / 2)

def GetValue(pair: str, allValues: list) -> bool:
    value = allValues[NodeNames.index(pair[1])]
    if pair[0] == "+":
        return value
    elif pair[0] == "-":
        return not value

if __name__ == "__main__":
    main()