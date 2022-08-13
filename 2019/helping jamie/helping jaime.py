def board():      #Function defines the dimensions and display the game board
    for item in board:
        for t in item:    #t is for top
            print('+̶ ', end= '')
        print('+')
        for s in item:    #s is  for side
            print('|',s,  end= '')
        print('|')
	print()
        


rows= eval(input('Enter the rows that you want: (1-9)' ''))  #Determines how many rows the game board will have
columns= eval(input('Enter the columns that you want: (1-9)' '')) #Determines how  many columns the game board will have
board = [['  ']*rows for i in range(columns)] #Determines what takes place between the spaces of the board

board() 

def place_stone(board, columns, rows,XorO):
    board [columns] [rows] = XorO

place_stone(board, 1,1,'X')
board()