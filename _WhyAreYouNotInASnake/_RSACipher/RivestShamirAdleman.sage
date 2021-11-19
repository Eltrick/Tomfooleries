alphabet = ["!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

N = int(input("N = "))
E = int(input("E = "))
D = [int(x) for x in input("[D] = ").split(" ")]

def GetPhiN(N):
    Factors = factor(N);
    p1 = Factors[0];
    p2 = Factors[1];
    phiN = ((p1 - 1) * (p2 - 1)) / gcd(p1 - 1, p2 - 1);
    return phiN

def GetPrivateComponent(phiN, publicComponent):
    A = phiN;
    B = publicComponent;
    Q = floor(A/B);
    R = A % B;
    T1 = 0;
    T2 = 1;
    T3 = T1 - (T2 * Q);
    while R != 0:
        A = B;
        B = R;
        Q = floor(A/B);
        R = A % B;
        T1 = T2;
        T2 = T3;
        T3 = T1 - (T2 * Q);
    privateComponent = T2 % phiN;
    if (privateComponent*publicComponent)%phiN == 1:
        return privateComponent;
    else:
        print("Error: Cannot get private component of RSA keypair");
        return;
    return;

def Decrypt(N, publicComponent, D):
    phiN = GetPhiN(N);
    privateComponent = GetPrivateComponent(phiN, publicComponent);
    for encryptedNumber in D:
        decryptedNumber = ((encryptedNumber ** privateComponent) % N) - 1;
        print(alphabet[decryptedNumber]);
    return;

Decrypt(N, E, D)