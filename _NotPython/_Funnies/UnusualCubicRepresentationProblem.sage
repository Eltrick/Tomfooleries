N = int(input("N = "))
m = int(input("m = "))

a = 4*N*N + 12*N - 3
b = 32*(N + 3)
ee=EllipticCurve([0, a, 0, b, 0])
P = ee.gens()[0]
print("Found point on elliptic curve: " + str(ee.gens()[0]))

def orig(P,N):
    x=P[0]
    y=P[1]
    a=(8*(N+3)-x+y)/(2*(N+3)*(4-x))
    b=(8*(N+3)-x-y)/(2*(N+3)*(4-x))
    c=(-4*(N+3)-(N+2)*x)/((N+3)*(4-x))
    da=denominator(a)
    db=denominator(b)
    dc=denominator(c)
    l=lcm(da,lcm(db,dc))
    return [a*l,b*l,c*l]

print("[a, b, c] = " + str(orig(m*P,N)))