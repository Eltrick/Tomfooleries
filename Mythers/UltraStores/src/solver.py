import argparse  # For instant interface customization
from src.functions import *  # Helper functions
from src.colors import order  # Color order

parser = argparse.ArgumentParser("Solves a KTANE UltraStores module")  # Argument parser
parser.add_argument("-d", "--debug", action="store_true",  # With arguments
                    help="Debug mode: prints debugging statements")
args = parser.parse_args()  # Parses the arguments


def main() -> None:
    """
    The main function, which solves the UltraStores module.
    :return: None
    """
    a = [0, 0, 0, 0, 0]  # Storage for A, B, C, D values
    b = [0, 0, 0, 0, 0]  # (a4 always = 0)
    c = [0, 0, 0, 0, 0, 0]
    d: int = 0
    stage_list = {0: a, 1: b, 2: c}  # Dict defining each stage's list

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
    a[0] = int((ser[2] * 36 + ser[3]) % 365)  # Characters 3 and 4
    b[0] = int((ser[4] * 36 + ser[5]) % 365)  # Characters 5 and 6
    c[0] = int((ser[0] * 36 + ser[1]) % 365)  # Characters 1 and 2
    if args.debug:  # If [serial number] debugging is enabled, print the values...
        print("Initial values are " + str(a[0]) + ", " + str(b[0]) + ", and " + str(c[0]))
        print("The value of D (sum of chars) is " + str(d))  # derived from the serial number
    
    STAGE = 0  # Keeps track of the module's stage

    partial = input("Are you using this to shadow other people without the initial stage(s)'s rotations? ").upper()
    if partial == "Y":
        STAGE = int(input("Which stage are we currently on? (2 or 3) ")) - 1
        if STAGE == 1:
            a[1] = int(input("a1 = "))
            a[2] = int(input("a2 = "))
            a[3] = int(input("a3 = "))
        elif STAGE == 2:
            a[1] = int(input("a1 = "))
            a[2] = int(input("a2 = "))
            a[3] = int(input("a3 = "))
            b[1] = int(input("b1 = "))
            b[2] = int(input("b2 = "))
            b[3] = int(input("b3 = "))
            b[4] = int(input("b4 = "))
    
    # Now the program has all required serial number data and can get rotations
    while STAGE < 3:  # For each of the 3 stages to do...
        for n in range(1, STAGE + 4):  # For each rotation...
            # Note on the +4: The first stage has 3 rotations, but that's STAGE = 0, so
            # 3 needs to be added, and the end of range is exclusive, so add 3+1, or 4.
            rots_valid = False  # Stores validity of a this stage's input
            rots = []  # Variable to store a list of sub-rotations
            while not rots_valid:  # Prompt until valid
                rots = input("Enter rotation number " + str(n) + " of stage " + str(STAGE + 1)
                             + ":\n(separate sub-rotations with spaces): ").upper().split(" ")
                rots_valid = validate_rots(rots)  # Method below main in this file

            if len(rots) == 1:  # If there's only 1 rotation, use it to calculate the next value
                stage_list[STAGE][n] = mono[rots[0]][STAGE](stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])
            elif len(rots) == 2:  # Otherwise, if there are 2 rotations, check the unused ones
                axes = ["X", "Y", "Z", "U", "V", "W"]  # List of axes
                func = ["X", "Y", "Z"]  # List of axes with functions
                axes.remove(rots[0][0])  # (and axes for function X!)
                axes.remove(rots[0][1])  # Removes the used axes...
                axes.remove(rots[1][0])  # To find the two...
                axes.remove(rots[1][1])  # unused ones.
                index = 0  # Index of the function
                for part in axes:  # For each axis not in XYZ, increment the function index
                    if part not in func:  # (Resulting function: Z if 0 in, Y if 1 in, X if 2 in)
                        index += 1  # Then calculate the next value without a 3rd rotation...

                stage_list[STAGE][n] = poly[func[index]][STAGE](  # (it's unused in X, Y, and Z anyway)
                    rots[0], rots[1], None, stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])
                if args.debug:  # If [multiple-rotation] debugging is enabled, begin with the function used...
                    msg = "Multiple rotation function used: " + func[index] + "\nSub-rotation evaluations:"
                    for rot in rots:  # And construct a debug message by appending various pieces to one string
                        msg += ("\n" + rot + " has a value of " + str(  # Calculates and appends each used value
                            mono[rot][STAGE](stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])))
                    print(msg)  # After constructing the debug message, print it
                # End of double rotation debug message if statement
            # End of double rotation calculation
            else:  # Otherwise, there must be 3 rotations, so check if they all have an axis from XYZ
                # If that's the case, they all must map XYZ to UVW or vice versa, as all six axes are used once
                func = ["X", "Y", "Z"]  # Stores the X, Y, and Z axes in a list for easy function use
                form = "W"  # Stores the formula to use, chosen by a test of each sub-rotation
                for part in rots:  # For each sub-rotation, if neither of the axes is XYZ...
                    if part[0] not in func and part[1] not in func:  # The test fails...
                        form = "V"  # So use function V instead of W in calculating
                        break  # Maybe the world's smallest optimization effort
                stage_list[STAGE][n] = poly[form][STAGE](  # Uses the result formula of the test
                    rots[0], rots[1], rots[2], stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])
                if args.debug:  # If [multiple-rotation] debugging is enabled, begin with the function used...
                    msg = "Multiple rotation function used: " + form + "\nSub-rotation evaluations:"
                    for rot in rots:  # And construct a debug message by appending various pieces to one string
                        msg += ("\n" + rot + " has a value of " + str(  # Calculates and appends each used value
                            mono[rot][STAGE](stage_list[STAGE][n - 1], d, n, a[n - 1], b[n - 1])))
                    print(msg)  # After constructing the debug message, print it
                # End of triple rotation debug message if statement
            # End of triple (and all) rotation calculation
            if args.debug:  # If [value-based] debugging is enabled, print each value
                print("Value " + str(n) + " of stage " + str(STAGE + 1) + " is " + str(stage_list[STAGE][n]))
        # End of rotation (n) loop
        ans_num = stage_list[STAGE][STAGE + 3]  # The answer! (+3 similar to +4 in rotation loop)
        if args.debug:  # If [value-based] debugging is enabled, print the final value (decimal, not ternary)
            print("Stage " + str(STAGE + 1) + "'s answer is " + str(int(ans_num)) + "! Now to input it...")
        print("Press the center button to reveal eight colors.")  # Prompt for color input
        if ans_num != 0:  # If the answer is zero, though, it doesn't matter, so skip.
            cols_valid = False  # Stores validity of the color list while prompting
            cols = []  # Variable to store a list of all eight colors
            while not cols_valid:  # Prompt until valid
                cols = list(input("Enter colors in CW order from North, without spaces: ").upper())
                cols_valid = validate_cols(cols)  # Method below main in this file
            ans_seq = order(stage_cols[STAGE], cols, args.debug)  # Changes list order
            if args.debug:  # If color-based debugging is allowed, print the ending order
                print("The order list goes " + str(ans_seq) + ", so...")
            answer(ans_num, ans_seq)  # Gets the final answer!
        else:  # If the answer was 0, say to only press the center.
            print("The answer is 0, so just press the center button again!")
        if input("Enter N if a strike occurred, otherwise press enter: ").upper() == "N":
            print("[STRIKE] Try reading the rotations again.\n[STRIKE] Note: only the colors will change,\n"
                 + "and you may have to re-light the white button.") # Clarified to avoid ambiguity
            STAGE -= 1  # If that wasn't correct, undo the increment of the stage (below)...
        STAGE += 1  # So this stage will be re-calculated only if it was wrong
    # End of stage loop and program (except for a solve message)
    print("[SOLVED] Congratulations on solving UltraStores! -mythers45#1807")


def answer(ans_num: int, ans_seq: list) -> None:
    """
    Takes the integer calculated from the serial number and 6D rotations,
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


def validate_rots(rots: list) -> bool:
    """
    Takes a list of sub-rotations comprising one rotation and tests its validity.
    For a rotation to be valid, it must have 1, 2, or 3 sub-rotations, all defined
    in the dictionary of single rotations, without using any axis more than once.
    :param rots: The rotation (a.k.a. list of sub-rotations) to validate
    :return: The validity of the rotation by the above tests
    """
    valid = True  # Assume valid until tested
    if not 1 <= len(rots) <= 3:  # If the rotation has 0 or 4+ sub-rotations...
        print("Invalid number of sub-rotations (should be 1, 2, or 3)")
        return False  # It's invalid, and skip the other tests.
    used = []  # List for storing used axes (which should be unique)
    for part in rots:  # Next, iterate through the sub-rotations...
        if part not in mono:  # If one's not in the dictionary, it's invalid...
            print("Invalid sub-rotation '" + part + "' (should have 2 of X Y Z W V U)")
            valid = False  # But keep checking other sub-rotations for validity.
        else:  # Otherwise, check for duplicate axes.
            if part[0] in used:  # If the first axis is already used...
                print("Axis '" + part[0] + "' used multiple times (axes should be unique)")
                valid = False  # The rotation is invalid.
            if part[1] in used:  # The same goes for the second axis,
                print("Axis '" + part[1] + "' used multiple times (axes should be unique)")
                valid = False  # After checking if the axes were used before...
            used.extend(list(part))  # Add them to the list so they're marked as used next time.
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


if __name__ == '__main__':
    main()
