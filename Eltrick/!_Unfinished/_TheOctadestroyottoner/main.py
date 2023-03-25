import math
from platform import java_ver

def main() -> None:
    batteryCount = int(input("Battery Count: "))
    batteryHolderCount = int(input("Battery Holder Count: "))
    indicatorCount = int(input("Indicator Count: "))
    unlitIndicatorCount = int(input("Unlit Indicator Count: "))
    portCount = int(input("Port Count: "))
    t = int(input("Current Time: "))
    output = input("Current Output, split in half: ").split(" ")

    j = batteryHolderCount
    jj = batteryCount + unlitIndicatorCount
    jjj = batteryCount + indicatorCount + portCount

    encSins = [0, 0]

    finalValuesLeft = []
    finalValuesRight = []

    for ts in range(0, 1001):
        for a in range(7, 16):
            for b in range(50, 101):
                encSins[0] = math.floor(2**8 * (EncryptedSine((a * math.floor(t + ts)) / b, j, jj, jjj)))
                if format(encSins[0], 'b') == output[0]:
                    finalValuesLeft.append([ts, a, b])
    
    for i in range(0, len(finalValuesLeft)):
        for c in range(7, 16):
            for d in range(50, 101):
                encSins[1] = math.floor(2**8 * (EncryptedSine(((c * math.floor(t + finalValuesLeft[i][0])) / d), j, jj, jjj)))
                if format(encSins[1], 'b') == output[1]:
                    finalValuesRight.append([finalValuesLeft[i][0], c, d])


def EncryptedSine(x: int, batteryHolderCount: int, batteryUnlitCount: int, batteryIndicatorPortCount: int) -> float:
    a = 0
    b = 0
    c = 0
    n = 0

    sineN = 0

    while abs(s(x, n)) >= (1/2**16):
        sineN += s(x, n)
        n += 1
    
    while abs(s(x, a)) < (1/batteryHolderCount):
        a += 1
    
    while abs(s(x, b)) < (1/batteryUnlitCount):
        b += 1
    
    while abs(s(x, c)) < (1/batteryIndicatorPortCount):
        c += 1
    
    return sineN - s(x, a) - s(x, b) - s(x, c)

def s(x: int, n: int) -> float:
    return ((-1)**n) * ((x **(2*n + 1)) / (math.factorial(2*n+1)))

if __name__ == "__main__":
    main()