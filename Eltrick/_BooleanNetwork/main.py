NodeNames = ["A", "B", "C", "D", "E", "F"]

def main() -> None:
    global NodeNames

    colours = list(input("Colours of the nodes, in order: ").upper())

    initialStateLogging = input("Initial state of the module: ").upper()
    initialState = list(initialStateLogging)
    for i in range(0, len(initialState)):
        if initialState[i] == "1":
            initialState[i] = True
        elif initialState[i] == "0":
            initialState[i] = False
    
    connections = []
    for i in range(0, len(initialState)):
        connections.append(input("Input the connections of node " + "ABCDEF"[i] + ": ").upper().split(" "))

    iterations = [[], [], [], []]
    for i in range(0, len(initialState)):
        iterations[0].append(initialState[i])
    for j in range(1, len(iterations)):
        currentConnections = [[], [], [], [], [], []]
        for k in range(0, len(currentConnections)):
            for l in range(0, len(connections[k])):
                currentConnections[k].append(GetValue(connections[k][l], iterations[j - 1]))
        for k in range(0, len(initialState)):
            if colours[k] == "R":
                iterations[j].append(Red(currentConnections[k]))
            elif colours[k] == "G":
                iterations[j].append(Green(currentConnections[k]))
            elif colours[k] == "B":
                iterations[j].append(Blue(currentConnections[k]))
    logEndStates = ""
    for j in range(0, len(iterations[3])):
        if iterations[3][j]:
            logEndStates += "1"
        else:
            logEndStates += "0"
    print("Initial State " + initialStateLogging + " has End State " + logEndStates + ".")

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