import copy
import random
import solver
import tkinter as tk
import tkinter.font as font
import threading

# Comment out for true random
random.seed(5)  # Changable randomizer seed

window = tk.Tk()  # Main window of the GUI, initially empty
COLORNAMES = ["red", "yellow", "green", "cyan", "blue", "magenta"]
COLORS = "RYGCBM"  # Full names and abbreviations of colors
buttons = [[None] * 5 for i in range(5)]
extras = [None] * 3  # Close, edit, and solve buttons
state = [[0] * 5 for i in range(5)]
trial = [[0] * 5 for i in range(5)]
edit = False

# Setup the GUI
def setup():
  # Main grid
  for i in range(25):
    r = i // 5
    c = i % 5
    color = random.randint(0, 5)
    state[r][c] = color
    button = tk.Button(
      window,
      width=8,
      height=5,
      bg=COLORNAMES[color],
      activebackground=COLORNAMES[color],
      command=lambda row=r,col=c: press(row, col, True)
    )  # Array for reference in color changing
    buttons[r][c] = button
    button.grid(row=r, column=c)
  # Close button
  close = tk.Button(
    window,
    width=5,
    height=2,
    bg="orange",
    activebackground="orange",
    fg="black",
    text="CLOSE",
    font=font.Font(size=15),
    command=lambda: window.destroy()
  )  # Right of TR corner of board
  close.grid(row=0, column=5)
  extras[0] = close
  # Edit button
  edit = tk.Button(
    window,
    width=5,
    height=2,
    bg="grey",
    activebackground="grey",
    fg="red",
    activeforeground="red",
    text="EDIT",
    font=font.Font(size=15),
    command=lambda: toggleedit()
  )  # Right of MR edge of board
  edit.grid(row=2, column=5)
  extras[1] = edit
  # Solve button
  solve = tk.Button(
    window,
    width=5,
    height=2,
    bg="lime",
    activebackground="lime",
    fg="black",
    text="SOLVE",
    font=font.Font(size=15),
    command=lambda: prepsolve()
  )  # Right of BR corner of board
  solve.grid(row=4, column=5)
  extras[2] = solve
  reset()  # Trial grid setup

# Handle a press, actual or not
def press(row, col, temp):
  global actual  # Allow referencing in other methods
  if(edit):  # Edit mode: direct actual alter
    actual = True
    alter(row, col)
    return  # Otherwise...
  actual = temp  # Update actuality of press
  if(state[row][col] == 5):  # Magenta (corners only)
    alter(0, 0)
    alter(0, 4)
    alter(4, 0)
    alter(4, 4)
    return
  if(state[row][col] not in (1, 2)):  # All except Y/G
    horiz(row, col)
  if(state[row][col] not in (1, 3)):  # All except Y/C
    vert(row, col)
  if(state[row][col] != 0):  # All except R
    diag(row, col)
  actual = True  # Reset actuality to True

# Directly left and right
def horiz(row, col):
  alter(row, col-1)
  alter(row, col+1)

# Directly up and down
def vert(row, col):
  alter(row-1, col)
  alter(row+1, col)

# All four diagonals
def diag(row, col):
  alter(row-1, col-1)
  alter(row-1, col+1)
  alter(row+1, col-1)
  alter(row+1, col+1)

# Directly alter a coordinate
def alter(row, col):
  if(not 0 <= row <= 4 or not 0 <= col <= 4):
    return  # Don't alter outside the grid
  trial[row][col] = (trial[row][col] + 1) % 6
  if(actual):  # Only sometimes update actual state
    state[row][col] = (state[row][col] + 1) % 6
    buttons[row][col]["bg"] = COLORNAMES[state[row][col]]
    buttons[row][col]["activebackground"] = COLORNAMES[state[row][col]]

# Resets changes to trial grid
def reset():
  for i in range(25):
    r = i // 5
    c = i % 5
    trial[r][c] = state[r][c]

def toggleedit():
  global edit  # Allows accurate toggle
  edit = not edit  # Text color indicates edit status
  fg = "lime" if edit else "red"
  extras[1]["fg"] = fg  # Updating
  extras[1]["activeforeground"] = fg

# Prepare the board when solve starts/ends
def prepsolve():
  # Disable edit mode and all buttons
  if edit:
    toggleedit()
  for row in buttons:
    for button in row:
      button["state"] = tk.DISABLED
  for button in extras:
    button["state"] = tk.DISABLED
  print("SOLVE INITIATED - BUTTONS LOCKED")
  
  digit = input("Enter a digit to make: ")
  while(len(digit) != 1 or digit not in "0123456789"):
    digit = input("Invalid digit. Enter a digit to make: ")
  digit = int(digit)  # Remember to make the digit an integer!

  options = "RYGCBM"  # Allowable colors (initially all 6)
  if(digit not in (0, 1, 4, 7)):  # Hard digit, check parity
    options = "RGB" if isprimary() else "YCM"
    print("Only some colors are possible for this digit/board: " + options)

  color = input("Enter a target color (RYGCBM): ").upper()
  while(len(color) != 1 or color not in options):  # Color checking
    if(options != "RYGCBM"):  # If options are restricted, print a reminder
      print("Remember, only the following colors work this time: " + options)
    color = input("Invalid color. Enter a target color (RYGCBM): ").upper()
  
  print("Solve in progress...")
  # Actual solve for the target digit and color, prints path
  thread = threading.Thread(target=solver.solve, args=(
    buttons, extras, state, trial, press, reset, digit, COLORS.index(color)))
  thread.start()  # Multithreading allows buttons to change color

def isprimary():
  return (state[0][0] + state[0][2] + state[0][4] +\
    state[2][0] + state[2][2] + state[2][4] +\
    state[4][0] + state[4][2] + state[4][4]) % 2 == 0

# The main code
setup()  # Self-explanatory
window.mainloop()
print("GUI window closed.")