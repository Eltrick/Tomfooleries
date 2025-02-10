import copy
from functools import reduce

def nim_sum(state: list) -> int:
    return reduce(lambda a, b: a ^ b, state)

def iter(state: list) -> list:
    state_safe = copy.deepcopy(state)

    n_sum = nim_sum(state)
    if n_sum == 0:
        return [-1]

    y_val = [state[x] ^ n_sum for x in range(len(state))]
    for i in range(len(y_val)):
        if y_val[i] < state[i]:
            state_safe[i] = y_val
            return [[i, y_val[i]], state_safe, n_sum]

def solve():
    state = [int(x) for x in input("Initial state, separated by spaces: ").split(" ")]

    while sum(state) != 0:
        iteration = iter(state)
        print(f"Nim sum: {iteration[2]}")
        print(f"Action:  Reduce row {iteration[0][0]} to {iteration[0][1]}")
        state = iteration[1]
        new_inp = [int(x) for x in input("Input position that changed, and the new value of it: ")]
        state[new_inp[0]] = new_inp[1]

if __name__ == "__main__":
    solve()