matrix1 = [[1, 2], [3, 4], [5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

def printMatrix(aMatrix) :
    ''' prints a matrix, one row per line; aMatrix
        is a 2 d list
    '''
    for row in aMatrix :
        for element in row :
            print('{:3}'.format(element), end=' ')
        print()
        
def addMatrices(matrix1, matrix2) :
    ''' adds two matrices (in 2 d lists), matrix1 + matrix2
        returns answer as a matrix (a 2 d list)
    '''
    ##eventually make sure they are the same size
    #save result in matrix3
    matrix3 = []
    for rowIndex in range(0, len(matrix1)) :
        row = []
        for colIndex in range(0, len(matrix1[0])) :
            row = row + [0]
        matrix3 = matrix3 + [row]
    printMatrix(matrix3)
    
    for rowIndex in range(0, len(matrix1)) :
        for colIndex in range(0, len(matrix1[0])) :
            #len of first row is num of columns
                matrix3[rowIndex][colIndex] = matrix1[rowIndex][colIndex] + matrix2[rowIndex][colIndex]
    return matrix3

printMatrix(matrix1)
print()
printMatrix(matrix2)
printMatrix(addMatrices(matrix1, matrix2))

