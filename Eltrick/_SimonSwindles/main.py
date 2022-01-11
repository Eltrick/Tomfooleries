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
    print("Current Solution: " + "".join(SolutionArray) + " (obviously)")
    Constant = list(input("Input the Constant: "))
    N = 0
    coloursFound = 0
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
                        SolutionArray[i] = colourXor(Constant[i], "W")
                        coloursFound += 1
            print("After XOR'ing with the Output: " + "".join(SolutionArray))
            if RGBBool[0]:
                temp = SolutionArray[2] + SolutionArray[1] + SolutionArray[0]
                for i in range(0, 3):
                    SolutionArray[i] = temp[i]
                print("R is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[0]:
                temp = SolutionArray[5] + SolutionArray[4] + SolutionArray[3]
                for i in range(3, 6):
                    SolutionArray[i] = temp[i - 3]
                print("R is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[1]:
                for i in range(0, 3):
                    if SolutionArray[i] != "-":
                        SolutionArray[i] = colourXor(SolutionArray[i], "W")
                print("G is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[1]:
                for i in range(3, 6):
                    if SolutionArray[i] != "-":
                        SolutionArray[i] = colourXor(SolutionArray[i], "W")
                print("G is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[2]:
                SolutionArray[:] = SolutionArray[1:] + SolutionArray[:1]
                print("B is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[2]:
                SolutionArray[:] = SolutionArray[5:] + SolutionArray[:5]
                print("B is F, new answer is: " + "".join(SolutionArray))
        elif len(infoDump[0]) == 6:
            inputs = list(infoDump[0]).reverse()
            TrueResponse = list(infoDump[1])
            print("Reversing...")
            for i in range(0, len(inputs)):
                if inputs[i] == "K":
                    TrueResponse = list(infoDump[1]).reverse()
                    print("Black gives: " + "".join(TrueResponse))
                elif inputs[i] == "R":
                    for j in range(0, len(TrueResponse)):
                        TrueResponse[j] = invertR[ColourOrder.index(TrueResponse[j])]
                    print("Red gives: " + "".join(TrueResponse))
                elif inputs[i] == "G":
                    for j in range(0, len(TrueResponse)):
                        TrueResponse[j] = invertG[ColourOrder.index(TrueResponse[j])]
                    print("Green gives: " + "".join(TrueResponse))
                elif inputs[i] == "B":
                    for j in range(0, len(TrueResponse)):
                        TrueResponse[j] = invertB[ColourOrder.index(TrueResponse[j])]
                    print("Blue gives: " + "".join(TrueResponse))
                elif inputs[i] == "C":
                    TrueResponse[:] = TrueResponse[1:] + TrueResponse[:1]
                    print("Cyan gives: " + "".join(TrueResponse))
                elif inputs[i] == "M":
                    TrueResponse[:] = TrueResponse[5:] + TrueResponse[:5]
                    print("Magenta gives: " + "".join(TrueResponse))
                elif inputs[i] == "Y":
                    for j in range(0, len(TrueResponse)):
                        TrueResponse[j] = colourXor(TrueResponse[j], "W")
                    print("Yellow gives: " + "".join(TrueResponse))
                elif inputs[i] == "W":
                    temp = TrueResponse[2] + TrueResponse[1] + TrueResponse[0] + TrueResponse[5] + TrueResponse[4] + TrueResponse[3]
                    TrueResponse = list(temp)
                    print("White gives: " + "".join(TrueResponse))
            for i in range(0, len(TrueResponse)):
                TrueResponse[i] = colourXor(TrueResponse[i], infoDump[0][i])
            print("After XOR'ing with inputs, the True Response is: " + "".join(TrueResponse))
            for i in range(0, len(SolutionArray)):
                if SolutionArray[i] != "-":
                    SolutionArray[i] = colourXor(SolutionArray[i], infoDump[1][i])
                elif SolutionArray[i] == "-":
                    if TrueResponse[i] == colourXor(Constant[i], "W"):
                        SolutionArray[i] = colourXor(Constant[i], "W")
                        coloursFound += 1
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
                for i in range(0, 3):
                    SolutionArray[i] = temp[i]
                print("R is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[0]:
                temp = SolutionArray[5] + SolutionArray[4] + SolutionArray[3]
                for i in range(3, 6):
                    SolutionArray[i] = temp[i - 3]
                print("R is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[1]:
                for i in range(0, 3):
                    SolutionArray[i] = colourXor(SolutionArray[i], "W")
                print("G is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[1]:
                for i in range(3, 6):
                    SolutionArray[i] = colourXor(SolutionArray[i], "W")
                print("G is F, new answer is: " + "".join(SolutionArray))
            if RGBBool[2]:
                SolutionArray[:] = SolutionArray[1:] + SolutionArray[:1]
                print("B is T, new answer is: " + "".join(SolutionArray))
            elif not RGBBool[2]:
                SolutionArray[:] = SolutionArray[5:] + SolutionArray[:5]
                print("B is F, new answer is: " + "".join(SolutionArray))
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