Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main() -> None:
    global Alphabet

    goals = Alphabet.copy()

    while len(goals) != 1:
        info = input("Input info on Klaxon: ").upper().split(" ")
        if info[0] == "-" or info[0] == "!":
            for i in range(0, len(info[1])):
                if info[1][i] in goals:
                    goals.pop(goals.index(info[1][i]))
        else:
            pointer = 0
            while pointer != len(goals):
                if goals[pointer] not in info[1]:
                    goals.pop(pointer)
                else:
                    pointer += 1
        print("Current: " + "".join(goals))
    print("Answer: " + "".join(goals))

if __name__ == "__main__":
    main()