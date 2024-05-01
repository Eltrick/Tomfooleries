import random
import math
from tkinter import *

window = Tk()
window.title("Pointer Pointer")

rowCount = 4
colCount = 4
states = [0, 1, 2]
pointer = 0
colours = ["black", "DodgerBlue2", "green", "red"]
surroundingColours = ["black", "red", "green2", "blue", "white", "yellow", "magenta", "cyan"]
grid = [[0] * colCount for i in range(rowCount)]
buttons = [[None] * colCount for i in range(rowCount)]
functionality = None
rowtransf = [-1, -1, -1, 0, 1, 1, 1, 0]
coltransf = [-1, 0, 1, 1, 1, 0, -1, -1]
latestRow = 0
latestCol = 0
functionalityPivot = [2, 11]

def Setup():
    global grid
    global latestRow
    global latestCol
    
    for i in range(colCount * rowCount):
        r = i // rowCount
        c = i % colCount
        button = Button(
            window,
            width = math.ceil(4 / 3 * colCount),
            height = math.ceil(2 / 3 * rowCount),
            bg = colours[0],
            activebackground = colours[0],
            command = lambda row = r, col = c: Press(row, col)
        )
        buttons[r][c] = button
        button.grid(row = r, column = c)
    reset = Button(
        window,
        width = math.ceil(55 / 8 * colCount),
        height = 4,
        bg = colours[3],
        activebackground = colours[3],
        command = lambda: ResetGrid()
    )
    reset.grid(row = rowCount + 1, column = 0, columnspan = colCount)
    for i in range(8):
        r = functionalityPivot[0] + rowtransf[i]
        c = functionalityPivot[0] + coltransf[i]
        button = Button(
            window,
            width = math.ceil(4 / 3 * colCount),
            height = math.ceil(2 / 3 * rowCount),
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
        for i in range(rowCount * colCount):
            r = i // rowCount
            c = i % colCount
            if not (row == r and col == c):
                grid[r][c] = 0
                buttons[r][c]["bg"] = colours[grid[r][c]]
                buttons[r][c]["activebackground"] = colours[grid[r][c]]
    else:
        for i in range(rowCount * colCount):
            r = i // rowCount
            c = i % colCount
            buttons[r][c]["bg"] = colours[grid[r][c]]
            buttons[r][c]["activebackground"] = colours[grid[r][c]]

def ResetGrid():
    for i in range(rowCount * colCount):
        row = i // rowCount
        col = i % colCount
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
        newRow = (pivotRow + rowtransf[iteration]) % rowCount
        newColumn = (pivotColumn + coltransf[iteration]) % colCount
        buttons[newRow][newColumn]["bg"] = surroundingColours[i]
        buttons[newRow][newColumn]["activebackground"] = surroundingColours[i]

def PickRandomIcon():
    x = random.randint(1, 8)
    window.iconbitmap("arrow" + str(x) + ".ico")

Setup()
PickRandomIcon()

window.mainloop()