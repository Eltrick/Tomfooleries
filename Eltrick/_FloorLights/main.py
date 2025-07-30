def R(p: list) -> list:
    o = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
    r = []
    for x in o:
        if p[0] + x[0] < 0 or p[0] + x[0] > 5:
            continue
        if p[1] + x[1] < 0 or p[1] + x[1] > 5:
            continue
        r.append([p[0] + x[0], p[1] + x[1]])
    return r

def G(p: list) -> list:
    o = [[0, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    r = []
    for x in o:
        if p[0] + x[0] < 0 or p[0] + x[0] > 5:
            continue
        if p[1] + x[1] < 0 or p[1] + x[1] > 5:
            continue
        r.append([p[0] + x[0], p[1] + x[1]])
    return r

def B(p: list) -> list:
    r = []
    for xo in range(-1, 2):
        for yo in range(-1, 2):
            if p[0] + xo < 0 or p[0] + xo > 5:
                continue
            if p[1] + yo < 0 or p[1] + yo > 5:
                continue
            r.append([p[0] + xo, p[1] + yo])
    return r

def coordToList(coord: str) -> list:
    row = int(coord[1]) - 1
    col = "ABCDEF".index(coord[0].upper())
    return [row, col]

def listToCoord(l: list) -> str:
    return "ABCDEF"[l[1]] + str(l[0] + 1)

def printGrid(g: list) -> list:
    l_grid = []
    l_log = []
    
    for i in range(len(g)):
        l_grid.append("".join(["1" if x == 1 else "0" for x in g[i]]))
        for j in range(len(g[i])):
            if g[i][j] == 1:
                l_log.append(listToCoord([i, j]))
    return ["\n".join(l_grid), " ".join(l_log)]

stage = 1
u_inp = input("Stage 1: ").upper()

state = [[0] * 6 for x in range(6)]

while u_inp != "END":
    u_inp_arr = u_inp.split(" ")
    for i in range(0, len(u_inp_arr), 2):
        adj = [R, G, B]["RGB".index(u_inp_arr[i])](coordToList(u_inp_arr[i + 1]))
        for x in range(len(adj)):
            state[adj[x][0]][adj[x][1]] ^= 1
    stage += 1
    u_inp = input(f"Stage {stage}: ").upper()

final = printGrid(state)
grid = final[0]
log = final[1]

print("\nGrid:\n" + grid)
print("Answer: " + log)