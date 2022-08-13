##AugLand class
##by Nathan Pelletier
##2015 Midterm
##
##Part of game board
##Represents a square land, containing princess and dragons
##

class AugLand():
    #DATA----------------------------------------------------------------
    #  land - a square matrix, initialized to creatures that occupy
    #         each space.  This initialization occurs in the constructor.
    #  size - the land is of dimension size X size.  This variable is
    #         also created in the constructor.


    #METHODS--------------------------------------------------------------
    #
    # 1)  Constructor __init__ : takes a square matrix and sets up object's
    #     data
    # 2)  __repr__ : gives a string to represent the land (2-d labeled grid)
    #
    #

    #CONSTRUCTOR
    def __init__(self, matrix):
        '''Constructor takes a square matrix (2-d structure) filled
           with creatures of the land (or blanks for empty places)

           self.land is set to the new matrix, to store the initial state
           self.size is set to the dimension of the matrix, i.e. to n
               if matrix is n X n
               
           No error checking is done.  You must ensure that the matrix is
           square.
        '''
        
        self.land = matrix
        self.size = len(matrix)
    #OVERWRITES DEFAULT REPRESENTATION
    #Returns string of a labelled grid showing where all creatures are
    def __repr__(self):
        '''Returns a string showing the land, with all creatures inhabiting
           it.
        '''
        rowNum = 1
        stringRep = 'AugLand\n'
        stringRep += '{:^5}'.format(' ')
                
        for colNum in range(1, self.size + 1):
            stringRep += '{:10}'.format(colNum)
        stringRep += '\n'
        
        for row in self.land:
            stringRep += '{:^10}'.format(rowNum)
            rowNum += 1
            for element in row:
                if element == ' ':
                    stringRep += '{:^10}'.format('--------')
                else:
                    stringRep += '{:^10}'.format(element)
            stringRep += '\n' 
        return stringRep


    ###PUT YOUR CODE HERE
    def findPrincess (self):
        'finds the princess and returns her location on grid'

        princess = 0      #so I call if no princess found
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.land[i] [j] == 'princess':  #finding her
                    princess = (i+1,j+1)        #princess found
                    return princess
                if princess == 0:
                    return 0,0

    def threat (self):
        '''calculates threat to princess via dragons in proximity and via
        her proximity to the edge'''

        ##only because I couldn't figure how to call back to it
        princess = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.land[i] [j] == 'princess': 
                    princess = (i+1,j+1) 

        meter = -1       #counts danger
        if princess != 0 and i != 0 and j != 0 \
           and i != self.size and j != self.size:
            #shlew above determines if princess is there and
            #if she's near a ledge

            meter = 0    #so it can start counting           

            if self.land [i] [j - 1] == 'dragon' :
                meter = meter + 1
            if self.land [i - 2] [j - 1] == 'dragon' :
                meter = meter + 1
            if self.land [i - 1] [j] == 'dragon' :
                meter = meter + 1
            if self.land [i - 1] [j - 2] == 'dragon' :
                meter = meter + 1
            if self.land [i] [j] == 'dragon' :
                meter = meter + 1
            if self.land [i - 2] [j] == 'dragon' :
                meter = meter + 1
            if self.land [i - 2] [j - 2] == 'dragon' :
                meter = meter + 1
            if self.land [i] [j - 2] == 'dragon' :
                meter = meter + 1
            #summary if dragon is left, right, above, below, or diagnal
                #add 1 to threat level
                
            print(meter)

    
###################################################################
###################################################################
##Some test worlds to use to help you with implementation:
##  y is the simplest
##
    
y = AugLand([[' ', 'dragon', 'dragon'],\
             [' ', 'princess', ' '],\
             ['dragon', ' ', ' ']])

a = AugLand([[' ', 'dragon', 'dragon'],\
             [' ', ' ', ' '],\
             ['dragon', ' ', 'princess']])

b = AugLand([[' ', 'dragon', 'princess'],\
             [' ', ' ', ' '],\
             ['dragon', ' ', ' ']])

c = AugLand([['princess', 'dragon', 'dragon'],\
             [' ', ' ', ' '],\
             ['dragon', ' ', ' ']])

d = AugLand([[' ', 'dragon', 'dragon'],\
             [' ', ' ', ' '],\
             ['princess', ' ', ' ']])

e = AugLand([[' ', 'dragon', 'dragon'],\
             [' ', ' ', 'princess'],\
             ['dragon', ' ', ' ']])

f = AugLand([[' ', 'princess', 'dragon'],\
             [' ', ' ', ' '],\
             ['dragon', ' ', ' ']])

g = AugLand([['dragon', 'dragon', 'dragon'],\
             ['princess', ' ', ' '],\
             ['dragon', ' ', ' ']])

h = AugLand([[' ', 'dragon', 'dragon'],\
             [' ', ' ', ' '],\
             [' ', 'princess', 'dragon']])

z = AugLand([['princess', ' ', ' ', ' '],\
             [' ', 'dragon', ' ', ' '],\
             ['dragon', 'dragon', ' ', ' '],\
             [' ', ' ', ' ', 'dragon']])

x = AugLand([['dragon', 'dragon', 'dragon', ' '],\
             ['dragon', ' ', 'princess', 'dragon'],\
             ['dragon', 'dragon', ' ', ' '],\
             [' ', ' ', ' ', 'dragon']])

w = AugLand([['dragon', ' ', 'dragon', ' '],\
             ['dragon', ' ', 'dragon', ' '],\
             ['dragon', 'dragon', ' ', ' '],\
             [' ', ' ', ' ', 'dragon']])

q = AugLand([['dragon', ' ', 'dragon', ' ', ' ', ' '],\
             ['dragon', ' ', 'dragon', ' ', ' ', 'dragon'],\
             ['dragon', 'dragon', 'dragon', ' ', 'princess', ' '],\
             ['dragon', 'dragon', ' ', 'dragon', ' ', 'dragon'],\
             ['dragon', 'dragon', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'dragon', ' ', ' ']])

r = AugLand([['dragon', ' ', 'dragon', ' ', ' ', ' '],\
             [' ', ' ', 'dragon', ' ', ' ', 'dragon'],\
             ['dragon', 'dragon', 'dragon', ' ', ' ', ' '],\
             ['dragon', 'dragon', ' ', 'dragon', ' ', 'dragon'],\
             [' ', 'dragon', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'dragon', 'dragon', ' ']])

s = AugLand([['princess']])

t = AugLand([[' ', 'dragon'],\
             ['dragon', 'princess']])
