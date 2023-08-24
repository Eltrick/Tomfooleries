def main() -> None:
    colourOrder = ["K", "B", "G", "C", "R", "M", "Y", "W"]

    stages = []
    stageCount = int(input("Number of modules on the bomb: "))
    for i in range(stageCount):
        stages.append([])
    
    done = False
    while not done:
        info = input("Stage Number + Gate + Colour + Grid: ").upper()
        if info == "END":
            done = True
            continue
        
        info = info.split(" ")
        actualGrid = []
        for i in range(len(info[3])):
            if info[3][i] == "1":
                actualGrid.append(True)
            else:
                actualGrid.append(False)
        
        stageNumber = int(info[0]) - 1

        if stageNumber != 0:
            stages[stageNumber] = [info[1], info[2], actualGrid]
        else:
            stages[stageNumber] = [info[1], info[2], info[3]]
    
    while(len(stages[-1]) == 0):
        stages.pop(-1)
    
    stages[0].append(True)
    for i in range(1, len(stages)):
        if i >= 2 and stages[i - 1][3] == stages[i - 2][3]:
            stages[i].append(not stages[i - 1][3])
        else:
            stages[i].append(determineValidity(stages[i][0], stages[i - 1][0]))
    
    colours = ["RMYW", "GCYW", "BCMW"]
    currentComponents = []
    for i in range(0, 3):
        comp = []
        for j in range(len(stages[0][2])):
            if stages[0][2][j] in colours[i]:
                comp.append(True)
            else:
                comp.append(False)
        currentComponents.append(comp)
    
    stagesToApply = [int(x) - 1 for x in input("Stages to apply: ").split(" ")]
    for i in range(len(stagesToApply)):
        if stages[stagesToApply[i]][3]:
            print("Stage #" + str(stagesToApply[i] + 1) + " is valid. Applying operator.")
            component = "RGB".index(stages[stagesToApply[i]][1])
            currentComponents[component] = bitwise(currentComponents[component], stages[stagesToApply[i]][2], stages[stagesToApply[i]][0])
        else:
            print("Stage #" + str(stagesToApply[i] + 1) + " is invalid. Ignoring.")
    
    finalGrid = []
    for i in range(len(currentComponents[0])):
        x = 0
        if currentComponents[0][i]:
            x += 4
        if currentComponents[1][i]:
            x += 2
        if currentComponents[2][i]:
            x += 1
        
        finalGrid.append(colourOrder[x])
    print("The final grid after modifications is: " + "".join(finalGrid))

def determineValidity(gate: str, previousGate: str) -> bool:
    gateOrder = ["AND", "NAND", "NIMPBY", "IMPBY", "XOR", "NOR", "OR", "NIMP", "IMP", "XNOR"]
    gateKeys = [["NAND", "NIMPBY", "IMPBY", "NOR"], ["NIMPBY", "IMPBY", "NOR", "OR"], ["IMPBY", "NOR", "OR", "NIMP"], ["NOR", "OR", "NIMP", "IMP"], ["XNOR", "XOR"], ["OR", "NIMP", "IMP", "AND"], ["NIMP", "IMP", "AND", "NAND"], ["IMP", "AND", "NAND", "NIMPBY"], ["AND", "NAND", "NIMPBY", "IMPBY"], ["XOR", "XNOR"]]

    return not (previousGate in gateKeys[gateOrder.index(gate)])

def bitwise(a: list, b: list, op: str) -> list:
    res = []
    for i in range(len(a)):
        res.append(False)
    
    for i in range(len(a)):
        if op == "AND":
            res[i] = a[i] & b[i]
        elif op == "NAND":
            res[i] = not (a[i] & b[i])
        elif op == "OR":
            res[i] = a[i] | b[i]
        elif op == "NOR":
            res[i] = not (a[i] | b[i])
        elif op == "IMP":
            res[i] = (not a[i]) | b[i]
        elif op == "NIMP":
            res[i] = not ((not a[i]) | b[i])
        elif op == "IMPBY":
            res[i] = a[i] | (not b[i])
        elif op == "NIMPBY":
            res[i] = not (a[i] | (not b[i]))
        elif op == "XOR":
            res[i] = a[i] ^ b[i]
        elif op == "XNOR":
            res[i] = not (a[i] ^ b[i])
    
    return res

if __name__ == "__main__":
    main()