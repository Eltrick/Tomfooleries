import time
from numpy import *

def main() -> None:
    temporaryInfo = []
    moduleInfo = []
    differences = []

    for i in range(0, 17):
        temporaryInfo = [int(x) for x in list(input("Enter state #" + str(i) + " of module: "))]
        moduleInfo.append(temporaryInfo.copy())
        if i != 0:
            for j in range(0, len(temporaryInfo)):
                temporaryInfo[j] = (temporaryInfo[j] - moduleInfo[i - 1][j]) % 10
        differences.append(temporaryInfo)
    differences.pop(0)
    # print(differences)

    tempMatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(0, len(differences)):
        for j in range(0, len(differences[i])):
            tempMatrix[j][i] = differences[i][j]
    

    for i in range(0, len(differences)):
        temp = ""
        for j in range(0, len(differences[i])):
            if j == 15:
                temp += str(differences[j][i]) + "*r[" + str(j + 1) + "] % 10" + "=" + str(((0 - moduleInfo[16][i]) + 10) % 10)
                break
            else:
                temp += str(differences[j][i]) + "*r[" + str(j + 1) + "]" + "+"
        print(temp)
    
    # matrix = sympy.Matrix(differences.copy())
    # diag = matrix.diagonalize()
    # print("D = " + diag)
    
    identity = []
    for i in range(0, len(moduleInfo) - 1):
        temporaryRow = [0] * (len(moduleInfo) - 1)
        temporaryRow[i] = 1
        identity.append(temporaryRow)

    mat = append(array(tempMatrix), array(identity), 1)

def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return vstack([A[:1], hstack([A[1:,:1], B]) ])

if __name__ == "__main__":
    main()