states = input("All N+1 states, ;: ").split(";")

for i in range(0, len(states)):
    states[i] = [int(x) for x in states[i]]

differences = []
for i in range(0, len(states[0])):
    x = []
    for j in range(0, len(states[0])):
        x.append(0)
    differences.append(x)

for i in range(0, len(differences)):
    for j in range(0, len(differences[i])):
        differences[i][j] = (states[i + 1][j] - states[i][j]) % 10


finals = []
for i in range(0, len(states[0])):
    x = []
    for j in range(0, len(states[0])):
        x.append(0)
    finals.append(x)

for i in range(0, len(finals)):
    for j in range(0, len(finals[i])):
        finals[j][i] = differences[i][j]

finalState = [(10 - x) % 10 for x in states[-1]]
A = matrix(Integers(10), finals)
V = vector(Integers(10), finalState)

def Trial(A, V, trial):
    x = []
    for i in range(0, len(differences)):
        x.append(1)
    try:
        if(trial != 10):
            A \ V
            print(str((-trial) % 10) + ": " + str(A \ V))
            Trial(A, V - vector(Integers(10), x), trial + 1)
    except Exception as e:
        Trial(A, V - vector(Integers(10), x), trial + 1)


Trial(A, V, 0)

