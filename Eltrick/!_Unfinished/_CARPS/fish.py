import random
import tkinter as tk
import tkinter.font as font

window = tk.Tk()
states = ["NULL", "ROCK", "PAPER", "SCISSORS"]
pointer = 0
colours = ["black", "red", "green2", "blue"]
grid = [[0] * 6 for i in range(8)]
buttons = [[None] * 6 for i in range(8)]
functionality = [None] * 3

def setup():
    global pointer
    global grid
    # Main grid
    for i in range(64):
        r = i // 8
        c = i % 6
        button = tk.Button(
            window,
            width = 8,
            height = 4,
            bg = colours[0],
            activebackground = colours[0],
            command = lambda row = r, col = c: press(row, col)
        )
        buttons[r][c] = button
        button.grid(row = r, column = c)
    rock = tk.Button(
        window,
        width = 14,
        height = 4,
        bg = "red",
        activebackground = "red",
        command = lambda: alterSelectedState(1)
    )
    rock.grid(row = 10, column = 0, columnspan = 2)
    paper = tk.Button(
        window,
        width = 14,
        height = 4,
        bg = "green2",
        activebackground = "green2",
        command = lambda: alterSelectedState(2)
    )
    paper.grid(row = 10, column = 2, columnspan = 2)
    scissors = tk.Button(
        window,
        width = 14,
        height = 4,
        bg = "blue",
        activebackground = "blue",
        command = lambda: alterSelectedState(3)
    )
    scissors.grid(row = 10, column = 4, columnspan = 2)
    next = tk.Button(
        window,
        width = 54,
        height = 4,
        bg = "DodgerBlue2",
        activebackground = "DodgerBlue2",
        command = lambda: iterateGrid()
    )
    next.grid(row = 11, column = 0, columnspan = 6)

def press(row, col):
    global pointer
    grid[row][col] = pointer
    buttons[row][col]["bg"] = colours[pointer]
    buttons[row][col]["activebackground"] = colours[pointer]
    
def alterSelectedState(newState):
    global pointer
    if pointer == newState:
        pointer = 0
    else:
        pointer = newState

def iterateGrid():
    tempGrid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for i in range(64):
        occurences = []
        r = i // 8
        c = i % 6
        occurences.append(grid[r-1][c-1])
        occurences.append(grid[r-1][c])
        occurences.append(grid[r-1][(c+1)%6])
        occurences.append(grid[r][c-1])
        occurences.append(grid[r][(c+1)%6])
        occurences.append(grid[(r+1)%8][c-1])
        occurences.append(grid[(r+1)%8][c])
        occurences.append(grid[(r+1)%8][(c+1)%6])
        if grid[r][c] == 0:
            if occurences.count(0) == 8 or (occurences.count(1) == occurences.count(2) and occurences.count(2) == occurences.count(3)):
                tempGrid[r][c] = 0
            elif (occurences.count(1) == occurences.count(2) and occurences.count(1) > 1) or (occurences.count(2) == occurences.count(3) and occurences.count(2) > 1) or (occurences.count(1) == occurences.count(3) and occurences.count(3) > 1):
                if occurences.count(1) == occurences.count(2):
                    tempGrid[r][c] = 2
                elif occurences.count(2) == occurences.count(3):
                    tempGrid[r][c] = 3
                elif occurences.count(1) == occurences.count(3):
                    tempGrid[r][c] = 1
            else:
                count = [0, 0, 0]
                count[0] = occurences.count(1)
                count[1] = occurences.count(2)
                count[2] = occurences.count(3)
                tempGrid[r][c] = count.index(max(count))
        else:
            currentState = grid[r][c]
            if occurences.count(bound(currentState - 1)) >= occurences.count(bound(currentState + 1)):
                tempGrid[r][c] = currentState
            else:
                tempGrid[r][c] = bound(currentState + 1)
    for i in range(64):
        r = i // 8
        c = i % 6
        grid[r][c] = tempGrid[r][c]
    updateGrid()

def updateGrid():
    for i in range(64):
        r = i // 8
        c = i % 6
        buttons[r][c]["bg"] = colours[grid[r][c]]
        buttons[r][c]["activebackground"] = colours[grid[r][c]]

def bound(val) -> int:
    if val == 0:
        val = 3
    elif val == 4:
        val = 1
    else:
        val = val
    return val

setup()
window.mainloop()