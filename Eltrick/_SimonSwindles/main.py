import math

ColourOrder = ["K", "B", "G", "C", "R", "M", "Y", "W"]
invertR = ["R", "M", "Y", "W", "K", "B", "G", "C"]
invertG = ["G", "C", "K", "B", "Y", "W", "R", "M"]
invertB = ["B", "K", "C", "G", "M", "R", "W", "Y"]

def main() -> None:
    global ColourOrder
    
    RGBBool = [False, False, False]
    SolutionArray = ["-", "-", "-", "-", "-", "-"]
    print("Welcome, I wish you the best of luck on your journey.")
    print("---------------------------------<INITIALISATION>----------------------------------")
    print("Current Solution: " + "".join(SolutionArray) + " (ob3viously)")
    Constant = list(input("Input the Constant: "))
    N = 0
    coloursFound = 0
    Impossibles = [[], [], [], [], [], []]
    print("-----------------------------------<THE_TEDIUM>------------------------------------")
    while True:
        print("-------------------------------------<N = " + str(N) + ">--------------------------------------")
        infoDump = input("Input the sequence of colours that was queried, and Simon's response: ").upper().split(" ")
        TrueResponse = ""
        if len(infoDump[0]) == 1:
            for i in range(0, len(infoDump[1])):
                TrueResponse += colourXor(infoDump[0], infoDump[1][i])
            print("Simon's True Response: " + TrueResponse)
            if infoDump[0] in "RMYW":
                RGBBool[0] = True
            else:
                RGBBool[0] = False
            if infoDump[0] in "GCYW":
                RGBBool[1] = True
            else:
                RGBBool[1] = False
            if infoDump[0] in "BCMW":
                RGBBool[2] = True
            else:
                RGBBool[2] = False
            for i in range(0, len(SolutionArray)):
                if SolutionArray[i] != "-":
                    SolutionArray[i] = colourXor(SolutionArray[i], infoDump[1][i])
                else:
                    if TrueResponse[i] == colourXor(Constant[i], "W"):
                        SolutionArray[i] = colourXor(infoDump[0], infoDump[1][i])
                        coloursFound += 1
                    else:
                        for j in range(0, len(Impossibles[i])):
                            Impossibles[i][j] = colourXor(Impossibles[i][j], infoDump[1][i])
                        Impossibles[i].append(colourXor(infoDump[0], infoDump[1][i]))
            print("After XORing with the Output: " + "".join(SolutionArray))
            if RGBBool[0]:
                temp = SolutionArray[2] + SolutionArray[1] + SolutionArray[0]
                temp2 = []
                temp2.append(Impossibles[2])
                temp2.append(Impossibles[1])
                temp2.append(Impossibles[0])
                for i in range(0, 3):
                    SolutionArray[i] = temp[i]
                    Impossibles[i] = temp2[i].copy()
                print("R is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[0]:
                temp = SolutionArray[5] + SolutionArray[4] + SolutionArray[3]
                temp2 = []
                temp2.append(Impossibles[5])
                temp2.append(Impossibles[4])
                temp2.append(Impossibles[3])
                for i in range(3, 6):
                    SolutionArray[i] = temp[i - 3]
                    Impossibles[i] = temp2[i - 3].copy()
                print("R is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[1]:
                for i in range(0, 3):
                    if SolutionArray[i] != "-":
                        SolutionArray[i] = colourXor(SolutionArray[i], "W")
                    for j in range(0, len(Impossibles[i])):
                        Impossibles[i][j] = colourXor(Impossibles[i][j], "W")
                print("G is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[1]:
                for i in range(3, 6):
                    if SolutionArray[i] != "-":
                        SolutionArray[i] = colourXor(SolutionArray[i], "W")
                    for j in range(0, len(Impossibles[i])):
                        Impossibles[i][j] = colourXor(Impossibles[i][j], "W")
                print("G is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[2]:
                SolutionArray[:] = SolutionArray[1:] + SolutionArray[:1]
                Impossibles[:] = Impossibles[1:] + Impossibles[:1]
                print("B is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[2]:
                SolutionArray[:] = SolutionArray[5:] + SolutionArray[:5]
                Impossibles[:] = Impossibles[5:] + Impossibles[:5]
                print("B is F, new answer is: " + "".join(SolutionArray))
            possibleLogging = []
            for i in range(0, len(Impossibles)):
                Impossibles[i] = list(set(Impossibles[i]))
                p = []
                for j in range(0, len("RGBCMYWK")):
                    if "RGBCMYWK"[j] not in Impossibles[i]:
                        p.append("RGBCMYWK"[j])
                possibleLogging.append("".join(p))
            print("Possible colours for each position is: " + ";".join(possibleLogging))
        elif len(infoDump[0]) == 6:
            inputs = list(infoDump[0])
            ConstantCopy = ["", "", "", "", "", ""]
            for i in range(0, len(ConstantCopy)):
                ConstantCopy[i] = Constant[i]
            print("Constant before modifications is: " + "".join(ConstantCopy))
            for i in range(0, len(inputs)):
                if inputs[i] == "K":
                    ConstantCopy = ConstantCopy[::-1]
                    print("K gives: " + "".join(ConstantCopy))
                elif inputs[i] == "R":
                    for j in range(0, len(ConstantCopy)):
                        ConstantCopy[j] = colourXor(ConstantCopy[j], "R")
                    print("R gives: " + "".join(ConstantCopy))
                elif inputs[i] == "G":
                    for j in range(0, len(ConstantCopy)):
                        ConstantCopy[j] = colourXor(ConstantCopy[j], "G")
                    print("G gives: " + "".join(ConstantCopy))
                elif inputs[i] == "B":
                    for j in range(0, len(ConstantCopy)):
                        ConstantCopy[j] = colourXor(ConstantCopy[j], "B")
                    print("B gives: " + "".join(ConstantCopy))
                elif inputs[i] == "C":
                    ConstantCopy[:] = ConstantCopy[1:] + ConstantCopy[:1]
                    print("C gives: " + "".join(ConstantCopy))
                elif inputs[i] == "M":
                    ConstantCopy[:] = ConstantCopy[-1:] + ConstantCopy[:-1]
                    print("M gives: " + "".join(ConstantCopy))
                elif inputs[i] == "Y":
                    for j in range(0, len(ConstantCopy)):
                        ConstantCopy[j] = colourXor(ConstantCopy[j], "W")
                    print("Y gives: " + "".join(ConstantCopy))
                elif inputs[i] == "W":
                    temp = ConstantCopy[2] + ConstantCopy[1] + ConstantCopy[0] + ConstantCopy[5] + ConstantCopy[4] + ConstantCopy[3]
                    ConstantCopy = list(temp)
                    print("W gives: " + "".join(ConstantCopy))
            for i in range(0, len(ConstantCopy)):
                ConstantCopy[i] = colourXor(ConstantCopy[i], infoDump[0][i])
            print("After XORing with inputs gives: " + "".join(ConstantCopy))
            for i in range(0, len(SolutionArray)):
                if SolutionArray[i] != "-":
                    SolutionArray[i] = colourXor(SolutionArray[i], infoDump[1][i])
                elif SolutionArray[i] == "-":
                    if infoDump[1][i] == colourXor(ConstantCopy[i], "W"):
                        SolutionArray[i] = colourXor(infoDump[0][i], infoDump[1][i])
                        coloursFound += 1
                    else:
                        for j in range(0, len(Impossibles[i])):
                            Impossibles[i][j] = colourXor(Impossibles[i][j], infoDump[1][i])
                        Impossibles[i].append(colourXor(infoDump[0][i], infoDump[1][i]))
            print("After finding opposites and XORing with output, the new current answer is: " + "".join(SolutionArray))
            if infoDump[0][N % 6] in "RMYW":
                RGBBool[0] = True
            else:
                RGBBool[0] = False
            if infoDump[0][N % 6] in "GCYW":
                RGBBool[1] = True
            else:
                RGBBool[1] = False
            if infoDump[0][N % 6] in "BCMW":
                RGBBool[2] = True
            else:
                RGBBool[2] = False
            if RGBBool[0]:
                temp = SolutionArray[2] + SolutionArray[1] + SolutionArray[0]
                temp2 = []
                temp2.append(Impossibles[2])
                temp2.append(Impossibles[1])
                temp2.append(Impossibles[0])
                for i in range(0, 3):
                    SolutionArray[i] = temp[i]
                    Impossibles[i] = temp2[i].copy()
                print("R is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[0]:
                temp = SolutionArray[5] + SolutionArray[4] + SolutionArray[3]
                temp2 = []
                temp2.append(Impossibles[5])
                temp2.append(Impossibles[4])
                temp2.append(Impossibles[3])
                for i in range(3, 6):
                    SolutionArray[i] = temp[i - 3]
                    Impossibles[i] = temp2[i - 3].copy()
                print("R is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[1]:
                for i in range(0, 3):
                    if SolutionArray[i] != "-":
                        SolutionArray[i] = colourXor(SolutionArray[i], "W")
                    for j in range(0, len(Impossibles[i])):
                        Impossibles[i][j] = colourXor(Impossibles[i][j], "W")
                print("G is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[1]:
                for i in range(3, 6):
                    if SolutionArray[i] != "-":
                        SolutionArray[i] = colourXor(SolutionArray[i], "W")
                    for j in range(0, len(Impossibles[i])):
                        Impossibles[i][j] = colourXor(Impossibles[i][j], "W")
                print("G is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[2]:
                SolutionArray[:] = SolutionArray[1:] + SolutionArray[:1]
                Impossibles[:] = Impossibles[1:] + Impossibles[:1]
                print("B is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[2]:
                SolutionArray[:] = SolutionArray[5:] + SolutionArray[:5]
                Impossibles[:] = Impossibles[5:] + Impossibles[:5]
                print("B is F, new answer is: " + "".join(SolutionArray))
            possibleLogging = []
            for i in range(0, len(Impossibles)):
                Impossibles[i] = list(set(Impossibles[i]))
                p = []
                for j in range(0, len("RGBCMYWK")):
                    if "RGBCMYWK"[j] not in Impossibles[i]:
                        p.append("RGBCMYWK"[j])
                possibleLogging.append("".join(p))
            print("Possible colours for each position is: " + ";".join(possibleLogging))
        elif infoDump[0] == "END":
            if coloursFound == 6:
                print("All six colours found! Solution: " + "".join(SolutionArray))
                exit()
            else:
                print("Cannot end here because you have only found " + str(coloursFound) + "/6 colours.")
        N += 1
    

def colourXor(X: str, Y: str) -> str:
    Z = ColourOrder.index(X) ^ ColourOrder.index(Y)
    return ColourOrder[Z]

if __name__ == "__main__":
    main()