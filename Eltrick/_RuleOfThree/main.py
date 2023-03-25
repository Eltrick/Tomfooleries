import math

def main() -> None:
    coordinates = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    lengths = [0, 0, 0]

    for i in range(0, len(coordinates)):
        movements = input("Enter XYZ movements of " + "RYB"[i] + " sphere: ").split(" ")
        for j in range(0, len(movements)):
            result = 0
            for k in range(0, len(movements[j])):
                if movements[j][k] == "+":
                    result += 3**k
                elif movements[j][k] == "-":
                    result -= 3**k
                else:
                    result += 0
            coordinates[i][j] = result
    for i in range(0, len(lengths)):
        lengths[i] = math.sqrt((coordinates[i][0] - coordinates[(i + 1) % len(coordinates)][0])**2 + (coordinates[i][1] - coordinates[(i + 1) % len(coordinates)][1])**2 + (coordinates[i][2] - coordinates[(i + 1) % len(coordinates)][2])**2)
    
    s = sum(lengths) / 2
    area = math.sqrt(s*(s - lengths[0])*(s - lengths[1])*(s - lengths[2]))
    print("Area = " + str(area))

    answer = BalancedTernary(math.floor(area))
    print("Press the following in order: " + answer)

def BalancedTernary(num: int) -> str:
    tern = []  # List to store balanced ternary for num
    for i in range(5, -1, -1):  # For each power of 3 from 3^5 down to 3^0...
        if abs(num - pow(3, i)) < abs(num):  # If subtracting it gets closer to 0...
            num -= pow(3, i)  # Subtract it, then put a +
            tern.insert(0, "B")  # Inserts at index 0 so 3^5 ends last
        elif abs(num + pow(3, i)) < abs(num):  # Otherwise, if adding it gets closer to 0...
            num += pow(3, i)  # Subtract it, then put a -
            tern.insert(0, "R")  # Inserts at index 0 so 3^5 ends last
        else:  # Otherwise, leave num as is and put a 0 (0) in balanced ternary
            tern.insert(0, "Y")  # Inserts at index 0 so 3^5 ends last
    return "".join(tern)

if __name__ == "__main__":
    main()