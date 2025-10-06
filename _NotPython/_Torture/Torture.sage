modulus = int(input("Modulus: "))
states = input("All N+1 states, ;: ").split(";")

if "," in states[0]:
    for i in range(0, len(states)):
        states[i] = states[i].split(",")
        for j in range(0, len(states[i])):
            states[i][j] = states[i - 1][j] if states[i][j] == "-" else int(states[i][j])
else:
    for i in range(0, len(states)):
        states[i] = list(states[i])
        for j in range(0, len(states[i])):
            states[i][j] = states[i - 1][j] if states[i][j] == "-" else int(states[i][j])

differences = []
for i in range(0, len(states[0])):
    x = []
    for j in range(0, len(states[0])):
        x.append(0)
    differences.append(x)

for i in range(0, len(differences)):
    for j in range(0, len(differences[i])):
        differences[i][j] = (states[i + 1][j] - states[i][j]) % modulus

finals = []
for i in range(0, len(states[0])):
    x = []
    for j in range(0, len(states[0])):
        x.append(0)
    finals.append(x)

for i in range(0, len(finals)):
    for j in range(0, len(finals[i])):
        finals[j][i] = differences[i][j]

finalState = [(modulus - x) % modulus for x in states[-1]]
A = matrix(Integers(modulus), finals)
V = vector(Integers(modulus), finalState)

def Trial(A, V, trial):
    x = []
    for i in range(0, len(differences)):
        x.append(1)
    try:
        if(trial != modulus):
            A \ V
            print(str((-trial) % modulus) + ": " + str(A \ V))
            Trial(A, V - vector(Integers(modulus), x), trial + 1)
    except Exception as e:
        Trial(A, V - vector(Integers(modulus), x), trial + 1)


Trial(A, V, 0)

while True:
    u_inp = vector(Integers(modulus), [(modulus - int(x)) % modulus for x in list(input("Another state: "))])
    Trial(A, u_inp, 0)