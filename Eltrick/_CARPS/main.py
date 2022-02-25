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
    for i in range(48):
        r = i // 6
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
    tempGrid = [[0] * 6 for i in range(8)]
    for i in range(48):
        occurences = []
        r = i // 6
        c = i % 6
        occurences.append(grid[((r-1)+8)%8][((c-1)+6)%6])
        occurences.append(grid[((r-1)+8)%8][c])
        occurences.append(grid[((r-1)+8)%8][(c+1)%6])
        occurences.append(grid[r][((c-1)+6)%6])
        occurences.append(grid[r][(c+1)%6])
        occurences.append(grid[(r+1)%8][((c-1)+6)%6])
        occurences.append(grid[(r+1)%8][c])
        occurences.append(grid[(r+1)%8][(c+1)%6])
        counts = [0, 0, 0, 0]
        counts[1] = occurences.count(0)
        counts[1] = occurences.count(1)
        counts[2] = occurences.count(2)
        counts[3] = occurences.count(3)
        distinct = list(set(counts))
        print(counts)
        print(distinct)
        
        print("currentState = " + str(grid[r][c]))
        winner = max(counts[1], counts[2], counts[3])
        whenThe = 0
        for j in range(3):
            if counts[j + 1] == winner:
                whenThe += 1
        print("countTies = " + str(whenThe))
        
        if grid[r][c] == 0:
            if whenThe == 3 or counts[0] == 8:
                tempGrid[r][c] = 0
            elif whenThe == 2:
                if counts[1] == counts[2]:
                    tempGrid[r][c] = 2
                elif counts[2] == counts[3]:
                    tempGrid[r][c] = 3
                elif counts[3] == counts[1]:
                    tempGrid[r][c] = 1
            else:
                tempGrid[r][c] = counts.index(max(counts[1], counts[2], counts[3]))
                print("TG = " + str(tempGrid[r][c]))
        else:
            currentState = grid[r][c]
            if (counts[bound(currentState - 1)] >= counts[bound(currentState + 1)]):
                tempGrid[r][c] = currentState
                print("TG = " + str(tempGrid[r][c]))
            else:
                tempGrid[r][c] = bound(currentState + 1)
                print("TG = " + str(tempGrid[r][c]))
        print("")
    for i in range(48):
        r = i // 6
        c = i % 6
        grid[r][c] = tempGrid[r][c]
    updateGrid()

def updateGrid():
    for i in range(48):
        r = i // 6
        c = i % 6
        buttons[r][c]["bg"] = colours[grid[r][c]]
        buttons[r][c]["activebackground"] = colours[grid[r][c]]

def bound(val) -> int:
    if val == 0:
        val = 3
    elif val > 3:
        val = val % 3
    return val

setup()
window.mainloop()