import math

b15 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"]
bitIndex = 0
bitstring = []
bits = []

def main() -> None:
    global b15
    global bitIndex
    global bitstring
    global bits
    
    TPCommands = []
    
    print("<―――――――――――――――――――――START―――――――――――――――――――――>")
    base15Number = input("Enter base-15 number from least to most significant digits here: ").upper()
    bitString = input("Enter 7-digit bitstring here: ")
    if len(bitString) != 7:
        print("Expected bitstring of length 7, restarting...")
        main()
    for x in range(0, 7):
        if bitString[x] == "0":
            bitstring.append(False)
        elif bitString[x] == "1":
            bitstring.append(True)
    base10Number = 0
    for x in range(0, len(base15Number)):
        base10Number += b15.index(base15Number[x]) * (15 ** x)
    print("Number: " + str(base10Number))
    Factors = list(set(PrimeFactor(base10Number)))
    tree = SetBool(Tree(0, base10Number))
    tree.active = True
    ratio = LogicCascade(tree)
    sequence = ReductiveCascade(ratio)
    indices = BaseConvert(base10Number, len(sequence))
    if len(indices) % 2 == 1:
        indices.insert(0, 0)
    truthFractions = []
    for x in range(0, len(indices)):
        if x % 2 == 1: # If we are on an even index
            if sequence[indices[x]] > sequence[indices[x - 1]]:
                truthFractions.append(Fraction(sequence[indices[x - 1]], sequence[indices[x]]))
            else:
                truthFractions.append(Fraction(sequence[indices[x]], sequence[indices[x - 1]]))
    for x in range(0, len(truthFractions)):
        if truthFractions[x].den != 0:
            truthFractions[x] = Fraction(math.floor(truthFractions[x].num / math.gcd(truthFractions[x].num, truthFractions[x].den)), math.floor(truthFractions[x].den / math.gcd(truthFractions[x].num, truthFractions[x].den)))
    print(Log(tree, 0, base10Number, None))
    print("Ratio: " + str(ratio.num) + "/" + str(ratio.den))
    print("Reductive Sequence: " + str(sequence))
    print("Number converted: " + str(indices))
    fractionLogging = ""
    for i in range(0, len(truthFractions)):
        fractionLogging += str(truthFractions[i].num) + "/" + str(truthFractions[i].den)
        if i != len(truthFractions) - 1:
            fractionLogging += ", "
    print("Quantum Logic Fractions: " + fractionLogging)
    quantum = QuantumLogic(truthFractions)
    answer = FractionCascade(quantum)
    print("Quantum Boolean: " + str(quantum.num) + "/" + str(quantum.den))
    print("Answer: " + str(answer))
    for i in range(0, len(answer)):
        answer[i] = str(bin(answer[i]))
        answer[i] = answer[i].replace("0b", "")
        tpString = ""
        for j in range(0, len(answer[i])):
            if answer[i][j] == "1":
                tpString += "r"
            elif answer[i][j] == "0":
                tpString += "l"
        TPCommands.append(tpString)
    print("Answer in binary: " + str(answer))
    fullCommand = ""
    for tpCommand in TPCommands:
        fullCommand += tpCommand + "m"
    fullCommand += "m"
    print("Command to input for Toilet Paper: " + fullCommand)

def BaseConvert(num, base):
    l = []
    if num == 0:
        l.append(0)
    while num > 0:
        l.append(num % base)
        num = math.floor(num / base)
    l = l[::-1]
    return l

def Log(node, depth, remainder, logic):
    logging = ""
    if depth == 0:
        logging += "<―――――――――――――――――――――TREE―――――――――――――――――――――>"
        logging += "\n[" + str(node.prime) + ";" + str(remainder) + ";" + (("1" if node.active else "0") if logic != None else "-") + ";" + (("1" if logic else "0") if logic != None else "1") + "]"
    else:
        logging += "\n"
        for n in range(0, depth):
            logging += "- "
        logging += "[" + str(node.prime) + ";" + str(remainder) + ";" + (("1" if node.active else "0") if logic != None else "-") + ";" + (("1" if logic else "0") if logic != None else "1") + "]"
    if logic == None:
        logic = True
    for child in node.children:
        logging += Log(child, depth + 1, math.floor(remainder / child.prime) + 1, logic ^ child.active)
    return logging

def RequestBit():
    global bitIndex
    neededBits = []
    for i in range(0, bitIndex + 1):
        neededBits.append(bitstring[i % len(bitstring)])
    neededBits = neededBits[::-1]
    for i in range(0, len(neededBits)):
        bits.append(neededBits[i])
    bit = bits[bitIndex]
    bitIndex += 1
    return bit

class Node:
    def __init__(self, prime):
        self.prime = prime
        self.active = False
        self.children = []

class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

def Tree(prime, remainder):
    node = Node(prime)
    if len(PrimeFactor(remainder)) == 1:
        return node
    factors = sorted(set(PrimeFactor(remainder)))
    for factor in factors:
        node.children.append(Tree(factor, math.floor(remainder / factor) + 1))
    return node

def PrimeFactor(num):
    Factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            Factors.append(i)
            num /= i
    return Factors

def ReductiveModulo(num, mod):
    while num >= mod & mod > 0:
        num -= mod
        mod -= 1
    if mod == 0:
        return 0
    else:
        return num

def SetBool(node):
    newnode = Node(node.prime)
    if len(node.children) == 0:
        newnode = node
        newnode.active = RequestBit()
    else:
        xor = False
        for child in node.children:
            newnode.children.append(SetBool(child))
            xor ^= newnode.children[-1].active
        newnode.active = xor
    return newnode
    
def LogicCascade(node):
    fraction = Fraction(0, 0)
    for child in node.children:
        newChild = child
        newChild.active = child.active ^ node.active
        childFrac = LogicCascade(newChild)
        fraction.num += childFrac.num + (newChild.prime if newChild.active else 0)
        fraction.den += childFrac.den + newChild.prime
    return fraction
    
def ReductiveCascade(fraction):
    sequence = [fraction.den, fraction.num]
    while 0 not in sequence:
        sequence.append(ReductiveModulo(sequence[len(sequence) - 2], sequence[-1]))
    return sequence

def QuantumLogic(quantumBools):
    fraction = Fraction(0, 1)
    for x in range(0, len(quantumBools)):
        if quantumBools[x].den == 0:
            quantumBools[x] = Fraction(1, 2)
        else:
            quantumBools[x] = Fraction(int(math.floor(quantumBools[x].num / math.gcd(quantumBools[x].num, quantumBools[x].den))), int(math.floor(quantumBools[x].den / math.gcd(quantumBools[x].num, quantumBools[x].den))))
    p = 1
    for i in range(0, len(quantumBools)):
        p *= 2
    truthtable = []
    for i in range(0, p):
        truthtable.append(RequestBit())
    truthlog = ""
    for l in range(0, len(truthtable)):
        if truthtable[l]:
            truthlog += "1"
        else:
            truthlog += "0"
    print("Truth table: " + truthlog)
    for i in range(0, p):
        if truthtable[i]:
            product = Fraction(1, 1)
            k = p
            for j in range(0, len(quantumBools)):
                k /= 2
                product = Fraction(product.num * ((quantumBools[j].num) if (math.floor(i / k) % 2 == 1) else (quantumBools[j].den - quantumBools[j].num)), product.den * quantumBools[j].den)
                product = Fraction(math.floor(product.num / math.gcd(product.num, product.den)), math.floor(product.den / math.gcd(product.num, product.den)))
            fraction = Fraction(fraction.num * product.den + fraction.den * product.num, fraction.den * product.den)
            if math.gcd(fraction.num, fraction.den) == 0 or fraction.num < 0 or fraction.den < 0:
                return Fraction(0, 0)
            fraction = Fraction(math.floor(fraction.num / math.gcd(fraction.num, fraction.den)), math.floor(fraction.den / math.gcd(fraction.num, fraction.den)))
    return fraction

def FractionCascade(fraction):
    sequence = []
    while fraction.den != 0:
        sequence.append(math.floor(fraction.num / fraction.den))
        fraction = Fraction(fraction.den, fraction.num % fraction.den)
    return sequence

if __name__ == '__main__':
    main()