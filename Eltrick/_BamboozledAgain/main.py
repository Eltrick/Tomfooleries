import math

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Symbols = ["#", "'", "\"", "?", "-", "*", "~", "!"]
PossibleTexts = ["THE#LETTER", "ONE#LETTER", "THE#COLOUR", "ONE#COLOUR", "THE#PHRASE", "ONE#PHRASE", "THEN", "NEXT", "ALPHA", "BRAVO", "CHARLIE", "DELTA", "ECHO", "GOLF", "KILO", "QUEBEC", "TANGO", "WHISKEY", "VICTOR", "YANKEE", "ECHO#ECHO", "E#THEN#E", "ALPHA#PAPA", "PAPA#ALPHA", "PAPHA#ALPA", "T#GOLF", "TANGOLF", "WHISKEE", "WHISKY", "CHARLIE#C", "C#CHARLIE", "YANGO", "DELTA#NEXT", "CUEBEQ", "MILO", "KI#LO", "HI-LO", "VVICTOR", "VICTORR", "LIME#BRAVO", "BLUE#BRAVO", "G#IN#JADE", "G#IN#ROSE", "BLUE#IN#RED", "YES#BUT#NO", "COLOUR", "MESSAGE", "CIPHER", "BUTTON", "TWO#BUTTONS", "SIX#BUTTONS", "I#GIVE#UP", "ONE#ELEVEN", "ONE#ONE#ONE", "THREE#ONES", "WHAT?", "THIS?", "THAT?", "BLUE!", "ECHO!", "BLANK", "BLANK?!", "NOTHING", "YELLOW#TEXT", "BLACK#TEXT?", "QUOTE#V", "END#QUOTE", "\"QUOTE#K\"", "IN#RED", "ORANGE", "IN#YELLOW", "LIME", "IN#GREEN", "JADE", "IN#CYAN", "AZURE", "IN#BLUE", "VIOLET", "IN#MAGENTA", "ROSE"]
PossibleValues = [40, 24, 32, 39, 20, 15, 0, 0, 70, 84, 83, 61, 66, 46, 68, 56, 80, 54, 65, 41, 84, 60, 56, 86, 69, 50, 62, 78, 64, 43, 41, 51, 47, 57, 45, 46, 86, 84, 82, 78, 47, 59, 63, 42, 89, 77, 70, 55, 67, 79, 71, 58, 86, 58, 88, 49, 78, 68, 75, 45, 44, 56, 72, 70, 46, 73, 66, 52, 48, 69, 41, 58, 84, 47, 45, 55, 83, 74, 51, 67]
PossibleCValues = [11, 12, 13, 14, 15, 16]
PossibleColours = ["WHITE", "RED", "ORANGE", "YELLOW", "LIME", "GREEN", "JADE", "GREY", "BLACK", "CYAN", "AZURE", "BLUE", "VIOLET", "MAGENTA", "ROSE", "GREY"]
PossibleTextColours = ["WHITE", "RED", "ORANGE", "YELLOW", "LIME", "GREEN", "JADE", "GREY", "CYAN", "AZURE", "BLUE", "VIOLET", "MAGENTA", "ROSE"]
ButtonPositions = ["TL", "TM", "TR", "BL", "BM", "BR"]
X = [0, 0, 0]
Y = [0, 0, 0]
FinalPressTable = [["#", "'", "\"", "?", "-", "*", "~", "!"], ["'", "'", "?", "-", "*", "~", "!", "#"], ["\"", "?", "\"", "*", "~", "!", "#", "'"], ["?", "-", "*", "?", "!", "#", "'", "\""], ["-", "*", "~", "!", "-", "'", "\"", "?"], ["*", "~", "!", "#", "'", "*", "?", "-"], ["~", "!", "#", "'", "\"", "?", "~", "*"], ["!", "#", "'", "\"", "?", "-", "*", "!"]]

def Main() -> None:
    global Alphabet
    global Symbols
    global PossibleTexts
    global PossibleValues
    global PossibleCValues
    global PossibleColours
    global PossibleTextColours
    global ButtonPositions
    global X
    global Y

    DecryptedTexts = ["", "", "", "", "", "", "", ""]
    DecryptedSymbols = ["", "", "", "", "", "", "", ""]
    TextColours = ["", "", "", "", "", "", "", ""]
    RawTextValues = [0, 0, 0, 0, 0, 0, 0, 0]
    ModifiedTextValues = [0, 0, 0, 0, 0, 0, 0, 0]
    FinalTextValues = [0, 0, 0, 0, 0, 0, 0, 0]
    AValues = [0, 0, 0, 0, 0, 0, 0, 0]
    BValues = [0, 0, 0, 0, 0, 0, 0, 0]
    CValues = [0, 0, 0, 0, 0, 0, 0, 0]

    print("Command format: <Boozleglyph_Set> <Encrypted_Display_Text> <Encrypted_Appended_Symbol> <Colour>")
    infoDump = ["", "", "", "", "", "", "", ""]

    # Get information
    for i in range(0, len(infoDump)):
        infoDump[i] = input("Enter display " + str(i+1) + "'s information: ").upper().split(" ")
        CValues[i] = PossibleCValues[Alphabet.index(infoDump[i][0])]
    
    # Decrypts texts
    for i in range(0, len(infoDump)):
        encryptedText = infoDump[i][1]
        possibleDecryptedText = ""
        testBValue = 1
        while(DecryptedTexts[i] not in PossibleTexts):
            possibleDecryptedText = ModifiedCaesar(encryptedText, -testBValue)
            for j in range(0, len(possibleDecryptedText)):
                if ShiftText(possibleDecryptedText, -j) in PossibleTexts:
                    if testBValue > 26:
                        print("Something went horribly wrong with Display Text #" + str(i + 1) + ". Please check that you have everything correctly.")
                        exit()
                    AValues[i] = j
                    BValues[i] = testBValue
                    DecryptedTexts[i] = ShiftText(possibleDecryptedText, -j)
                    break
            testBValue += 1
    print("Decrypted Texts are: " + str(DecryptedTexts))
    print("A Values are: " + str(AValues))
    print("B Values are: " + str(BValues))
    print("C Values are: " + str(CValues))

    # Decrypts appended symbols using found keys
    for i in range(0, len(infoDump)):
        DecryptedSymbols[i] = ModifiedCaesar(infoDump[i][2], -BValues[i])
    print("Decrypted Symbols are: " + str(DecryptedSymbols))
    
    # Stores colours (pun not intended)
    for i in range(0, len(infoDump)):
        TextColours[i] = infoDump[i][3]
    
    # Gets raw text velues
    for i in range(0, len(DecryptedTexts)):
        RawTextValues[i] = PossibleValues[PossibleTexts.index(DecryptedTexts[i])]
    print("Raw Text Values are: " + str(RawTextValues))
    
    # Modifies text values
    for i in range(0, len(RawTextValues)):
        if not (i == 1 or i == 3):
            ModifiedTextValues[i] = ModifyTextValues(RawTextValues[i], TextColours[i])
    print("Therefore, Modified Text Values are: " + str(ModifiedTextValues))

    # Calculates final values of each text that can be evaluated
    for i in range(0, len(ModifiedTextValues)):
        FinalTextValues[i] = ModifiedTextValues[i] + 5 * AValues[i] + 2 * (BValues[i] + CValues[i])
    print("Final Text Values of each text are: " + str(FinalTextValues))
    print("--------------------------------BUTTONS--------------------------------")
    print("Command format: <Colour> <Text>")
    print("<Text> MUST include # in place of spaces!!")
    InitialButtonValues = [0, 0, 0, 0, 0, 0]
    FinalButtonValues = [0, 0, 0, 0, 0, 0]
    buttonInfoDump = ["", "", "", "", "", ""]
    T = [[6, 7, 8, 6, 7, 8], [1, 3, 3, 5, 5, 1], [1, 1, 3, 3, 5, 5]]
    # Gets button information
    for i in range(0, len(buttonInfoDump)):
        buttonInfoDump[i] = input("Enter " + ButtonPositions[i] + " button's information: ").upper().split(" ")
    for buttonPressCount in range(0, 4):
        # Calculates Initial Button Values
        for i in range(0, len(InitialButtonValues)):
            InitialButtonValues[i] = ButtonCalculations(buttonInfoDump[i][1], buttonInfoDump[i][0], DecryptedTexts, TextColours)
        print("Initial Button Values are: " + str(InitialButtonValues))

        # Calculates final button values
        for i in range(0, len(FinalButtonValues)):
            FinalButtonValues[i] = 3 * InitialButtonValues[i] + 2 * (FinalTextValues[T[0][i] - 1] + FinalTextValues[T[1][i] - 1] + FinalTextValues[T[2][i] - 1])
        print("Final Button Values are: " + str(FinalButtonValues))

        SortedFinalButtonValues = [0, 0, 0, 0, 0, 0]
        for i in range(0, len(SortedFinalButtonValues)):
            SortedFinalButtonValues[i] = FinalButtonValues[i]
        SortedFinalButtonValues.sort()

        # Gets answer
        answer = FinalButtonValues.index(SortedFinalButtonValues[buttonPressCount + 2])
        timeToPress = CalculateTime(buttonInfoDump[answer][1], buttonInfoDump[answer][0], buttonPressCount, DecryptedTexts, DecryptedSymbols, TextColours)
        print("Press the " + ButtonPositions[answer] + " button when " + timeToPress)

        if buttonPressCount == 3:
            break

        print("--------------------------------INFORMATION_CHANGE--------------------------------")

        # After pressing the button, it changes
        buttonInfoDump[answer] = input("Enter the " + ButtonPositions[answer] + " button's new information: ").upper().split(" ")
    print("The module should now solve. The End.")
    exit()
    
def ButtonCalculations(buttonText, buttonColour, DecryptedTexts: list, TextColours: list) -> int:
    buttonValue = 0
    # Rule 1
    if buttonColour == "BLACK":
        buttonValue = 30
    elif buttonColour == "WHITE" or buttonColour == "GREY":
        buttonValue = 20
    else:
        buttonValue = 0

    # Rule 2
    if buttonColour in buttonText:
        buttonValue += 70
    elif PossibleColours[(PossibleColours.index(buttonColour) + 8) % len(PossibleColours)] in buttonText:
        buttonValue += 35
    else:
        anyColour = False
        for j in range(0, len(PossibleColours)):
            if PossibleColours[j] in buttonText:
                anyColour = True
        if "COLOUR" in buttonText:
            anyColour = True
        if anyColour:
            buttonValue += 5
    
    # Rule 3
    for j in range(0, len(DecryptedTexts)):
        if DecryptedTexts[j] == buttonText:
            buttonValue += 60
    
    # Rule 4
    for j in range(0, len(TextColours)):
        if buttonColour == TextColours[j]:
            buttonValue += 15
    
    # Rule 5
    if buttonColour != "GREY":
        for j in range(0, len(TextColours)):
            if PossibleColours[(PossibleColours.index(buttonColour) + 8) % len(PossibleColours)] == TextColours[j]:
                buttonValue += 10

    return buttonValue

def ModifiedCaesar(s: str, off: int) -> str:
    res = ""
    for i in range(0, len(s)):
        if s[i] in Alphabet:
            res += Alphabet[(Alphabet.index(s[i]) + off) % 26]
        elif s[i] in Symbols:
            res += Symbols[(Symbols.index(s[i]) + off) % 8]
    return res

def ShiftText(s: str, off: int) -> str:
    res = s[off:] + s[:off]
    return res

def ModifyTextValues(val: int, rule: str) -> int:
    res = 0
    if rule == "WHITE":
        res = val
    elif rule == "RED":
        res = val - math.floor(val / 10)
    elif rule == "ORANGE":
        res = int(str(val)[0] + str(val)[0])
    elif rule == "YELLOW":
        res = val + (val % 10)
    elif rule == "LIME":
        res = val - max(int(str(val)[0]), int(str(val)[1]))
    elif rule == "GREEN":
        res = val - (int(str(val)[0]) + int(str(val)[1]))
    elif rule == "JADE":
        res = val - (2 * int(str(val)[0]))
    elif rule == "GREY":
        res = int(str(val)[1] + str(val)[0])
    elif rule == "CYAN":
        res = val - (val % 10)
    elif rule == "AZURE":
        res = int(str(val)[1] + str(val)[1])
    elif rule == "BLUE":
        res = val + math.floor(val / 10)
    elif rule == "VIOLET":
        res = val - min(int(str(val)[0]), int(str(val)[1]))
    elif rule == "MAGENTA":
        res = val - abs(int(str(val)[0]) - int(str(val)[1]))
    elif rule == "ROSE":
        res = val - (2 * int(str(val)[1]))
    return res

def ModifyButtonValue(val: int, rule: str) -> int:
    res = 0
    valStr = str(val)
    if val < 10:
        valStr = "0" + valStr
    if rule == "WHITE":
        res = max(int(valStr[0]), int(valStr[1]))
    elif rule == "RED":
        res = int(valStr[0]) - int(valStr[1])
    elif rule == "ORANGE":
        res = val % 9
        if res == 0:
            res = 9
    elif rule == "YELLOW":
        res = int(valStr[0])
    elif rule == "LIME":
        digitalRoot = val % 9
        if digitalRoot == 0:
            digitalRoot = 9
        res = int(valStr[0]) - digitalRoot
    elif rule == "GREEN":
        res = int(valStr[0]) + int(valStr[1])
    elif rule == "JADE":
        res = 2 * int(valStr[0])
    elif rule == "GREY":
        digitalRoot = val % 9
        if digitalRoot == 0:
            digitalRoot = 9
        res = int(valStr[0]) + int(valStr[1]) - digitalRoot
    elif rule == "CYAN":
        res = int(valStr[1]) - int(valStr[0])
    elif rule == "AZURE":
        res = val % 9
        if res == 0:
            res = 9
        res *= -1
    elif rule == "BLUE":
        res = int(valStr[1])
    elif rule == "VIOLET":
        digitalRoot = val % 9
        if digitalRoot == 0:
            digitalRoot = 9
        res = int(valStr[1]) - digitalRoot
    elif rule == "MAGENTA":
        res = 10 - (int(valStr[0]) + int(valStr[1]))
    elif rule == "ROSE":
        res = 2 * int(valStr[1])
    elif rule == "BLACK":
        res = min(int(valStr[0]), int(valStr[1]))
    return res

def LogTime(YValue: int, symbol: str) -> str:
    res = ""
    if symbol == "#":
        res = "the last digit of the timer is " + str(YValue % 10)
    elif symbol == "'":
        res = "the sum of the last two digits of the timer is " + str((YValue % 9) + 3)
    elif symbol == "\"":
        res = "the sum of the last two digits of the timer is " + str(((2 * YValue) % 9) + 3)
    elif symbol == "?":
        res = "the difference between the last two digits of the timer is " + str(YValue % 5)
    elif symbol == "-":
        res = "the last digit of the timer is " + str(9 - (YValue % 10))
    elif symbol == "*":
        res = "the sum of the last two digits of the timer is " + str(11 - (YValue % 9))
    elif symbol == "~":
        res = "the sum of the last two digits of the timer is " + str(11 - ((2 * YValue) % 9))
    elif symbol == "!":
        res = "the difference between the last two digits of the timer is " + str((2 * YValue) % 5)
    return res

def CalculateTime(buttonText: str, buttonColour: str, buttonsPressed: int, displayTexts: list, symbols: list, displayColours: list) -> str:
    answerTime = ""
    if buttonsPressed == 1:
        print(str(buttonsPressed) + " button have been pressed.")
    else:
        print(str(buttonsPressed) + " buttons have been pressed.")
    if buttonsPressed != 3:
        rawValue = PossibleValues[PossibleTexts.index(buttonText)]
        print("Raw value: " + str(rawValue))
        X[buttonsPressed] = ModifyButtonValue(rawValue, buttonColour)
        Y[buttonsPressed] = 0
        if buttonsPressed == 0:
            Y[buttonsPressed] = X[buttonsPressed]
        elif buttonsPressed == 1:
            if displayTexts[1] == "THEN":
                Y[buttonsPressed] = X[buttonsPressed] + X[buttonsPressed - 1]
            elif displayTexts[1] == "NEXT":
                Y[buttonsPressed] = X[buttonsPressed] - X[buttonsPressed - 1]
        elif buttonsPressed == 2:
            if displayTexts[3] == "THEN":
                Y[buttonsPressed] = X[buttonsPressed] + Y[buttonsPressed - 1]
            elif displayTexts[3] == "NEXT":
                Y[buttonsPressed] = X[buttonsPressed] - Y[buttonsPressed - 1]
        print("X = " + str(X[buttonsPressed]))
        print("Y = " + str(Y[buttonsPressed]))
        answerTime = LogTime(Y[buttonsPressed], symbols[7 - buttonsPressed])
    elif buttonsPressed == 3:
        rawValue = PossibleValues[PossibleTexts.index(buttonText)]
        S1 = ModifyTextValues(rawValue, displayColours[1])
        S2 = ModifyTextValues(rawValue, displayColours[3])
        print("S1 = " + str(S1))
        print("S2 = " + str(S2))
        X1 = ModifyButtonValue(S1, buttonColour)
        X2 = ModifyButtonValue(S2, buttonColour)
        print("X1 = " + str(X1))
        print("X2 = " + str(X2))
        YVal = 0
        if displayTexts[1] == displayTexts[3]:
            YVal = X1 + X2
            print("Displays 2 and 4 are the same, Y = " + str(YVal))
        else:
            YVal = abs(X1 - X2)
            print("Displays 2 and 4 are the different, Y = " + str(YVal))
        FinalSymbol = FinalPressTable[Symbols.index(symbols[1])][Symbols.index(symbols[3])]
        answerTime = LogTime(YVal, FinalSymbol)
    return answerTime

if __name__ == "__main__":
    Main()