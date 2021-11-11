import math

b36 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
let = ["!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
triangleNumbers = [ 28, 29, 21, 30, 22, 15, 31, 23, 16, 10, 32, 24, 17, 11, 6, 33, 25, 18, 12, 7, 3, 34, 26, 19, 13, 8, 4, 1, 35, 27, 20, 14, 9, 5, 2, 0 ]
squareNumbers = [ 30, 24, 18, 12, 6, 0, 31, 25, 19, 13, 7, 1, 32, 26, 20, 14, 8, 2, 33, 27, 21, 15, 9, 3, 34, 28, 22, 16, 10, 4, 35, 29, 23, 17, 11, 5 ]

def main() -> None:
    global b36
    global triangleNumbers
    global squareNumbers
    charsUsed = []
    Keys = ["", "", "", "", "", ""]
    
    print("Welcome to the thing I made out of spite due to not knowing that the LED only stays on for a quarter of a second.")
    serial = input("Please input the serial number: ").upper()
    tempX = input("Please concatenate and input all indicators' labels: ").upper()
    
    X = 0;
    
    for n in tempX:
        X += let.index(n)
    X %= 36
    while math.gcd(X, 36) != 1:
        X += 1
    print("X = " + str(X))
    
    initialCipherSequence = ""
    for k in range(0, 36):
        currentChar = serial[k % 6]
        while initialCipherSequence.find(currentChar) != -1:
            currentChar = b36[(b36.index(currentChar) + X) % 36]
        initialCipherSequence += currentChar
    print("Initial Cipher Sequence: " + initialCipherSequence)
    
    for k in range(0, 6):
        if k == 0:
            convert = initialCipherSequence
        else:
            convert = Keys[k - 1]
        
        con = ""
        if b36.index(serial[k]) > 9:
            for x in range(0, 36):
                con += convert[triangleNumbers[x]]
        else:
            for x in range(0, 36):
                con += convert[squareNumbers[x]]
        
        Keys[k] = con
        print("Key #" + str(k + 1) + ": " + con)
    cipherText = input("Input Module Ciphertext separated by spaces for each row: ").split(" ")
    plainText = ""
    for i in range(0, 6):
        for j in range(0, 6):
            plainText += Keys[i][b36.index(cipherText[i][j])]
        plainText += "\r\n";
    print("Plaintext: " + "\r\n" + plainText)
    while input("Is there another Outrageous? (Y/N) ").upper() == "Y":
        cipherText = input("Input Module Ciphertext separated by spaces for each row: ").split(" ")
        plainText = ""
        for i in range(0, 6):
            for j in range(0, 6):
                plainText += Keys[i][b36.index(cipherText[i][j])]
            plainText += "\r\n";
        print("Plaintext: " + "\r\n" + plainText)
    print("And that is it. Goodbye. - L.V.")
    
if __name__ == '__main__':
    main()