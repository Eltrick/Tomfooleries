Keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def main() -> None:
    global Keys

    result = []
    offset = []

    for i in range(0, 6):
        info = input("Key + Offset: ").upper()
        if info == "END":
            print(" ".join(result))
            exit()
        else:
            info = info.split(" ")
        offset.append((int(info[1]) % len(Keys) + len(Keys)) % len(Keys))
        result.append(Keys[(Keys.index(info[0]) + offset[i]) % len(Keys)])

    stage = 6
    while True:
        info = input("Key: ").upper()
        if info == "END":
            print(" ".join(result))
            exit()
        result.append(Keys[(Keys.index(info) + offset[stage % len(offset)]) % len(Keys)])
        stage += 1


if __name__ == "__main__":
    main()
