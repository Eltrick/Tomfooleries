Houses = [{
        "C": 1,
        "D": 2,
        "F": 2,
        "G": 2,
        "I": 2,
        "N": 1,
        "O": 2,
        "R": 3,
        "Y": 1
    },
    {
        "A": 1,
        "E": 2,
        "F": 4,
        "G": 1,
        "H": 2,
        "L": 2,
        "P": 1,
        "U": 2
    },
    {
        "A": 3,
        "C": 1,
        "E": 2,
        "L": 1,
        "N": 2,
        "O": 1,
        "R": 2,
        "V": 1,
        "W": 2
    },
    {
        "A": 3,
        "E": 1,
        "H": 1,
        "I": 1,
        "L": 2,
        "N": 1,
        "R": 2,
        "S": 2,
        "T": 1,
        "Y": 1,
        "Z": 1
    }]

def main() -> None:
    global Houses
    while True:
        score = 0
        moduleName = list(input("Input module key: ").upper())
        house = int(input("Input house Number (zero-indexed, see manual): "))
        for i in range(0, len(moduleName)):
            if moduleName[i] in Houses[house]:
                score += Houses[house][moduleName[i]]
        print("Final Score: " + str(score))

if __name__ == "__main__":
    main()