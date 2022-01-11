"""
This file is utilized to calculate the
order of colors to use in submission,
based on a given order of eight colors.
They must be abbreviated to a single
letter during input with these letters:

Red = R
Green = G
Blue = B
Cyan = C
Magenta = M
Yellow = Y
White = W
Black = K (B is blue, so first letter can't work here)
"""


def order(stage_cols: list, cols: list, debug: bool) -> list:
    """
    The primary method of this file, which makes a color order.
    :param stage_cols: The initial color list for this stage
    :param cols: The validated list of colors on the module
    :param debug: Debug mode, which prints debug statements
    :return: The initial list, re-ordered by various rules
    """
    if debug: # Only print initial list if debugging
        print("Initial color list: " + str(stage_cols))
    if cols[0] == "W":  # If top is white, reverse the sequence.
        stage_cols.reverse()
        if debug:
            print("After rule #1: " + str(stage_cols))
    if cols[1] == "Y":  # If top-right is yellow, cycle all 1 left.
        stage_cols = stage_cols[1:] + [stage_cols[0]]
        if debug:
            print("After rule #2: " + str(stage_cols))
    if abs(cols.index("W") - cols.index("K")) == 4:  # If white is opposite black...
        for i in range(0, 4):  # Swap each color with its opposite color on the module.
            if cols[i] != "W" and cols[i] != "K":  # For each color pair, if it's not...
                swap(stage_cols, cols[i], cols[i + 4])  # W/K, then it can be swapped.
        if debug:
            print("After rule #3: " + str(stage_cols))
    if abs(cols.index("R") - cols.index("C")) == 4:  # If red is opposite cyan...
        swap(stage_cols, "R", "C")  # Swap R and C, G and M, and B and Y.
        swap(stage_cols, "G", "M")
        swap(stage_cols, "B", "Y")  # If G and M have one button between them (6 for wraparound)...
        if debug:
            print("After rule #4: " + str(stage_cols))
    if abs(cols.index("G") - cols.index("M")) == 2 or abs(cols.index("G") - cols.index("M")) == 6:
        # [Possible index pairs: 02, 13, 24, 35, 46, 57, 60, 71 (last two use 6, others use 2)]
        # Cycle the colors based on clockwise order of appearance on the module.
        cw = cols.copy()  # List to store colors in clockwise order
        cw.remove("W")  # But without W or K
        cw.remove("K")  # first is used to store cw[0]...
        first = cw[0]  # so the cycle performs right
        for i in range(1, 6):  # Example below
            swap(stage_cols, first, cw[i])
        if debug:
            print("After rule #5: " + str(stage_cols))
        """
        Let stage_cols = R G B C M Y
        Let cw = R C Y M G B, so first = R
        
        i = 1: stage_cols = C G B R M Y (swapped R, C)
        i = 2: stage_cols = C G B Y M R (swapped R, Y)
        i = 3: stage_cols = C G B Y R M (swapped R, M)
        i = 4: stage_cols = C R B Y G M (swapped R, G)
        i = 5: stage_cols = C B R Y G M (swapped R, B)
        
        Start: stage_cols = R G B C M Y
        i = 5: stage_cols = C B R Y G M
        R->C, C->Y, Y->M, M->G, G->B, B->R (correct)
        """
    # (End of example) If G is adjacent to W (7 for wraparound), cycle the primary colors
    if abs(cols.index("G") - cols.index("W")) == 1 or abs(cols.index("G") - cols.index("W")) == 7:
        cycle_pri(stage_cols)  # If M is adjacent to K (7 for wraparound), cycle the secondary colors
        if debug:
            print("After rule #6: " + str(stage_cols))
    if abs(cols.index("M") - cols.index("K")) == 1 or abs(cols.index("M") - cols.index("K")) == 7:
        cycle_sec(stage_cols)  # If W is adjacent to K (7 for wraparound), cycle both of those sets
        if debug:
            print("After rule #7: " + str(stage_cols))
    if abs(cols.index("W") - cols.index("K")) == 1 or abs(cols.index("W") - cols.index("K")) == 7:
        cycle_pri(stage_cols)  # Note: This stacks with earlier cycles
        cycle_sec(stage_cols)
        if debug:
            print("After rule #8: " + str(stage_cols))
    if (1 <= cols.index("B") <= 3 and 1 <= cols.index("Y") <= 3) or (  # If B and Y are both on the right...
            5 <= cols.index("B") <= 7 and 5 <= cols.index("Y") <= 7):  # or both on the left, swap B with...
        swap_int(stage_cols, stage_cols.index("B"), 5 - stage_cols.index("B"))  # its opposite in the list.
        if debug:
            print("After rule #9: " + str(stage_cols))
    if 1 <= cols.index("R") <= 3:  # If red is on the right...
        swap(stage_cols, "R", "Y")  # Swap red and yellow.
        if debug:
            print("After rule #10: " + str(stage_cols))
    if 5 <= cols.index("B") <= 7:  # If blue is on the left...
        swap(stage_cols, "G", "C")  # Swap green and cyan.
        if debug:
            print("After rule #11: " + str(stage_cols))
    offset_cols = cols[cols.index("W"):] + cols[:cols.index("W")]  # Offsets list so W is first
    if offset_cols.index("Y") > offset_cols.index("G"):  # If, from W, Y is further clockwise than G...
        swap_int(stage_cols, 0, 5)  # Swap the first and last colors in the list
        if debug:
            print("After rule #12: " + str(stage_cols))
    offset_cols = cols[cols.index("K"):] + cols[:cols.index("K")]  # Offsets list so K is first
    if offset_cols.index("B") > offset_cols.index("C"):  # If, from K, B is further clockwise than C...
        if cols[0] != "W" and cols[0] != "K" and cols[4] != "W" and cols[4] != "K":
            swap(stage_cols, cols[0], cols[4])  # Swap top and bottom (if neither are W/K)
        if debug:
            print("After rule #13: " + str(stage_cols))
    return stage_cols  # Finally, return the list with swaps applied


def cycle_pri(l: list) -> None:
    """Small method to cycle the primary colors (R->G, G->B, B->R)"""
    swap(l, "R", "G")  # RGB -> GRB
    swap(l, "R", "B")  # -> GBR (correct)


def cycle_sec(l: list) -> None:
    """Small method to cycle the secondary colors (C->M, M->Y, Y->C)"""
    swap(l, "C", "M")  # CMY -> MCY
    swap(l, "C", "Y")  # -> MYC (correct)


def swap(l: list, a: str, b: str) -> None:
    """A method for swapping two strings in a list (uses below method)."""
    swap_int(l, l.index(a), l.index(b))  # Gets indexes and passes to swap_int


def swap_int(l: list, a: int, b: int) -> None:
    """A method for swapping two strings in a list by using their indexes."""
    l[a], l[b] = l[b], l[a]  # Note: these small functions help reduce code size
