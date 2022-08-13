matrix1 = [[1, 2], [3, 4], [5, 6]]
matrix2 = [[7, 8, 10], [9, 10, 11], [11, 12, 13]]

def printMatrix(aMatrix) :
    ''' prints a matrix (with row and column numbers),
        one row per line; aMatrix is a 2 d list
    '''
    #column numbers across top
    print(' '*5, end = '')
    for colNum in range(1, len(aMatrix[0]) + 1):
        print('{:^4}'.format(colNum), end='')
    print()
    print(' '*5, end = '')
    print('-'*4*len(aMatrix[0]))

    rowNum = 1    
    for row in aMatrix :
        print('{:^4}'.format(rowNum), end = '')
        print('|', end = '')
        rowNum += 1
        for element in row :
            print('{:^4}'.format(element), end='')
        print()

def displayGrid(size, pointsList):
    '''prints a grid of <size> X <size>, with stars in the
       locations specified by the <pointsList>.  Points not in the
       grid give error message.  The pointsList is a list of 2-d tuples.
       <size> should be a positive integer.
    '''

    #make grid
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row = row + ['.']
        matrix = matrix + [row]
        
    #add stars
    for point in pointsList:
        if point[0] > size or point[-1] > size:
            print('ERROR ', point, 'is not in range')
        else:
            matrix[point[0] - 1][point[-1] - 1] = '*'

    #print grid
    printMatrix(matrix)

displayGrid(7,[(1,1),(8,2),(4,8),(-2,3),(0,5)])

