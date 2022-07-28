"""
This file contains one dict of lists to
store color orders, two dicts of tuples
with each tuple containing three lambdas,
and finally a basic tuple for base-36.
For the first tuple dict (mono, 1 rotation),
the rotation of the 6D cube is the key,
and the value tuple contains the functions
for module stages 1, 2, and 3 in that order.
The second one (poly, multiple rotations)
has similar values, but the keys have to
be computed in solver.py and the functions
begin relying on single rotation functions.
A helper method is used to put all of the
results between -364 and 364 inclusive.
"""

b_36 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B",
        "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

stage_cols = {0: ["R", "G", "B", "C", "M", "Y"],
              1: ["Y", "B", "M", "G", "R", "C"],
              2: ["M", "C", "R", "Y", "G", "B"]}

"""
MONO: Definitions of single (mono) rotation functions (5 args: x d n a b)
x is the number put into the function (a_n-1 for stage 1, b_n-1 for stage 2, c_n-1 for stage 3)
d is the constant sum of the base-36 digits in the serial number, notated in the manual as D
n is the position of this rotation in the sequence of rotations (from 1 to stage+2, a_4 = 0)
a is a_n-1, used in many functions for stages 2 and 3 (the same as x in stage 1)
b is b_n-1, used in many functions for stage 3 (the same as x in stage 2)
"""
mono = {"XY": ((lambda x, d, n, a, b: bound(x + d)),
               (lambda x, d, n, a, b: bound(x + a)),
               (lambda x, d, n, a, b: bound(x + b - a))),
        "XZ": ((lambda x, d, n, a, b: bound(2 * x - d)),
               (lambda x, d, n, a, b: bound(2 * x - a)),
               (lambda x, d, n, a, b: bound(2 * x - b - a))),
        "YZ": ((lambda x, d, n, a, b: bound(x + 2 * d)),
               (lambda x, d, n, a, b: bound(x + 2 * a)),
               (lambda x, d, n, a, b: bound(x + 2 * b - a))),
        "XW": ((lambda x, d, n, a, b: bound(2 * d - x)),
               (lambda x, d, n, a, b: bound(3 * d - x - a)),
               (lambda x, d, n, a, b: bound(4 * d - x - b - a))),
        "YW": ((lambda x, d, n, a, b: bound(2 * x + d - 35 * n)),
               (lambda x, d, n, a, b: bound(2 * x + abs(a) - 12 * pow(n, 2))),
               (lambda x, d, n, a, b: bound(2 * x + abs(b) + abs(a) - 5 * pow(n, 3)))),
        "ZW": ((lambda x, d, n, a, b: bound(x + pow((x % 6), 3))),
               (lambda x, d, n, a, b: bound(x + pow((a % 7), 3))),
               (lambda x, d, n, a, b: bound(x + pow((b % 6), 3) + pow((a % 6), 3)))),
        "XV": ((lambda x, d, n, a, b: bound(2 * (d - x))),
               (lambda x, d, n, a, b: bound(2 * x - 3 * (d - a))),
               (lambda x, d, n, a, b: bound(2 * x - 4 * (d - b)))),
        "YV": ((lambda x, d, n, a, b: bound(x + pow((d % 6), 3) - 35 * n)),
               (lambda x, d, n, a, b: bound(x + pow((a % 7), 3) - 12 * pow(n, 2))),
               (lambda x, d, n, a, b: bound(x + pow((b % 8), 3) - 5 * pow(n, 3)))),
        "ZV": ((lambda x, d, n, a, b: bound((x - x % 2) / 2 + d)),
               (lambda x, d, n, a, b: bound(x + (x - x % 2) / 2 - a)),
               (lambda x, d, n, a, b: bound((x - x % n) / n + 2 * b))),
        "WV": ((lambda x, d, n, a, b: bound(5 * x - 3 * d)),
               (lambda x, d, n, a, b: bound(8 * x - 5 * d + 3 * a)),
               (lambda x, d, n, a, b: bound(13 * x - 8 * d + 5 * a - 3 * b))),
        "XU": ((lambda x, d, n, a, b: bound(x + 365 - d)),
               (lambda x, d, n, a, b: bound(x + 365 - abs(a))),
               (lambda x, d, n, a, b: bound(x + 365 - abs(a) - abs(b)))),
        "YU": ((lambda x, d, n, a, b: bound(2 * x - 365 + d)),
               (lambda x, d, n, a, b: bound(2 * x - 365 + abs(a))),
               (lambda x, d, n, a, b: bound(2 * x - 365 + abs(a) + abs(b)))),
        "ZU": ((lambda x, d, n, a, b: bound(x + 365 - 2 * d)),
               (lambda x, d, n, a, b: bound(x + 365 - 2 * abs(a))),
               (lambda x, d, n, a, b: bound(x + 365 - 2 * abs(a) - 2 * abs(b)))),
        "WU": ((lambda x, d, n, a, b: bound(365 - abs(x))),
               (lambda x, d, n, a, b: bound(365 - abs(x) - abs(a))),
               (lambda x, d, n, a, b: bound(365 - abs(x) - abs(a) - abs(b)))),
        "VU": ((lambda x, d, n, a, b: bound(n * x)),
               (lambda x, d, n, a, b: bound(n * (x - a))),
               (lambda x, d, n, a, b: bound(n * (x - a + b)))),
        "YX": ((lambda x, d, n, a, b: bound(x - d)),
               (lambda x, d, n, a, b: bound(x - a)),
               (lambda x, d, n, a, b: bound(x - b + a))),
        "ZX": ((lambda x, d, n, a, b: bound(2 * x + d)),
               (lambda x, d, n, a, b: bound(2 * x + a)),
               (lambda x, d, n, a, b: bound(b + a - 2 * x))),
        "ZY": ((lambda x, d, n, a, b: bound(x - 2 * d)),
               (lambda x, d, n, a, b: bound(x - 2 * a)),
               (lambda x, d, n, a, b: bound(x + 2 * a - b))),
        "WX": ((lambda x, d, n, a, b: bound(2 * d + x)),
               (lambda x, d, n, a, b: bound(3 * d + x - a)),
               (lambda x, d, n, a, b: bound(4 * d + x - b - a))),
        "WY": ((lambda x, d, n, a, b: bound(2 * x - d - 35 * n)),
               (lambda x, d, n, a, b: bound(2 * x - abs(a) - 12 * pow(n, 2))),
               (lambda x, d, n, a, b: bound(2 * x - abs(b) - abs(a) - 5 * pow(n, 3)))),
        "WZ": ((lambda x, d, n, a, b: bound(x - pow((x % 7), 3))),
               (lambda x, d, n, a, b: bound(x - pow((a % 6), 3))),
               (lambda x, d, n, a, b: bound(x - pow((b % 7), 3) - pow((a % 7), 3)))),
        "VX": ((lambda x, d, n, a, b: bound(2 * (d + x))),
               (lambda x, d, n, a, b: bound(2 * x - 3 * (d + a))),
               (lambda x, d, n, a, b: bound(2 * x - 4 * (d + b)))),
        "VY": ((lambda x, d, n, a, b: bound(x - pow((d % 6), 3) - 35 * n)),
               (lambda x, d, n, a, b: bound(x - pow((a % 7), 3) - 12 * pow(n, 2))),
               (lambda x, d, n, a, b: bound(x - pow((b % 8), 3) - 5 * pow(n, 3)))),
        "VZ": ((lambda x, d, n, a, b: bound((x - x % 2) / 2 - d)),
               (lambda x, d, n, a, b: bound(x + (x - x % 2) / 2 + a)),
               (lambda x, d, n, a, b: bound((x - x % n) / n - 2 * b))),
        "VW": ((lambda x, d, n, a, b: bound(5 * x + 3 * d)),
               (lambda x, d, n, a, b: bound(8 * x + 5 * d - 3 * a)),
               (lambda x, d, n, a, b: bound(13 * x + 8 * d - 5 * a + 3 * b))),
        "UX": ((lambda x, d, n, a, b: bound(x - 365 - d)),
               (lambda x, d, n, a, b: bound(x - 365 - abs(a))),
               (lambda x, d, n, a, b: bound(x - 365 + abs(a) - abs(b)))),
        "UY": ((lambda x, d, n, a, b: bound(2 * x - 365 - d)),
               (lambda x, d, n, a, b: bound(2 * x - 365 - abs(a))),
               (lambda x, d, n, a, b: bound(2 * x - 365 + abs(a) - abs(b)))),
        "UZ": ((lambda x, d, n, a, b: bound(x + 365 + 2 * d)),
               (lambda x, d, n, a, b: bound(x + 365 + 2 * abs(a))),
               (lambda x, d, n, a, b: bound(x + 365 + 2 * abs(a) - 2 * abs(b)))),
        "UW": ((lambda x, d, n, a, b: bound(365 - 2 * abs(x))),
               (lambda x, d, n, a, b: bound(365 - 2 * abs(x) - abs(a))),
               (lambda x, d, n, a, b: bound(365 - 2 * abs(x) - abs(a) - abs(b)))),
        "UV": ((lambda x, d, n, a, b: bound(n * x - d)),
               (lambda x, d, n, a, b: bound(n * (x - a - d))),
               (lambda x, d, n, a, b: bound(n * (x - a - b))))}

"""
POLY: Definitions of multiple (poly) rotation functions (8 args: r s t x d n a b)
x, d, n, a, and b share the same meanings from the mono dictionary (above)
r is one of the two or three rotations in the multiple rotation
s is another of the two or three rotations, like r (order doesn't matter!)
t is only used if there are three rotations, where it's the third one of the trio
"""
poly = {"X": ((lambda r, s, t, x, d, n, a, b: bound(2 * d - abs(mono[r][0](x, d, n, a, b)
                                                                - mono[s][0](x, d, n, a, b)))),
              (lambda r, s, t, x, d, n, a, b: bound(3 * d - abs(mono[r][1](x, d, n, a, b)
                                                                + mono[s][1](x, d, n, a, b)))),
              (lambda r, s, t, x, d, n, a, b: bound(4 * d - abs(mono[r][2](x, d, n, a, b))
                                                    - abs(mono[s][2](x, d, n, a, b))))),
        "Y": ((lambda r, s, t, x, d, n, a, b: bound(2 * d - mono[r][0](x, d, n, a, b)
                                                    - mono[s][0](x, d, n, a, b))),
              (lambda r, s, t, x, d, n, a, b: bound(2 * a - mono[r][1](x, d, n, a, b)
                                                    - mono[s][1](x, d, n, a, b))),
              (lambda r, s, t, x, d, n, a, b: bound(2 * b - mono[r][2](x, d, n, a, b)
                                                    - mono[s][2](x, d, n, a, b)))),
        "Z": ((lambda r, s, t, x, d, n, a, b: bound(mono[r][0](x, d, n, a, b)
                                                    + mono[s][0](x, d, n, a, b) - x)),
              (lambda r, s, t, x, d, n, a, b: bound(mono[r][1](x, d, n, a, b)
                                                    + mono[s][1](x, d, n, a, b) - x - a)),
              (lambda r, s, t, x, d, n, a, b: bound(mono[r][2](x, d, n, a, b)
                                                    + mono[s][2](x, d, n, a, b) - x - b - a))),
        "W": ((lambda r, s, t, x, d, n, a, b: bound(max(mono[r][0](x, d, n, a, b),
                                                        mono[s][0](x, d, n, a, b),
                                                        mono[t][0](x, d, n, a, b)) - 2 * d)),
              (lambda r, s, t, x, d, n, a, b: bound(mono[r][1](x, d, n, a, b)
                                                    + mono[s][1](x, d, n, a, b)
                                                    + mono[t][1](x, d, n, a, b) - 3 * x)),
              (lambda r, s, t, x, d, n, a, b: bound(mono[r][2](x, d, n, a, b)
                                                    + mono[s][2](x, d, n, a, b)
                                                    + mono[t][2](x, d, n, a, b) - a - b - x))),
        "V": ((lambda r, s, t, x, d, n, a, b: bound(min(mono[r][0](x, d, n, a, b),
                                                        mono[s][0](x, d, n, a, b),
                                                        mono[t][0](x, d, n, a, b)) + 2 * d)),
              (lambda r, s, t, x, d, n, a, b: bound(3 * x - mono[r][1](x, d, n, a, b)
                                                    - mono[s][1](x, d, n, a, b)
                                                    - mono[t][1](x, d, n, a, b))),
              (lambda r, s, t, x, d, n, a, b: bound(a + b + x - mono[r][2](x, d, n, a, b)
                                                    - mono[s][2](x, d, n, a, b)
                                                    - mono[t][2](x, d, n, a, b))))}


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
