Rotations = ["00", "XY", "XZ", "XW", "YX", "YZ", "YW", "ZX", "ZY", "ZW", "WX", "WY", "WZ"]
RotationalMapping = {
    "00": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
    "XY": [2, 0, 3, 1, 6, 4, 7, 5, 10, 8, 11, 9, 14, 12, 15, 13], 
    "XZ": [4, 0, 6, 2, 5, 1, 7, 3, 12, 8, 14, 10, 13, 9, 15, 11], 
    "XW": [8, 0, 10, 2, 12, 4, 14, 6, 9, 1, 11, 3, 13, 5, 15, 7], 
    "YX": [1, 3, 0, 2, 5, 7, 4, 6, 9, 11, 8, 10, 13, 15, 12, 14], 
    "YZ": [4, 5, 0, 1, 6, 7, 2, 3, 12, 13, 8, 9, 14, 15, 10, 11], 
    "YW": [8, 9, 0, 1, 12, 13, 4, 5, 10, 11, 2, 3, 14, 15, 6, 7], 
    "ZX": [1, 5, 3, 7, 0, 4, 2, 6, 9, 13, 11, 15, 8, 12, 10, 14], 
    "ZY": [2, 3, 6, 7, 0, 1, 4, 5, 10, 11, 14, 15, 8, 9, 12, 13], 
    "ZW": [8, 9, 10, 11, 0, 1, 2, 3, 12, 13, 14, 15, 4, 5, 6, 7], 
    "WX": [1, 9, 3, 11, 5, 13, 7, 15, 0, 8, 2, 10, 4, 12, 6, 14], 
    "WY": [2, 3, 10, 11, 6, 7, 14, 15, 0, 1, 8, 9, 4, 5, 12, 13], 
    "WZ": [4, 5, 6, 7, 12, 13, 14, 15, 0, 1, 2, 3, 8, 9, 10, 11]
}
ModuleRotations = [[], [], []]

def main() -> None:
    global Rotations
    global RotationalMapping
    global ModuleRotations
    
    moduleStates = [[], [], [], []] # moduleStates[iteration][colour]

    for i in range(0, 4):
        moduleState = input("Enter state #" + str(i) + " of the module: ").split(" ")
        for j in range(0, 3):
            state = []
            for k in range(0, len(moduleState)):
                state.append(moduleState[k][j])
            moduleStates[i].append(state)

    for i in range(0, 3):
        print("----------------------------" + "RED,GREEN,BLUE".split(",")[i] + "----------------------------")
        for j in range(1, len(moduleStates)):
            pointer = 0
            expectedMapping = PerformRotation(moduleStates[j - 1][i], Rotations[pointer])
            while expectedMapping != moduleStates[j][i]:
                pointer += 1
                expectedMapping = PerformRotation(moduleStates[j - 1][i], Rotations[pointer])
                # print(expectedMapping)
            ModuleRotations[i].append(Rotations[pointer])
            print("Found rotation: " + Rotations[pointer])

    for i in range(0, 3):
        print("----------------------------SUBMISSION----------------------------")
        moduleState = input("Vertex + Ternary: ").split(" ")
        moduleState[0] = VertexToIndex(moduleState[0])
        moduleState[1] = [int(x) for x in moduleState[1]]
        for j in range(0, 3):
            for k in range(0, moduleState[1][j]):
                print("Applying: " + ModuleRotations[j][i])
                moduleState[0] = VertexRotation(moduleState[0], ModuleRotations[j][i])
        print("Input Vertex " + IndexToVertex(moduleState[0]))

    # while True:
    #     initialMapping = input("Enter string representing states of the module, for a given channel: ").upper().split(" ")
    #     initialMapping[0] = list(initialMapping[0])
    #     for i in range(1, len(initialMapping)):
    #         initialMapping[i] = list(initialMapping[i])
    #         pointer = 0
    #         expectedMapping = PerformRotation(initialMapping[i - 1], Rotations[pointer])
    #         while expectedMapping != initialMapping[i]:
    #             pointer += 1
    #             expectedMapping = PerformRotation(initialMapping[i - 1], Rotations[pointer])
    #         print("Found rotation: " + Rotations[pointer])

def IndexToVertex(input: int) -> str:
    res = format(input, "04b")[::-1]
    res = res.replace("0", "-")
    res = res.replace("1", "+")
    return res

def VertexToIndex(input: str) -> int:
    res = 0
    for i in range(0, len(input)):
        res += (2 ** i) * (1 if input[i] == "+" else 0)
    return res

def VertexRotation(vertex: int, rotation: str) -> int:
    return RotationalMapping[rotation].index(vertex)

def PerformRotation(inputs: list, rotation: str) -> list:
    result = []
    for i in range(0, len(RotationalMapping[rotation])):
        result.append(inputs[RotationalMapping[rotation][i]])
    return result

if __name__ == "__main__":
    main()