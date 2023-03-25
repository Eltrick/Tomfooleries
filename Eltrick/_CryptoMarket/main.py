import math

def main() -> None:
    finalValues = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    fluctuations = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    volatility = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    volatileScores = [[], [], [], []]
    maxScores = [0, 0, 0, 0]
    minScores = [0, 0, 0, 0]
    volatilityRanking = [0, 0, 0, 0]
    volatilityOrder = []
    maxValues = []
    minValues = []
    totalScores = [0, 0, 0, 0]
    kc = int(input("Number at the bottom: "))

    for i in range(0, len(finalValues)):
        finalValues[i][-1] = int(input("Final value of Crypto #" + str(i + 1) + ": "))
    for i in range(0, len(fluctuations)):
        fluctuations[i] = input("Crypto #" + str(i + 1) + " fluctuations: ").split(" ")
    
    for i in range(0, len(finalValues)):
        for j in range(0, len(finalValues[i]) - 1):
            finalValues[i][3 - j] = PerformReverseOperation(finalValues[i][4 - j], fluctuations[i][3 - j])

    for i in range(0, len(finalValues)):
        maxValues.append([max(finalValues[i][1:]), i])
        minValues.append([min(finalValues[i][1:]), i])
    
    maxValues = sorted(maxValues, key=lambda x: x[0], reverse=True)
    minValues = sorted(minValues, key=lambda x: x[0], reverse=True)

    for i in range(0, len(maxValues)):
        maxScores[maxValues[i][1]] = 12 - (3 * i)
        minScores[minValues[i][1]] = 12 - (3 * i)
    
    for i in range(0, len(volatility)):
        for j in range(0, len(volatility[i])):
            volatility[i][j] = math.trunc((int(fluctuations[i][j]) / finalValues[i][j]) * 100)
        volatility[i] = sorted(volatility[i], reverse=True)
        volatileScores[i] = [(volatility[i][0] - volatility[i][-1]), i]
    
    volatileScores = sorted(volatileScores, key=lambda x: x[0])
    print("Volatility: " + str(volatileScores))
    if volatileScores[0][0] == volatileScores[1][0]:
        if volatileScores[0][0] == volatileScores[2][0]:
            if volatileScores[0][0] == volatileScores[3][0]:
                volatilityOrder = [10, 10, 10, 10]
            else:
                volatilityOrder = [12, 12, 12, 4]
        elif volatileScores[2][0] == volatileScores[3][0]:
            volatilityOrder = [14, 14, 6, 6]
        else:
            volatilityOrder = [14, 14, 8, 4]
    elif volatileScores[1][0] == volatileScores[2][0]:
        if volatileScores[1][0] == volatileScores[3][0]:
            volatilityOrder = [16, 8, 8, 8]
        else:
            volatilityOrder = [16, 10, 10, 4]
    elif volatileScores[2][0] == volatileScores[3][0]:
        volatilityOrder = [16, 12, 6, 6]
    else:
        volatilityOrder = [16, 12, 8, 4]
    
    for i in range(0, len(volatileScores)):
        volatilityRanking[volatileScores[i][1]] = volatilityOrder[i]
    
    for i in range(0, len(totalScores)):
        totalScores[i] = maxScores[i] + minScores[i] + volatilityRanking[i]
    
    print("Peak Value Ranking, in order, is: " + str(maxScores))
    print("Slump Value Ranking, in order, is: " + str(minScores))
    print("Volatility Ranking, in order, is: " + str(volatilityRanking))
    print("Total score, in order, is: " + str(totalScores))
    
    for x in range(20, 36):
        j = []
        for i in range(0, len(totalScores)):
            j.append(math.floor((totalScores[i] * x) / 100))
        if ((j[0] * finalValues[0][-1]) + (j[1] * finalValues[1][-1]) + (j[2] * finalValues[2][-1]) + (j[3] * finalValues[3][-1]) == kc):
            print("X = " + str(x))
            print("Therefore, A, B, C, and D are: " + str(j))

    
def PerformReverseOperation(value: int, operation: str) -> int:
    if "+" in operation:
        return value - int(operation[1:])
    elif "-" in operation:
        return value + int(operation[1:])
    elif "*" in operation:
        return math.floor(value / int(operation[1:]))
    elif "/" in operation:
        return value * int(operation[1:])

if __name__ == "__main__":
    main()