# State, and trial are 5*5 arrays of colors, 012345 = RYGCBM for both
# Press takes (row, col, actual), use actual=False for trial
# Reset takes no arguments, use after trial checks

import tkinter as tk
import time
LETTERS = "ABCDE"
NUMBERS = [
  "█████"+
  "█   █"+
  "█   █"+
  "█   █"+
  "█████",

  "  █  "+
  "  █  "+
  "  █  "+
  "  █  "+
  "  █  ",

  "█████"+
  "    █"+
  "█████"+
  "█    "+
  "█████",

  "█████"+
  "    █"+
  "█████"+
  "    █"+
  "█████",

  "█   █"+
  "█   █"+
  "█████"+
  "    █"+
  "    █",

  "█████"+
  "█    "+
  "█████"+
  "    █"+
  "█████",

  "█████"+
  "█    "+
  "█████"+
  "█   █"+
  "█████",

  "█████"+
  "    █"+
  "    █"+
  "    █"+
  "    █",

  "█████"+
  "█   █"+
  "█████"+
  "█   █"+
  "█████",

  "█████"+
  "█   █"+
  "█████"+
  "    █"+
  "█████"
]  # Formations of 3CS digits (big)

DELAY = 0.01  # Delay between presses (for seeing the solve in action)

def cell_name(row, col):
  return LETTERS[col] + str(row + 1)

def log(row, col):  # Press a button and log it
  global presses, press, centers
  time.sleep(DELAY)  # Wait, then press
  cell = " " + cell_name(row, col)
  if(cell == " C3"):  # Center detection
    centers += 1
    centers %= 6
  #print(cell[1:])  # Logging part
  presses += cell
  press(row, col, True)

def finish():  # Finish the solve, including unlocking buttons
  global presses, buttons, extras
  print("press" + (" [no presses needed]" if presses == "" else presses))
  for row in buttons:
    for button in row:
      button["state"] = tk.NORMAL
  for button in extras:
    button["state"] = tk.NORMAL
  print("SOLVE COMPLETE - BUTTONS UNLOCKED")
  return "Done!"

def _check():  # Check without pressing (1 if good, 0 if neutral, -1 if bad)
  global state, trial, digit, color, PRINT
  for test_color in range(0, 6):
    cells = ""  # Get each color's pattern
    for row in trial:
      for cell in row:
        cells += "█" if cell == test_color else " "
    for test_digit in range(0, 10):  # Check all digits
      if(cells == NUMBERS[test_digit]):  # Formation found!
        if(PRINT):  # Print that it was found if it's not being spammed
          print("A formation was found in the grid!")
        # Check if it's the correct formation
        correct = test_digit == digit and color == test_color
        if(correct):  # Correct: wrap up the solve
          if(PRINT):  # (Also print the first time seeing this)
            print("\nIt's correct, finishing solve.")
          PRINT = False
          return 1
        else:  # Incorrect: check if the formation is safe
          # (Formation encoded as a number)
          result = -10 * test_color - 10 - test_digit
          if(decode(result)[1] == ALLOWED):  # Safe: return 0
            print("\nIt existed at the start, so it's safe.")
            return 0
          else:  # Unsafe: return the encoded number
            PRINT = False
            return result
  return 0  # If no incorrect unsafe formation found in any digit/color, return 0

def check(row, col=None):  # Press something and check it, workaround if needed
  global press, reset, ALLOWED
  if(col == None):  # Array extraction
    col = row[1]
    row = row[0]
  press(row, col, False)  # Trial press
  result = _check()
  if(result < 0):  # Workaround
    workaround(row, col)
    result = _check()
    if(result < 0):  # Workaround failure?
      print("Error: workaround failed to avoid incorrect formation!")
      exit(1)
  else:  # Actual press (safe)
    log(row, col)
  reset()  # Update trial grid with actual press/es
  return result == 1

def print_colors(ary):
  for row in range(0, 5):
    row_string = ""
    for col in range(0, 5):
      row_string += "RYGCBM"[ary[row][col]] + " "
    print(row_string[:-1])

def decode(code):
  # Invalid codes should only be encountered during testing
  global WORKAROUND_TEST_DIGIT
  if(not -69 <= code <= -10):
    return "unknown formation, testing", WORKAROUND_TEST_DIGIT
  # Extract and return the encoded information
  color_code = -code // 10 - 1
  digit_code = -code % 10
  return ("red", "yellow", "green", "cyan", "blue", "magenta")[
    color_code], digit_code  # Color first, then digit

def farthest_pressable(row, col):
  global press, reset
  pressable = []
  max_distance = 3
  reset()  # For accuracy
  for test_row in range(0, 5):
    for test_col in range(0, 5):
      distance = abs(test_row - row) + abs(test_col - col)
      if(distance < max_distance or ((test_row in (0, 5)) and (test_col in (0, 5)))):
        continue  # Don't bother testing too-close cells or corners
      if((row in (0, 5)) and (col in (0, 5)) and state[test_row][test_col] == 5):
        continue  # Also don't bother testing magentas if a corner is being pressed

      # Check that pressing the cell 6 times won't form anything bad
      all_safe = True
      for i in range(0, 6):
        press(test_row, test_col, False)
        if(_check() < 0):
          all_safe = False
          break

      # If the cell is safe to press 6 times, check its distance
      if(all_safe):
        # If it's farther than the former max, clear the list and update the max
        if(distance > max_distance):
          max_distance = distance
          pressable = []
        # Append the found safe cell regardless of whether the max updated
        pressable.append([test_row, test_col])
      # Finally, reset the trial grid for testing the next cell
      reset()
  return pressable

def workaround(row, col):  # If an incorrect digit is made, avoid it
  global state, trial, press, reset, STEP, PRINT, WORKAROUND_TEST_DIGIT
  WORKAROUND_TEST_DIGIT = 2

  code = _check()
  decoded = decode(code)
  full_color = decoded[0]
  color = full_color[0].upper()
  digit = decoded[1]

  print("\nInvalid formation detected!")
  print("Current state:\n")
  print_colors(state)  # Log as much as possible
  print("\nAttempted press: " + cell_name(row, col))
  print("Resulting state:\n")
  print_colors(trial)  # Print both code and decoded result
  print("\nFormation: " + str(code) + ", aka: " + full_color + " " + str(digit))

  # Determine which cells can be pressed 6x (resets trial before and after)
  pressable = farthest_pressable(row, col)

  # Workaround complete, now just reset the printing variable
  PRINT = True

# The main solve method, which is broken into parts
def solve(_buttons, _extras, _state, _trial, _press, _reset, _digit, _color):
  # Setup for most of the global variables (so they can be used across methods)
  global buttons, extras, state, trial, press, reset,\
    digit, color, presses, centers, ALLOWED, STEP, PRINT
  buttons, extras, state, trial, press, reset,\
    digit, color, presses, centers, ALLOWED, STEP =\
    _buttons, _extras, _state, _trial, _press, _reset,\
    _digit, _color, "", 0, -1, 10  # step//10=main-step, step%10=sub-step
  result = _check()  # Find any initial formation
  if(result == 1):  # Already solved?
    print("Already solved? Really?")
    return finish()  # Value not actually used in any "return finish()" lines
  if(result != 0):  # Formation safe to make?
    ALLOWED = decode(result)[1]
  PRINT = True  # Ensure printing starts enabled, then begin

  corners()  # A1, A5, E1, E5
  if(_check() == 1): return finish()
  STEP = 20
  edges()  # A3, C1, C5, E3
  if(_check() == 1): return finish()
  STEP = 30
  ace135()  # C3 + finish ACE135 setup
  if(_check() == 1): return finish()
  STEP = 40
  midedges()  # B3, C2, C4, D3
  if(_check() == 1): return finish()
  STEP = 50
  greens()  # A2, A4, E2, E4
  if(_check() == 1): return finish()
  STEP = 60
  cyans()  # B1, B5, D1, D5
  if(_check() == 1): return finish()
  STEP = 70
  yellows()  # B2, B4, D2, D4
  if(_check() != 1):  # Failed to solve?
    print("Warning: algorithm failed to solve formation!")
  return finish()  # Print presses even if failed to solve

def hit_corners():  # Helper method for hitting all four corners
  check(0, 0)
  check(0, 4)
  check(4, 0)
  check(4, 4)

def hit_altering():  # Helper method for hitting all altering cells from step 1
  check(0, 1)
  check(1, 4)
  check(3, 0)
  check(4, 3)

def magenta(board):  # Magenta detection (all magentas work the same)
  for row in range(0, 5):
    for col in range(0, 5):
      if(board[row][col] == 5):
        return row, col
  return -1, -1

def make_magenta(row=2, col=2, actual=True):  # Way of magenta creating/pressing
  cell = magenta(state)  # (Defaults to using center)
  while(cell[0] == -1):
    if(actual):
      check(row, col)
    else:
      press(row, col, False)
      return _check()
    cell = magenta(state)
  check(cell)
  return 0

# Main solve step 1
def corners():
  global state, STEP
  # Data in order (row, col, altering_row, altering_col)
  for corner in ((0, 0, 0, 1), (0, 4, 1, 4), (4, 0, 3, 0), (4, 4, 4, 3)):
    # 1. Set up cells adjacent to the corners (helpful here and later)
    while(state[corner[2]][corner[3]] != 0):
      # To do that, get the corner to red/blue and hit it
      while(state[corner[0]][corner[1]] not in (0, 4)):
        make_magenta()
      check(corner[0], corner[1])
    STEP += 1
    # 2. Get the corner to the same state as A1
    while(state[corner[0]][corner[1]] != state[0][0]):
      check(corner[2], corner[3])
    STEP += 1

# Main solve step 2
def edges():
  global state, STEP
  # 1. Get all corners to red/blue and hit each of them once
  while(state[0][0] not in (0, 4)):
    make_magenta()
  STEP += 1
  hit_corners()
  STEP += 1
  # Now the altering cells from step 1 are all yellow
  # Data in order (row, col, mid_row, mid_col, altering_row, altering_col)
  for edge in ((0, 2, 1, 2, 0, 1), (2, 0, 2, 1, 3, 0), (
    2, 4, 2, 3, 1, 4), (4, 2, 3, 2, 4, 3)):
    # 2. Set up the mid-edges (helpful here and later)
    while(state[edge[2]][edge[3]] != 0):
      # This is known to be yellow
      check(edge[4], edge[5])
    STEP += 1
    # 3. Get the edge to the same state as A1
    while(state[edge[0]][edge[1]] != state[0][0]):
      check(edge[2], edge[3])
    STEP += 1

# Main solve step 3
def ace135():
  global state, digit, color, STEP
  # 1. Hit all corners 5 times
  for i in range(0, 5):
    hit_corners()
  STEP += 1
  # Now the altering cells are red again
  # 2A. If the digit is 0, a separate order of alterations can make it faster
  if(digit == 0):
    # First ensure the center isn't the target color
    # (Keep alignment of the edges and corners together!)
    if(state[2][2] == color):
      check(1, 2)
      check(2, 1)
      check(2, 3)
      check(3, 2)
      make_magenta()
    STEP += 1
    # Then simply use the altering cells to make the 0 correctly colored
    while(state[0][0] != color):
      hit_altering()
    return
  # 2. Align the center and other squares (useless digit is 4)
  while(state[0][0] != state[2][2] and digit != 4):
    hit_altering()
  STEP += 1
  # 3. Get the edges to the target color
  # (Center will remain aligned if both possible and desired)
  while(state[0][2] != color):
    check(1, 2)
    check(2, 1)
    check(2, 3)
    check(3, 2)
  STEP += 1
  # 4. Fix certain squares for certain digits
  if(digit == 1):
    # For 1, disalign the left and right edges (and corners in step 5)
    check(2, 1)
    STEP += 1
    while(state[2][2] != color):
      check(2, 3)
  elif(digit == 4):
    # For 4, disalign the top and bottom edges, and the BL corner
    check(1, 2)
    STEP += 1
    while(state[2][2] != color):  # Also align center here
      check(3, 2)
    STEP += 1
    # This could be optimized, but it would result in a right-facing swastika
    # Instead, a left-facing swastika is used since that's NOT a hate symbol
    while(state[4][2] == color or state[4][0] == state[0][0]):
      # Optimizable part: aligning 4,1 specifically
      while(state[4][1] not in (0, 3, 4)):
        # ...Which requires aligning 4,0 too
        while(state[4][0] not in (0, 3, 4)):
          make_magenta()
        check(4, 0)
      # This last part doesn't go away with the optimization
      check(4, 1)
  elif(digit == 7):
    # For 7, disalign the cells that aren't on the top or right edge
    # B4's diagonals are those exact cells, so hit B4
    while(state[3][1] in (0, 5)):
      # Of course, it can't be red/magenta when hit
      while(state[4][0] in (0, 5)):
        make_magenta()
      check(4, 0)
    STEP += 1
    check(3, 1)

# Main solve step 4
def midedges():
  global state, digit, color, STEP
  # Data in order (row, col, altering_row, altering_col, corner_row, corner_col)
  for midedge in ((1, 2, 0, 1, 0, 0), (2, 1, 3, 0, 4, 0), (
    2, 3, 1, 4, 0, 4), (3, 2, 4, 3, 4, 4)):
    # While the mid-edge is (aligned if absent / disaligned if present)...
    while((state[midedge[0]][midedge[1]] == color) == (
      NUMBERS[digit][midedge[0] * 5 + midedge[1]] == " ")):
      # Set its altering cell to yellow using a corner then alter the mid-edge
      while(state[midedge[2]][midedge[3]] != 1):
        # The corner must be red/blue first, use another corner to make magenta
        while(state[midedge[4]][midedge[5]] not in (0, 4)):
          make_magenta(4, (4 if midedge[0] == 3 else 0))
        check(midedge[4], midedge[5])
      check(midedge[2], midedge[3])
    STEP += 1

# Main solve step 5
def greens():  # Short for "altered by green corners"
  global state, digit, color, STEP
  # Data in order (row, col, corner_row, corner_col)
  for green in ((1, 0, 0, 0), (1, 4, 0, 4), (3, 0, 4, 0), (3, 4, 4, 4)):
    # While the green is (aligned if absent / disaligned if present)...
    while((state[green[0]][green[1]] == color) == (
      NUMBERS[digit][green[0] * 5 + green[1]] == " ")):
      # Set its corner to green and hit it
      while(state[green[2]][green[3]] != 2):
        make_magenta()
      check(green[2], green[3])
    STEP += 1

# Main solve step 6
def cyans():  # Short for "altered by cyan corners"
  global state, digit, color, STEP
  # Data in order (row, col, corner_row, corner_col)
  for cyan in ((0, 1, 0, 0), (0, 3, 0, 4), (4, 1, 4, 0), (4, 3, 4, 4)):
    # While the cyan is (aligned if absent / disaligned if present)...
    while((state[cyan[0]][cyan[1]] == color) == (
      NUMBERS[digit][cyan[0] * 5 + cyan[1]] == " ")):
      # Set its corner to cyan and hit it
      while(state[cyan[2]][cyan[3]] != 3):
        make_magenta()
      check(cyan[2], cyan[3])
    STEP += 1
  # Also fix mid-edges here for easy checking (max 6 checks/5 presses)
  for i in range(0, 5):
    aligned = True  # Alignment test
    for midedge in ((1, 2), (2, 1), (2, 3), (3, 2)):
      if((state[midedge[0]][midedge[1]] == color) == (
        NUMBERS[digit][midedge[0] * 5 + midedge[1]] == " ")):
        aligned = False
        break
    if(aligned):  # If aligned, return, otherwise try again
      return
    if(i == 5):  # If not aligned after 5 presses, something's wrong
      print("Warning: Mid-edge fixing in cyans method failed!")
      return
    check(2, 2)
    STEP += 1

# Main solve step 7 (last step)
def yellows():  # Short for "altered by yellow corners"
  global state, digit, color, centers, STEP
  # Fast way for yellow center
  if(state[2][2] == 1):
    STEP = 77  # Indicator that yellow center is being used
    # Dis/align the corners to the target color depending on the digit
    # (1: while aligned, alter / else: while unaligned, alter)
    while((state[0][0] == color) == (digit == 1)):
      make_magenta()
    STEP += 1
    # Already solved?
    if(_check() == 1):
      return
    # If not, press center to solve (max 4 presses)
    for i in range(0, 4):
      if(check(2, 2)):
        return
    # If that fails, something's wrong
    print("Warning: Yellow center solve in yellows method failed!")
    return
  # Normal way (actually uses corners)
  # Data in order (row, col, corner_row, corner_col)
  centers = 0  # Start tracking center presses
  for yellow in ((1, 1, 0, 0), (1, 3, 0, 4), (3, 1, 4, 0), (3, 3, 4, 4)):
    # While the yellow is aligned (since yellows are always absent)...
    while((state[yellow[0]][yellow[1]] - centers + 6) % 6 == color):
      # Set its corner to yellow and hit it
      while(state[yellow[2]][yellow[3]] != 1):
        make_magenta()
      check(yellow[2], yellow[3])
    STEP += 1
  # Fix corners and possibly cells near center
  while((state[0][0] == color) == (digit == 1)):
    make_magenta()
  STEP += 1
  # Already solved?
  if(_check() == 1):
    return
  for i in range(0, 5):  # Max 5 presses
    if(check(2, 2)):
      return
  # If that fails, something's wrong
  print("Warning: Non-yellow center solve in yellows method failed!")