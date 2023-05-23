from time import time


def calc(b, used, s, it, out):
    for n in range(b):
        if used[n]: continue
        ns = s * b + n
        if ns % it != 0: continue
        if it == b:
            out.append(ns)
            return
        else:
            used[n] = True
            calc(b, used, ns, it + 1, out)
            used[n] = False


BASE = int(input("Input base: "))

time_start = time()
print(time_start)
print()

res = []
calc(BASE, [False for _ in range(BASE)], 0, 1, res)

print()
print(time() - time_start)
# print(res)
for n in res:
    bs = []
    for k in range(BASE):
        bs.append(n % BASE)
        n //= BASE
    print(bs[-1:0:-1])