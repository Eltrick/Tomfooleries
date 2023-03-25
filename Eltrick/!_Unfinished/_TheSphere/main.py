import math

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
SequenceOrders = [["T4", "T1", "H5", "T2", "H3", "H1", "T6", "T3", "H2", "H4", "T5"], ["H3", "T2", "T6", "T1", "H2", "H5", "T3", "T4", "T5", "H1", "H4"], ["H5", "H1", "T3", "T4", "H3", "T6", "T1", "H2", "H4", "T5", "T2"], ["T1", "H2", "T3", "H5", "T6", "H4", "H1", "T2", "T4", "T5", "H3"], ["H1", "T5", "T3", "H4", "H2", "T6", "T1", "T2", "T4", "H3", "H5"], ["T2", "T4", "H5", "H1", "T3", "T1", "H2", "H3", "H4", "T5", "T6"], ["T6", "H3", "T2", "H1", "T5", "T4", "H4", "H2", "T3", "T1", "H5"], ["H4", "H1", "H3", "T2", "T6", "H5", "H2", "T4", "T3", "T5", "T1"], ["T4", "T6", "H3", "T1", "T2", "H5", "H1", "T3", "H2", "T5", "H4"], ["H2", "T2", "H3", "T6", "H1", "T5", "T4", "H4", "H5", "T1", "T3"], ["T1", "H1", "T2", "H2", "T3", "H3", "T4", "H4", "T5", "H5", "T6"]]
SphereColours = ["R", "B", "G", "O", "I", "P", "X", "W"]
ColourData = [99, 99, 99, 99, 99, 99, 99, 99]

def main() -> None:
    global Alphabet
    global SequenceOrders

    serialNumber = list(input("Serial Number: ").upper())
    for i in range(0, len(serialNumber)):
        if serialNumber[i] in Alphabet:
            serialNumber[i] = (Alphabet.index(serialNumber[i]) + 1) % 10
        else:
            serialNumber[i] = int(serialNumber[i])
    
    holdColours = list(input("Colour Sequence: ").upper())

    for i in range(0, len(holdColours)):
        if ColourData[SphereColours.index(holdColours[i])] != 99:
            


if __name__ == "__main__":
    main()