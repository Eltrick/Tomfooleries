order = int(input("Last Digit: ")) % 2

dump = [int(x) for x in input("Digits: ").split(" ")]

sort_grid = sorted(dump)
result = []
if order == 1:
    sort_grid = sort_grid[::-1]
    for i in sort_grid:
        result.append(str(dump.index(i) + 1))
else:
    for i in sort_grid:
        result.append(str(dump.index(i) + 1))

print("press " + " ".join(result))