LUT = [[1, 4, 0, 3, 2], [3, 2, 4, 3, 3], [2, 3, 1, 4, 2], [2, 3, 4, 2, 1], [3, 2, 4, 3, 4]]
R_INDEX = "BRYMG"
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def column_index(bat_count: int) -> int:
    if bat_count < 2:
        return 0
    return max(5, bat_count) - 1

def sn_sum(sn: str) -> int:
    result = 0
    for c in sn:
        if c in A:
            result += A.index(c) + 1
        else:
            result += int(c)
    return result

def solve():
    bat = int(input("Input battery count: "))
    
    inp = input("Input colour abbreviation and number on the module: ").upper().split(" ")
    start_num = sn_sum(input("Input serial number: ").upper())

    shift_count = LUT[R_INDEX.index(inp[0])][column_index(bat)]
    num = (start_num >> shift_count) ^ start_num
    print(f"Press {'Yes' if num == inp[1] else 'No'}.")

if __name__ == "__main__":
    solve()