matrix1 = [[1,2], [3,4], [5,6]]
matrix2 = [[7,8], [9,10], [11,12]]

def print_matrix(a_matrix):
    '''prints a matrix (with row and colunm numbers),
       one row per line; a_matrix is a 2-d list
    '''
    #coumn numbers across top
    print(' '*5, end = '')
    for col_num in range(1, len(a_matrix) + 1):
        print('{:4}'.format(col_num),end='')
    print()
    print(' '*5, end = '')
    print('_' *4*len(a_matrix[0]))    

    row_num = 1
    for row in range(a_matrix):
        print('{:4}'.format(row),end='')
        print('|',end = '')
        row_num += 1
        for element in row :
            print('{:^4}'.format(element),end = '')
        print()    

    for row in a_matrix:
        for element in row :
            print('{:^4}'.format(element), end='')
        print()

def display_grid(size, points_list):
    '''prints a grid of <size> X <size>, with stars in the
       location specified by the <points_list>. Points not in the
       grid give error message. The points_list is a list of 2-d tuple
       <size> should be a positive interger.
    '''
    #make grid
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row = row + [' ']
        matrix = matrix + [row]
    
    #adds stars
    for point in points_list:
        if point[0] > size or point[1] > size or \
        point[0] < 1 or point[1] < 1:
            print('Error', point, 'is not in range')
        else:
            matrix[point[0] - 1][point[1] - 1] = '*'
            
    #print grid
    print_matrix(matrix)
    
print_matrix(display_grid(7,[(1,1),(2,2),(3,3),(7,7),(6,2),(3,1),(8,2),(4,8),(-2,3),(0,5)]))
