from sage.matrix.berlekamp_massey import berlekamp_massey

bitstring = input("Bitstring: ")
s = []
for i in range(0, len(bitstring)):
    s.append(GF(2)(int(bitstring[i])))

p = list(berlekamp_massey(s))[:-1]
print("".join([str(x) for x in p]))