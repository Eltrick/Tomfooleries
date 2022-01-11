def main() -> None:
    Alphabet = ["!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    string = list(input("26-character string goes here: ").upper())
    message = ""
    for i in range(0, 26):
        for j in range(0, Alphabet.index(string[i])):
            message += Alphabet[i + 1]
    print("Input for other: " + message)

if __name__ == "__main__":
    main()