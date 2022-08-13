#Completion_Chart.py
#by: Nathan Pelletier
#November 2, 2015

#Creates numbered graph and then uses a matrix to convert the given tuple
#to a usable format. It then fills the grid with the apropriate stars

#bugs:
#     can not use a non-tuple or list format for star_points 
#     can not use letters or symbols

#feed back corner:
#Please explain how to remove brackets from a printed list.
#Though I may seem to have a grasp on indexing and matrixes I am still
#thoroughly lost in the topic
#OH and cool quotes from Einstine

##Project goals:INCOMPLETE                                          !=done
##          Print a row and colum of numbers assigned to a varible!
##          Use a user inputed matrix into a grid format!
##          Print stars in said spots!
##          If not a grid print error!
##          If out of range print error!
##          removing the brackets 

def displayGrid (size,star_points):
    '''Uses a given number to create a grid, then uses a list of data as
       co-ordanite points to place stars on the grid
       use a [(5,1),(4,3),(1,1)] format to enter data for star_points'''
    control = 0    #limits the matrix in its for loop
    matrix=[]       #a matrix with coordinates to use the tuple

    if size > 0:    #create grid

        for creation in range(0,size):    #creates loop to fill matrix
            matrix1 = [''] * size
            matrix.append(matrix1)

        for index in star_points:       #reads and interprets tuple
            y = index[1]
            x = index[0]

            if size >= x and size >= y:     #adds a star to list
                matrix[x-1][y-1] = ('*')

            else:                           #avoids an error and explains
                print('ERROR -- ','(', x,',',y,') OUT OF RANGE')
            
        for col in range(1,size+1):     #creates numbers for colums
            print(' ',col,end='')
        print()

        for row in range(1,size+1):     #creates numers for rows and
            print(row,matrix[control])  #adds the filled matrix
            control = control + 1       #while control keeps matrix to one
                                        #copy
    else:    #dousn't create grid
        print('ERROR -- FAILED TO CREATE GRID')
displayGrid(7, [[1,2],(5,1),(3,4),(3,4),(6,1)]) #testing

##print(1,2,3,4,5) 
##for i in range(1,6):
##    print(i,end=' ')
##finding universal code that equivilates to 
