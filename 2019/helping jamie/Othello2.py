#Othello.py
#Jamie Plant
#Date Finished December 8, 2018

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


count_x = 0
count_o = 0
valid_rows = []
valid_columns = []
randrows = random.randrange (0, rows)
randcolumns = random.randrange (0, columns)

def start_game():
        print('You are playing a game of Othello (Reversi) against a Computer Player')
        print('The game ends when all available moves are taken')
        print('Please input the size of the game board you wish to play on')
        game_over = False
        while (not game_over):
                game_board()
                human_turn(board, count_o)
                game_board()
                flip(board, columns, rows)
                game_board()
                if(all_spots_chosen(board, rows, columns)):
                        game_over = True
                machine_turn(board,randcolumns + 1, randrows + 1, count_x)
                flip(board, columns, rows)
                game_board()
                if(all_spots_chosen(board, rows, columns)):
                        game_over = True
        if count_o > count_x:
                print('Human Player Wins')
        if count_x > count_o:
                print('Computer Player Wins')
        if count_x == count_o:
                print('Human Player and Computer Player tie')
        print(count_o)
        print(count_x)


def game_board():    #Function defines the dimensions and display the game board
        temp = 1
        print('  ', end='')
        for row_number in range(rows):
                print(row_number +1, end='  ' )
        print()
        for column in board:
                print('  ', end='')
                for celing in column:
                        print('+- ', end= '')
                print(' ')
                print(temp, end='')
                for column_number in column:
                        print('|',column_number,  end= '')
                print('|')
                temp = temp +1
        print()


def human_turn(board, count_o):  #Manages the placing of stones for human player
        columns = 0
        rows = 0
#Determines player move coordinate
        rows = eval(input('Enter row of next move: '))
#Determines player move coordinates
        columns = eval(input('Enter column of next move: '))
        columns = columns - 1
        rows = rows - 1
        if board[rows] [columns] == 'X' or board[rows] [columns] =='O':
                return False
        else:
                board [columns] [rows] = 'O'
                count_o += 1
                return True


def machine_turn(board, randcolumns, randrows, count_x):  # Manages the placing of stones for computer player
        if board[randrows] [randcolumns] == 'X' or board[rows] [columns] == 'O':
                return False
        else:
                if adjacent(randrows, randcolumns):
                        board [randrows] [randcolumns] = 'X'
                        count_x = count_x +1
                        return True
        return False


#returns True if no spots left, otherwise return False
def all_spots_chosen(board, rows, columns):
        for vertical in range(rows):
                for horizontal in range(columns):
                        if board[vertical][horizontal] != 'X' and board[vertical][horizontal] !='O':
                                return False
        return True


#Makes sures stones can only be placed adjacent to other stones
def adjacent(horizontal, vertical):
        if vertical== 0 and horizontal == 0:
                if(board[horizontal+1] [vertical] == 'X' or
                   board[horizontal+1] [vertical+1] == 'X' or
                   board[horizontal] [vertical+1] == 'X' or
                   board[horizontal+1] [vertical] =='O' or
                   board[horizontal] [vertical+1] == 'O' or
                   board[horizontal+1] [vertical+1] == 'O'):
                        return True
                else:
                        return Flase
        if vertical == 0 and horizontal == rows:
                if(board[horizontal-1] [vertical] == 'X' or
                   board[horizontal] [vertical+1] == 'X' or
                   board[horizontal-1] [vertical+1] == 'X' or
                   board[horizontal-1] [vertical] =='O' or
                   board[horizontal] [vertical+1] == 'O' or
                   board[horizontal-1] [vertical+1]== 'O'):
                        return True
                else:
                        return False
        if vertical == columns and horizontal == rows:
                if(board[horizontal-1] [vertical] == 'X' or
                   board[horizontal] [vertical-1] == 'X' or
                   board[horizontal-1] [vertical-1] =='X' or
                   board[horizontal-1] [vertical] == 'O' or
                   board[horizontal] [verical-1] == 'O' or
                   board[horizontal-1] [vertical-1] == 'O'):
                        return True
                else:
                        return False
        if vertical == columns and horizontal == 0 :     #corners
                if(board[horizontal+1] [vertical] == 'X' or
                   board[horizontal] [vertical-1] == 'X' or
                   board[horizontal+1] [vertical-1] == 'X' or
                   board[horizontal+1] [vertical] =='O' or
                   board[horizontal] [verical-1] == 'O' or
                   board[horizontal+1] [vertical-1] == 'O'):
                        return True
                else:
                        return False
        if vertical == 0:
                if(board[horizontal+1] [vertical] == 'X' or
                   board[horizontal+1] [vertical+1] == 'X' or
                   board[horizontal-1] [vertical+1] == 'X' or
                   board[horizontal] [vertical+1] == 'O' or
                   board[horizontal+1] [vertical+1] == 'O' or
                   board[horizontal-1] [vertical+1] == 'O'):
                        return True
                else:
                        return False
        if vertical == columns:         #top
                if(board[horizontal-1] [vertical] == 'X' or
                   board[horizontal-1] [vertical-1] =='X' or
                   board[horizontal-1] [vertical+1] == 'X' or
                   board[horizontal-1] [vertical] == 'O' or
                   board[horizontal] [verical-1] == 'O' or
                   board[horizontal-1] [vertical-1] == 'O' or
                   board[horizontal-1] [vertical+1])== 'O':
                        return True
                else:
                        return False
        if horizontal == 0:
                if(board[horizontal+1] [vertical] == 'X' or
                   board[horizontal+1] [vertical+1] == 'X' or
                   board[horizontal+1] [vertical-1] == 'X' or
                   board[horizontal+1] [vertical] =='O' or
                   board[horizontal+1] [vertical+1] == 'O' or
                   board[horizontal+1] [vertical-1] == 'O'):
                        return True
                else:
                        return False
        if horizontal == rows:    #bottom
                if(board[horizontal] [vertical-1] == 'X' or
                   board[horizontal-1] [vertical-1] =='X' or
                   board[horizontal+1] [vertical-1] == 'X' or
                   board[horizontal] [verical-1] == 'O' or
                   board[horizontal-1] [vertical-1] == 'O' or
                   board[horizontal+1] [vertical-1] == 'O'):
                        return True
                else:
                        return False
        else:
                if(board[horizontal+1] [vertical] == 'X' or
                   board[horizontal-1] [vertical] == 'X' or
                   board[horizontal] [vertical+1] == 'X' or
                   board[horizontal] [vertical-1] == 'X' or
                   board[horizontal+1] [vertical+1] == 'X' or
                   board[horizontal-1] [vertical-1] =='X' or
                   board[horizontal+1] [vertical-1] == 'X' or
                   board[horizontal-1] [vertical+1] == 'X' or
                   board[horizontal+1] [vertical] =='O' or
                   board[horizontal-1] [vertical] == 'O' or
                   board[horizontal] [vertical+1] == 'O' or
                   board[horizontal] [vertical-1] == 'O' or
                   board[horizontal+1] [vertical+1] == 'O' or
                   board[horizontal-1] [vertical-1] == 'O' or
                   board[horizontal+1] [vertical-1] == 'O' or
                   board[horizontal-1] [vertical+1] =='O'):
                        return True
                else:
                        return False

def flip(board, columns, rows):
        for horizontal in range(columns):
                for vertical in range(rows):
                        if board[horizontal][vertical] == 'X' or board[horizontal][vertical] == 'O':
                                follow_horizontal(board, rows, columns, horizontal, vertical)
                                follow_vertical(board, rows, columns, horizontal, vertical)
                                follow_diagonal(board, rows, columns, horizontal, vertical)




def follow_horizontal(board, rows, columns, horizontal, vertical):
        counter=0
        while board[horizontal][vertical] == 'X' or board[horizontal][vertical] == 'O':
                counter = counter + 1
                horizontal = horizontal + 1
                if horizontal >= rows:
                        break
        horizontal = horizontal - 1
        if board[horizontal][vertical] == board[horizontal-counter][vertical]:
                final_step_h(board, rows, columns, horizontal, vertical, counter)


def final_step_h(board, rows, columns, horizontal, vertical, coutner):
        while counter > 0:
                horizontal = horizontal - 1
                board[horizontal][vertical] = board[horizontal+1][vertical]
                counter = counter - 1


def follow_vertical(board, rows, columns, horizontal, vertical):
        counter = 0
        while board[horizontal][vertical] == 'X' or board[horizontal][vertical] == 'O':
                counter = counter + 1
                vertical =  vertical + 1
                if vertical >= columns:
                        break
        vertical = vertical - 1
        if board[horizontal][vertical] == board[horizontal][vertical-counter]:
                final_step_v(board, rows, columns, horizontal, vertical, counter)

def final_step_v(board, rows, columns, horizontal, vertical, counter):
        while counter > 0:
                vertical = vertical - 1
                board[horizontal][vertical] = board[horizontal][vertical+1]
                counter = counter - 1

def follow_diagonal(board, rows, columns, horizontal, vertical):
        counter = 0
        while board[horizontal][vertical] == 'X' or board[horizontal][vertical]:
                counter = counter + 1
                horizontal = horizontal + 1
                vertical = vertical + 1
                if horizontal >= rows or vertical >= columns:
                        break
        horizontal = horizontal - 1
        vertical = vertical - 1
        if board[horizontal][vertical] == board[horizontal-counter][vertical-counter]:
                final_step_d(board, rows, columns, horizontal, vertical, counter)

def final_step_d(board, rows, columns, horizontal, vertical, counter):
        while counter > 0:
                horizontal = horizontal - 1
                vertical = vertical - 1
                board[horizontal][vertical] = board[horizontal+1][vertical+1]
                counter = counter - 1

start_game()
