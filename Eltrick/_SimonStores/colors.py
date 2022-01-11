def order(stage_cols: list, cols: list) -> list:
    print("Initial color list: " + str(stage_cols))
    if cols[1] == "Y": #If TR = Yellow
        stage_cols = [stage_cols[5]] + stage_cols[:5]
        print("After rule #1: " + str(stage_cols))
    if abs(cols.index("R") - cols.index("C")) == 4: #If Red opposite Cyan
        swap(stage_cols, "R", "C")
        swap(stage_cols, "G", "M")
        swap(stage_cols, "B", "Y")
        print("After rule #2: " + str(stage_cols))
    if abs(cols.index("G") - cols.index("W")) == 1 or abs(cols.index("G") - cols.index("W")) == 7:  #If Green adjacent to White
        cycle_pri(stage_cols)
        print("After rule #3: " + str(stage_cols))
    if abs(cols.index("M") - cols.index("K")) == 1 or abs(cols.index("M") - cols.index("K")) == 7: #If Magenta adjacent to Black
        cycle_sec(stage_cols)
        print("After rule #4: " + str(stage_cols))
    if (1 <= cols.index("B") <= 3 and 1 <= cols.index("Y") <= 3) or (5 <= cols.index("B") <= 7 and 5 <= cols.index("Y") <= 7):
        swap_int(stage_cols, stage_cols.index("B"), 5 - stage_cols.index("B"))  # Swap B with its opposite in the list.
        print("After rule #5: " + str(stage_cols))
    if 1 <= cols.index("R") <= 3:  # If red is on the right...
        swap(stage_cols, "R", "Y")
        print("After rule #6: " + str(stage_cols))
    if 5 <= cols.index("B") <= 7:  # If blue is on the left...
        swap(stage_cols, "G", "C")
        print("After rule #7: " + str(stage_cols))
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