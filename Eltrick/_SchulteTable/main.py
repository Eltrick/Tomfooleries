order = int(input("Last Digit: ")) % 2

dump = input("Digits: ").split(" ")
for i in range(0, len(dump)):
    dump[i] = int(dump[i]) - 1

result = []
if order == 1:
    for i in range(0, len(dump)):
        result.append(str(dump.index(24 - i) + 1))
else:
    for i in range(0, len(dump)):
        result.append(str(dump.index(i) + 1))

print("press " + " ".join(result))