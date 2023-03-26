import keyboard
import tkinter as tk
import tkinter.font as font

window = tk.Tk()
states = [0, 1, 2]
pointer = 0
colours = ["black", "DodgerBlue2", "green", "red"]
surroundingColours = ["black", "red", "green2", "blue", "white", "yellow", "magenta", "cyan"]
grid = [[0] * 6 for i in range(6)]
buttons = [[None] * 6 for i in range(6)]
functionality = None
rowtransf = [-1, -1, -1, 0, 1, 1, 1, 0]
coltransf = [-1, 0, 1, 1, 1, 0, -1, -1]
latestRow = 0
latestCol = 0
functionalityPivot = [3, 11]

def setup():
    global grid
    global latestRow
    global latestCol
    
    for i in range(36):
        r = i // 6
        c = i % 6
        button = tk.Button(
            window,
            width = 8,
            height = 4,
            bg = colours[0],
            activebackground = colours[0],
            command = lambda row = r, col = c: Press(row, col)
        )
        buttons[r][c] = button
        button.grid(row = r, column = c)
    reset = tk.Button(
        window,
        width = 55,
        height = 4,
        bg = colours[3],
        activebackground = colours[3],
        command = lambda: ResetGrid()
    )
    reset.grid(row = 8, column = 0, columnspan = 6)
    for i in range(8):
        r = functionalityPivot[0] + rowtransf[i]
        c = functionalityPivot[0] + coltransf[i]
        button = tk.Button(
            window,
            width = 8,
            height = 4,
            bg = colours[0],
            activebackground = colours[0],
            command = lambda row = r, col = c, idx = i: ColourSurroundings(latestRow, latestCol, rowtransf[idx], coltransf[idx])
        )
        button.grid(row = r, column = c + 8)

def Press(row, col):
    global latestRow
    global latestCol

    grid[row][col] = 2 if grid[row][col] == 2 else grid[row][col] + 1
    buttons[row][col]["bg"] = colours[grid[row][col]]
    buttons[row][col]["activebackground"] = colours[grid[row][col]]
    latestRow = row
    latestCol = col
    
    if grid[row][col] == 2:
        for i in range(36):
            r = i // 6
            c = i % 6
            if not (row == r and col == c):
                grid[r][c] = 0
                buttons[r][c]["bg"] = colours[grid[r][c]]
                buttons[r][c]["activebackground"] = colours[grid[r][c]]
    else:
        for i in range(36):
            r = i // 6
            c = i % 6
            buttons[r][c]["bg"] = colours[grid[r][c]]
            buttons[r][c]["activebackground"] = colours[grid[r][c]]

def ResetGrid():
    for i in range(36):
        row = i // 6
        col = i % 6
        grid[row][col] = 0
        buttons[row][col]["bg"] = colours[0]
        buttons[row][col]["activebackground"] = colours[0]

def FindIndices(array, value) -> list:
    result = []
    for i in range(len(array)):
        if array[i] == value:
            result.append(i)
    return result

def Intersection(arrayA, arrayB) -> list:
    result = []
    if len(arrayA) >= len(arrayB):
        for i in range(len(arrayA)):
            if arrayA[i] in arrayB:
                result.append(arrayA[i])
    else:
        for i in range(len(arrayB)):
            if arrayB[i] in arrayA:
                result.append(arrayB[i])
    return result

def ColourSurroundings(pivotRow, pivotColumn, rowOffset, columnOffset):
    start = Intersection(FindIndices(rowtransf, rowOffset), FindIndices(coltransf, columnOffset))[0]
    for i in range(8):
        iteration = (start + i) % 8
        newRow = (pivotRow + rowtransf[iteration]) % 6
        newColumn = (pivotColumn + coltransf[iteration]) % 6
        buttons[newRow][newColumn]["bg"] = surroundingColours[i]
        buttons[newRow][newColumn]["activebackground"] = surroundingColours[i]

setup()
window.mainloop()