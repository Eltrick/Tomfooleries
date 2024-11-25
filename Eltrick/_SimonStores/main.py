from colors import order

v = [0, 0, 0, 0, 0]  # Storage for A, B, C, D values
vv = [0, 0, 0, 0, 0]  # (a4 always = 0)
vvv = [0, 0, 0, 0, 0, 0]
d = 0
cols = []

#Region: Main

def main() -> None:
    global v
    global vv
    global vvv
    global d
    global cols
    
    stage_list = {0: v, 1: vv, 2: vvv}  # Dict defining each stage's list
    ser = list(input("Enter the bomb's serial number: ").upper())
    while len(ser) != 6:  # Gets the serial number (SN), ensuring it's six characters long
        ser = list(input("Invalid serial number. Re-enter it:\n(six characters with no spaces): ").upper())
    for i in range(0, len(ser)):  # Iterates through the SN's characters, first validating...
        if not ser[i].isalnum():  # (All characters should be alphanumeric)
            print("DANGER: Non-alphanumeric character encountered at character " + str(i + 1))
            print("Such characters CANNOT appear in the serial number. Exiting...")
            exit(1)  # If a non-alphanumeric character appears, exit immediately
        elif ser[i].isdigit() and (i == 3 or i == 4):  # Chars 4 and 5 should be letters
            print("WARNING: Number encountered at character " + str(i + 1))
            print("Characters 4 and 5 should always (?) be letters.")
        elif ser[i].isalpha() and (i == 2 or i == 5):  # Chars 3 and 6 should be numbers
            print("WARNING: Letter encountered at character " + str(i + 1))
            print("Characters 3 and 6 should always (?) be numbers.")
        ser[i] = b_36.index(ser[i])  # Then translating the current SN character...
        d += ser[i]  # into base 36, while accumulating d with each one
    cols_valid = False
    while not cols_valid:
        cols = list(input("Enter colors in CW order from North, without spaces: ").upper())
        cols_valid = validate_cols(cols)
    v[0] = int((ser[2] * 36 + ser[3]) % 365)  # Characters 3 and 4
    vv[0] = int((ser[4] * 36 + ser[5]) % 365)  # Characters 5 and 6
    vvv[0] = int((ser[0] * 36 + ser[1]) % 365)  # Characters 1 and 2
    print("Initial values are " + str(v[0]) + ", " + str(vv[0]) + ", and " + str(vvv[0]))
    print("The value of D (sum of chars) is " + str(d))  # derived from the serial number
    
    #Start solving the actual module
    STAGE = 0
    while STAGE < 3:
        for n in range(1, STAGE + 4):
            flash_valid = False
            flashes = []
            while not flash_valid:
                flashes = input("Enter flash number " + str(n) + " of stage " + str(STAGE + 1) + ":\n(separate sub-flashes with spaces, primary colours are to be input first): ").upper().split(" ")
                flash_valid = validate_flashes(flashes)
            
            if len(flashes) == 1:
                stage_list[STAGE][n] = single[flashes[0]][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                
            elif len(flashes) == 2:
                pri = ["R", "G", "B"]
                sec = ["C", "M", "Y"]
                if flashes[0] in pri and flashes[1] in pri: #Case: PP
                    pri.remove(flashes[0])
                    pri.remove(flashes[1])
                    stage_list[STAGE][n] = double["PP"][STAGE](flashes[0], flashes[1], pri[0], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: PP \nSub-flash evaluations: "
                    for flash in flashes:
                        msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
                elif flashes[0] in pri and flashes[1] in sec: #Case: PS
                    pri.remove(flashes[0])
                    sec.remove(flashes[1])
                    stage_list[STAGE][n] = double["PS"][STAGE](flashes[0], flashes[1], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: PS \nSub-flash evaluations: "
                    for flash in flashes:
                        msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
                elif flashes[0] in sec and flashes[1] in sec: #Case: SS
                    sec.remove(flashes[0])
                    sec.remove(flashes[1])
                    stage_list[STAGE][n] = double["SS"][STAGE](flashes[0], flashes[1], sec[0], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: SS \nSub-flash evaluations: "
                    for flash in flashes:
                        msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
            else:
                pri = ["R", "G", "B"]
                sec = ["C", "M", "Y"]
                if flashes[0] in pri and flashes[1] in pri and flashes[2] in pri: #Case: PPP
                    stage_list[STAGE][n] = triple["PPP"][STAGE](flashes[0], flashes[1], flashes[2], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: PPP \nSub-flash evaluations: "
                    for flash in flashes:
                        msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
                elif flashes[0] in pri and flashes[1] in pri and flashes[2] in sec: #Case: PPS
                    stage_list[STAGE][n] = triple["PPS"][STAGE](flashes[0], flashes[1], flashes[2], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: PPS \nSub-flash evaluations: "
                    for flash in flashes:
                        msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
                elif flashes[0] in pri and flashes[1] in sec and flashes[2] in sec: #Case: PSS
                    stage_list[STAGE][n] = triple["PSS"][STAGE](flashes[0], flashes[1], flashes[2], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: PSS \nSub-flash evaluations: "
                    if STAGE != 2:
                        for flash in flashes:
                            msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    else:
                        msg += ("\n" + flashes[0] + " has a value a of " + str(single[flashes[0]][STAGE](stage_list[0][n - 1], d, n, v[n - 1], vv[n - 1])))
                        msg += ("\n" + flashes[0] + " has a value b of " + str(single[flashes[0]][STAGE](stage_list[1][n - 1], d, n, v[n - 1], vv[n - 1])))
                        msg += ("\n" + flashes[1] + " has a value of " + str(single[flashes[1]][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                        msg += ("\n" + flashes[2] + " has a value of " + str(single[flashes[2]][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
                elif flashes[0] in sec and flashes[1] in sec and flashes[2] in sec: #Case: SSS
                    stage_list[STAGE][n] = triple["SSS"][STAGE](flashes[0], flashes[1], flashes[2], stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])
                    msg = "Multiple flash function used: SSS \nSub-flash evaluations: "
                    for flash in flashes:
                        msg += ("\n" + flash + " has a value of " + str(single[flash][STAGE](stage_list[STAGE][n - 1], d, n, v[n - 1], vv[n - 1])))
                    print(msg)
            print("Value " + str(n) + " of stage " + str(STAGE + 1) + " is " + str(stage_list[STAGE][n]))
            
        ans_num = stage_list[STAGE][STAGE + 3]
        print("Stage " + str(STAGE + 1) + "'s answer is " + str(int(ans_num)) + "! Now to input it...")
        
        if ans_num == 0:
            print("The answer is 0, so just press the center button without inputting any colours!")
        else:
            ans_seq = order(stage_cols[STAGE], cols)
            print("The order list goes " + str(ans_seq) + ", so...")
            answer(ans_num, ans_seq)  # Gets the final answer!
        if input("Enter N if a strike occurred, otherwise press enter: ").upper() == "N":
            print("[STRIKE] Try reading the flashes again.\n[STRIKE] Note: only the colors will change,\n and you may have to re-light the white button.") # Clarified to avoid ambiguity
            STAGE -= 1  # If that wasn't correct, undo the increment of the stage (below)...
        STAGE += 1  # So this stage will be re-calculated only if it was wrong
    print("[SOLVED] This is the end.")

def answer(ans_num: int, ans_seq: list) -> None:
    """
    Takes the integer calculated from the serial number and colour flashes,
    along with the list calculated from the ordering of the button colors,
    and combines them to form a sequence of button presses for submitting.
    Entering three of these button sequences correctly will solve the module.
    :param ans_num: The answer number, as an integer
    :param ans_seq: The answer color sequence
    :return: None, but print the answer
    """
    tern = []  # List to store balanced ternary for ans_num
    for i in range(5, -1, -1):  # For each power of 3 from 3^5 down to 3^0...
        if abs(ans_num - pow(3, i)) < abs(ans_num):  # If subtracting it gets closer to 0...
            ans_num -= pow(3, i)  # Subtract it, then put a + (W) in balanced ternary
            tern.insert(0, "W")  # Inserts at index 0 so 3^5 ends last
        elif abs(ans_num + pow(3, i)) < abs(ans_num):  # Otherwise, if adding it gets closer to 0...
            ans_num += pow(3, i)  # Subtract it, then put a - (K) in balanced ternary
            tern.insert(0, "K")  # Inserts at index 0 so 3^5 ends last
        else:  # Otherwise, leave ans_num as is and put a 0 (0) in balanced ternary
            tern.insert(0, "0")  # Inserts at index 0 so 3^5 ends last
    sign = "W"  # Stores the currently selected sign (W or K)
    ans_str = ""  # Stores the final answer string
    for i in range(0, 6):  # For each of the buttons...
        if tern[i] != "0":  # If it has nonzero value...
            if sign != tern[i]:  # Add and update the new sign if needed
                ans_str += tern[i]
                sign = tern[i]  # Update
            ans_str += ans_seq[i]  # Then add the color to press
    print("Press " + ans_str + ", then press the center button to submit.")  # PRINTS THE FINAL ANSWER


def validate_flashes(flashes: list) -> bool:
    valid = True  # Assume valid until tested
    if not 1 <= len(flashes) <= 3:  # If the rotation has 0 or 4+ sub-flashes...
        print("Invalid number of sub-flashes (should be 1, 2, or 3)")
        return False  # It's invalid, and skip the other tests.
    return valid  # Finally, return the validity (False if any tests failed, else True).


def validate_cols(cols: list) -> bool:
    """
    Takes a list of colors and ensures they form a valid configuration of colors.
    :param cols: The list of colors to validate (1 each of R G B C M Y W K)
    :return: The validity of the list based on the above condition
    """
    if len(cols) != 8:  # If there aren't 8 colors...
        print("Invalid number of colors (should be 8 letters, no spaces)")
        return False  # It's invalid, and skip the other tests.
    # These lists start with all 8 colors. all_cols doesn't change, as it's
    # made for storing valid colors, while unused changes to detect duplicates.
    all_cols = ["R", "G", "B", "C", "M", "Y", "W", "K"]
    unused = all_cols.copy()  # Copy won't change original
    for color in cols:  # Iterating through cols...
        if color not in all_cols:  # If an invalid color was entered, don't remove.
            print("Invalid color '" + color + "' (should be one of R G B C M Y W K)")
        elif color not in unused:  # If a valid color was already removed, don't remove.
            print("Color '" + color + "' used multiple times (colors should be unique)")
        else:  # Otherwise, the color can be removed from the list of unused ones.
            unused.remove(color)  # Above case checks for absence, stopping errors here
    return len(unused) == 0  # If all eight colors removed successfully, the input is valid.

#Endregion: Main

#Region: Functions

b_36 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B",
        "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

stage_cols = {0: ["R", "G", "B", "C", "M", "Y"],
              1: ["Y", "B", "G", "M", "C", "R"],
              2: ["B", "M", "R", "Y", "G", "C"]}
              
single = {"R": ((lambda x, d, n, a, b: bound(x + d)),
                (lambda x, d, n, a, b: bound(x + a + pow(n, 2))),
                (lambda x, d, n, a, b: bound(x + b - a))),
          "G": ((lambda x, d, n, a, b: bound(x - d)),
                (lambda x, d, n, a, b: bound(2*x - a)),
                (lambda x, d, n, a, b: bound(x - 2*b))),
          "B": ((lambda x, d, n, a, b: bound(2*x - d)),
                (lambda x, d, n, a, b: bound(2*x - v[0] - 4*pow(n, 2))),
                (lambda x, d, n, a, b: bound(x + vv[0] - v[3]))),
          "C": ((lambda x, d, n, a, b: bound(d - x - 8*n)),
                (lambda x, d, n, a, b: bound(x + v[1])),
                (lambda x, d, n, a, b: bound(x - b + a))),
          "M": ((lambda x, d, n, a, b: bound(3*pow(n, 3) - 2*x)),
                (lambda x, d, n, a, b: bound(x + v[2] - d)),
                (lambda x, d, n, a, b: bound(x - 2*a))),
          "Y": ((lambda x, d, n, a, b: bound(x + d - 6*n)),
                (lambda x, d, n, a, b: bound(x + v[3] - a)),
                (lambda x, d, n, a, b: bound(x + vv[4] - v[0])))}

double = {"PP": ((lambda p, pp, r, x, d, n, a, b: bound(max(single[p][0](x, d, n, a, b), single[pp][0](x, d, n, a, b)))),
                 (lambda p, pp, r, x, d, n, a, b: bound(abs(single[p][1](x, d, n, a, b) - single[pp][1](x, d, n, a, b)))),
                 (lambda p, pp, r, x, d, n, a, b: bound(single[r][2](x, d, n, a, b) + single[r][2](b, d, n, a, b) + single[r][2](a, d, n, a, b)))),
          "PS": ((lambda p, s, x, d, n, a, b: bound(single[p][0](x, d, n, a, b) + single[s][0](x, d, n, a, b) - 2*d)),
                 (lambda p, s, x, d, n, a, b: bound(4*d - bound(abs(single[p][1](x, d, n, a, b) - single[s][1](x, d, n, a, b))))),
                 (lambda p, s, x, d, n, a, b: bound(min(single[p][2](x, d, n, a, b), single[s][2](x, d, n, a, b), -bound(abs(single[p][2](x, d, n, a, b) - single[s][2](x, d, n, a, b))))))),
          "SS": ((lambda s, ss, r, x, d, n, a, b: bound(min(single[s][0](x, d, n, a, b), single[ss][0](x, d, n, a, b)))),
                 (lambda s, ss, r, x, d, n, a, b: bound(max(single[r][1](x, d, n, a, b), single[r][1](x, d, n, a, b)))),
                 (lambda s, ss, r, x, d, n, a, b: bound(single[r][2](x, d, n, a, b) - single[s][2](x, d, n, a, b) - single[ss][2](x, d, n, a, b))))}

triple = {"PPP": ((lambda p, pp, ppp, x, d, n, a, b: bound(x + v[0])),
                  (lambda p, pp, ppp, x, d, n, a, b: bound(x + (x % 4)*vv[0] - v[3])),
                  (lambda p, pp, ppp, x, d, n, a, b: bound(x + (x % 3)*vvv[0] - (b % 3)*vv[0] + (a % 3)*v[0]))),
          "PPS": ((lambda p, pp, s, x, d, n, a, b: bound(max(single[p][0](x, d, n, a, b), single[pp][0](x, d, n, a, b), single[s][0](x, d, n, a, b)))),
                  (lambda p, pp, s, x, d, n, a, b: bound(x + single[p][1](x, d, n, a, b) + single[pp][1](x, d, n, a, b) - single[s][1](a, d, n, a, b))),
                  (lambda p, pp, s, x, d, n, a, b: bound(single[p][2](x, d, n, a, b) + single[pp][2](x, d, n, a, b) - single[s][2](b, d, n, a, b) - single[s][2](a, d, n, a, b)))),
          "PSS": ((lambda p, s, ss, x, d, n, a, b: bound(min(single[s][0](x, d, n, a, b), single[ss][0](x, d, n, a, b), single[p][0](x, d, n, a, b)))),
                  (lambda p, s, ss, x, d, n, a, b: bound(x + single[s][1](a, d, n, a, b) + single[ss][1](a, d, n, a, b) - single[p][1](x, d, n, a, b))),
                  (lambda p, s, ss, x, d, n, a, b: bound(single[s][2](x, d, n, a, b) + single[ss][2](x, d, n, a, b) - single[p][2](b, d, n, a, b) - single[p][2](a, d, n, a, b)))),
          "SSS": ((lambda s, ss, sss, x, d, n, a, b: bound(x - v[0])),
                  (lambda s, ss, sss, x, d, n, a, b: bound(x + (vv[0] % 4)*x - v[3])),
                  (lambda s, ss, sss, x, d, n, a, b: bound(x + (vvv[0] % 3)*x - (vv[0] % 3)*b + (v[0] % 3)*a)))}

def bound(x: int) -> int:
    """
    Takes the result of a function and takes it modulo 365,
    but if the original number was negative and the result
    of the modulo wasn't zero, subtracts 365 from the result.
    This puts the number between -364 and 364 inclusive.
    :param x: The number to bound
    :return: The bounded number
    """
    y = x % 365  # Begin by taking x modulo 365 where the result is positive.
    if x < 0 < y:  # If x was negative, and y was not 0 (y can't be negative)...
        return int(y - 365)  # Subtract 365 from y, putting it to -364 at the lowest.
    return int(y)  # Otherwise, just return y (if y was 0, this case holds, not the above).

#Endregion: Functions

if __name__ == '__main__':
    main()
