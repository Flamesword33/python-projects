#Othello.py
#Jamie Plant
#Date Finished

#Plays the bored game of Othello (Reversi)
#Stones are placed on a grid. If you surround the stones of your opponent 
#in a straight line the stones are flipped (or reversed). The game is played 
#until there are no more legal moves. Stones can only be placed adjacently 
#to other stones. This game is played between a human player and a computer

#/////////////
#//FUNCTIONS//
#/////////////
#start_game()
#game_board()
#human_turn(list[][], int, char)
#machine_turn(list[][], int, int, char)
#find_available_moves()
#all_spots_chosen()
#adjacent(int,int)

import random

#Determines how many rows the game board will have
rows= eval(input('Enter the rows that you want: (1-9)' '')) 
#Determines how  many columns the game board will have
columns= eval(input('Enter the columns that you want: (1-9)' '')) 
#Determines what takes place between the spaces of the board
board = [['  ']*rows for i in range(columns)] 
#game_piece = [rows] [columns]

a = rows + 1
b = columns + 1

#WHAT IN THE HELL IS THIS CODE DOING AND WHY IS IT NOT IN A METHOD???
randrows = random.randrange (1, a)
randcolumns = random.randrange (1, b)
randcolumns != columns
randrows != rows

#GLOBAL VARIABLES GO ABOVE YOUR CODE MESS
count_x = 0
count_o = 0
#WHAT IS valid_moves. IT ISN't USED ONCE.
valid_moves = []

#WE NEED TO WORK ON THIS METHOD 
#NEEDS TO RUN OVER AND OVER AGAIN UNTIL THE GAME IS OVER
def start_game():
	#game_over = FALSE
	#while(not game_over):
    game_board()
    human_turn(board, count_o, 'O')
    adjacent(columns, rows)
    game_board()
    machine_turn(board, randrows, randcolumns, 'X')
    adjacent(columns, rows)
    game_board()
	#if(find_available_moves() or win_condition()):
		#game_over = TRUE
    
    

def game_board():    #Function defines the dimensions and display the game board
    temp = 1
    print('  ', end='')
	#MAYBE CALL NR CURRENT ROW OR ROW NUMBER INSTEAD?
    for nr in range(rows):    #number of rows
       print(nr +1, end='  ' )
    print()
	#ITEM SHOULD BE SOME FORM OF ROW
    for item in board:
        print('  ', end='')
	#T NEEDS TO BE RENAMED
        for t in item:    #t is for top
            print('+̶ ', end= '')
        print('+')
        #for nc in range(columns):  #number of columns
          #  print(nc + 1, end='')
        print(temp, end='')
	#NC IS BETTER THAN S, S MEANS NOTHING
        for s in item:    #s is  for side
            print('|',s,  end= '')
        print('|')
        temp = temp +1
    print()

	
#NOTE TO JAIME: WE USED PARAMETER O WHEN WE DIDN'T KNOW WHOSE TURN WE
#  WERE DOING, WE NO LONGER NEED PARAMETER O AS WE KNOW O IS ALWAYS 'O'. 

# NOTE TO SELF: FIND SPOT FOR adjacent IN human_turn AND machine_turn
def human_turn(board, count_o, O):  #Manages the placesing of stones
    columns = 0
    rows = 0
	#Determines player move coordinate
    rows = eval(input('Enter row of next move: '))  
	#Determines player move coordinates
    columns = eval(input('Enter column of next move: ')) 
    columns = columns - 1
    rows = rows - 1
    if board[rows] [columns] == 'X' or board[rows] [columns] =='O':
#RETURN FALSE IS PLACED HERE SO YOU CAN REDO THIS METHOD ON A FALSE 
#WITH AN ERROR MESSAGE FOR THE USER
        return False 
    else:
        board [columns] [rows] = O
        count_o += 1
        return True


def machine_turn(board, rows, columns, X):  # Manages the placing
#JAIME THIS METHOD SHOULD MANAGE THE RANDOM ASPECTS, 
#NOT JUST THE PLACING OF THE COMPUTERS STONE!!!
    count_x = 0
    columns = columns - 1  #why is this code here?
    rows = rows - 1
    if board[rows] [columns] == 'X' or board[rows] [columns] =='O':
        return False
    else:
        board [rows] [columns] = X
        count_x = count_x +1
        return True
    



#Make a function that detects when no more moves are available on the board otherwise
#there will be an infinite loop
def find_available_moves():

#PLEASE MAKE A BETTER NAME THAN q WE ARE NOT IN PHYSICS, WE DON'T NEED MULTIPLE q's
    q =False
    while not q:
        randrows = random.randrange (1, a)
        randcolumns = random.randrange (1, b)
        q=machine_turn(board, randrows, randcolumns, 'X')
#SUGGESTION: MAYBE DO AN IF STATEMENT 
#if(q):
#   q = adjacent(columns, rows)
        adjacent(columns, rows)
        
 

#returns True if no spots left, otherwise return False
def all_spots_chosen():
#THIS METHOD FINDS SPOT [0,0] AND RETURNS TRUE OR FALSE
#THIS METHOD SHOULD BY YOUR DESCRIPTION LOOK THOUGH THE WHOLE 
#BOARD AND RETURN TRUE IF ALL SPOTS ARE X AND O
# AND IT SHOULD RETURN FALSE IF IT FINDS A SINGLE ' '
    for rows in board:
        for columns in board:
            if board[rows] [columns] == 'X' or board[rows] [columns] =='O':
                return False
            else:
                return True

#Makes sures stones can only be placed adjacent to other stones
def adjacent(columns, rows):
#WHY DID YOU REVERT TO A DOUBLE FOR LOOP?
#NO SERIOUSLY I'M VERY CURRIOUS, WHAT DO YOU PLAN TO DO WITH IT?
#AND WHATS SO GREAT ABOUT GOING OUT OF BOUNDS OVER AND OVER AGAIN?    
    for rows in board:
        for columns in board:
		
#WHAT IN THE BLOODY HELL ARE YOU TRYING TO DO? 
#TRY CATCH AND EXCEPT ARE SECOND YEAR CONCEPTS, DON'T USE THEM!!!
#THEY ARE THERE TO CATCH AN ERROR YOU EXPECT AND RUN A CODE BLOCK

# I AM MAD BECAUSE YOU ARE USING THIS 
# B-E-C-A-U-S-E  Y-O-U  A-R-E  E-X-S-P-E-C-T-I-N-G  F-A-I-L-U-E
# NOT BECAUSE YOU ARE PLANNING FOR EVERY POSIBILITY.
            try:
                (board[rows+1] [columns] == 'X' or
                 board[rows-1] [columns] == 'X' or
                 board[rows] [columns+1] == 'X' or
                 board[rows] [columns-1] == 'X' or
                 board[rows+1] [columns+1] == 'X' or
                 board[rows-1] [columns-1] =='X' or
                 board[rows+1] [columns] =='O' or
                 board[rows-1] [columns] == 'O' or
                 board[rows] [columns+1] == 'O' or
                 board[rows] [columns-1] == 'O' or
                 board[rows+1] [columns+1] == 'O' or
                 board[rows-1] [columns-1] == 'O')
            except:
                 print('Oops')
                          

#machine_turn(board, randrows, randcolumns, 'X')
#game_board()
start_game()
