## lab4.py
##
## AUCSC 490
## by Nathan Pelletier
## Started: Febuary 23
## Published:

## Solves tile problem
## In this problem you have one tile that is blank and
## 8 tiles that must be moved into position, only the empty tile can be moved.
##
## Final board postion:
## 1 2 3
## 4 5 6
## 7 8 _
## 

## This program uses simulated annealing
## to solve the problem.
## simulated annealing works by
## using the hill climbing algorithm to find
## a local maximum in combination with
## a statistics function makes bad moves every now and
## then to attempt to keep the function from getting stuck
## in local maximums.

## work plan:
##   basic game rules
##     move 0 up
##     move 0 left
##     move 0 right
##     move 0 down
##     check for wall boundaries
##   check for win condition
##     1 2 3
##     4 5 6
##     7 8
##
##     use manhattan distance to find closeness to goal
##     should be a negitive and machine should look for a positive goal
##   set up
##     random chance to make a bad move
##     should print out bad move upon making one
##   print out the game
##     print out score based on mannhatten distance
##     print a win

## Big Errors:
##   While testing class I found that print_mannhattan_distance
##   did not exist until I removed the class.

import math
import random
import copy


## connective structure of block puzzle and ai
## It attempts a move
##   the move may or may not be made based on if it is better
##   or worse depending on a random call
## It checks if the goal state was achieved
## It reduces the random variable
## It prints out the game
def start(initial_game = ([1,2,3],[4,5,8],[6,7,0])):
  """start(int[][]) --> boolean"""

  is_game_over = False
  chance_of_bad_move = 40

  for x in range(50):
    current_game = attempt_a_move(initial_game, chance_of_bad_move)
    if current_game != initial_game:
      print_my_game(current_game)
      initial_game = current_game
      
      is_game_over = is_game_won(current_game)
      if is_game_over == True:
        print("GOAL")
        return True
      #end if game is over
    #end if
    chance_of_bad_move = chance_of_bad_move - 1
    print("move", end = ' ')
    print(x)
  #end for
  print("Local maximum reached")
  return True
#end start


def attempt_a_move(current_game,bad_move_chance):
  """attempt_a_move(int[][],int) --> int[][]"""

  current_score = mannhattan_distance(current_game)
  zero_position = find_zero(current_game)

  if (zero_position == [0,0]
      or zero_position == [0,2]
      or zero_position == [2,0]
      or zero_position == [2,2]):
    return corner_move(current_game,bad_move_chance, current_score, zero_position)
  #end if
  elif zero_position == [1,1]:
    return middle_move(current_game,bad_move_chance,current_score)
  #end elif
  else:
    return wall_move(current_game,bad_move_chance,current_score,zero_position)
  #end else
#end attempt_a_move


def find_zero(game):
  for x in range(len(game)):
    for y in range(len(game[x])):
      if game[x][y] == 0:
        temp = [x,y]
        return temp
      #end if
    #end for
  #end for
#end find_zero


def corner_move(current_game,bad_move_chance, current_score, zero_position):
  """corner_move(int[][],int,int,int)-->int[][]"""
  if zero_position == [0,0]:
    return top_left_corner(current_game,bad_move_chance, current_score)
  elif zero_position == [0,2]:
    return top_right_corner(current_game,bad_move_chance, current_score)
  elif zero_position == [2,0]:
    return bottom_left_corner(current_game,bad_move_chance, current_score)
  else:
    return bottom_right_corner(current_game,bad_move_chance, current_score)
#end corner_move


def top_left_corner(current_game,bad_move_chance, current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  
  game_1 = move_down(game_1, ([0,0]))
  game_2 = move_right(game_2, ([0,0]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  return current_game
#end top_left_corner


def top_right_corner(current_game,bad_move_chance, current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  
  game_1 = move_left(game_1, ([0,2]))
  game_2 = move_down(game_2, ([0,2]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  return current_game
#end top_right_corner


def bottom_left_corner(current_game,bad_move_chance, current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  
  game_1 = move_right(game_1, ([2,0]))
  game_2 = move_up(game_2, ([2,0]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  return current_game
#end bottom_left_corner


def bottom_right_corner(current_game,bad_move_chance, current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  
  game_1 = move_up(game_1, ([2,2]))
  game_2 = move_left(game_2, ([2,2]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  return current_game
#end bottom_right_corner


def middle_move(current_game, bad_move_chance,current_score):
  """middle_move(int[][],int,int) --> int[][]"""
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  game_3 = copy.deepcopy(current_game)
  game_4 = copy.deepcopy(current_game)
  
  game_1 = move_up(game_1, ([1,1]))
  game_2 = move_left(game_2, ([1,1]))
  game_3 = move_right(game_3, ([1,1]))
  game_4 = move_down(game_4, ([1,1]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)
  score_3 = mannhattan_distance(game_3)
  score_4 = mannhattan_distance(game_4)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  if(score_3 > current_score
   or should_make_bad_move(score_3 - current_score,bad_move_chance)):
    return game_3
  if(score_4 > current_score
   or should_make_bad_move(score_4 - current_score,bad_move_chance)):
    return game_4
  return current_game
#end middle_move


def wall_move(current_game,bad_move_chance,current_score,zero_position):
  if zero_position[1] == 0:
    return left_wall(current_game,bad_move_chance,current_score)
  elif zero_position[1] == 2:
    return right_wall(current_game,bad_move_chance,current_score)
  elif zero_position[0] == 0:
    return top_wall(current_game,bad_move_chance,current_score)
  else:
    return bottom_wall(current_game,bad_move_chance,current_score)
#end wall_move


def left_wall(current_game,bad_move_chance,current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  game_3 = copy.deepcopy(current_game)
  
  game_1 = move_down(game_1, ([1,0]))
  game_2 = move_right(game_2, ([1,0]))
  game_3 = move_up(game_3, ([1,0]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)
  score_3 = mannhattan_distance(game_3)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  if(score_3 > current_score
   or should_make_bad_move(score_3 - current_score,bad_move_chance)):
    return game_3
  return current_game
#end left_wall


def right_wall(current_game,bad_move_chance,current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  game_3 = copy.deepcopy(current_game)
  
  game_1 = move_up(game_1, ([1,2]))
  game_2 = move_left(game_2, ([1,2]))
  game_3 = move_down(game_3, ([1,2]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)
  score_3 = mannhattan_distance(game_3)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  if(score_3 > current_score
   or should_make_bad_move(score_3 - current_score,bad_move_chance)):
    return game_3
  return current_game
#end right_wall


def top_wall(current_game,bad_move_chance,current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  game_3 = copy.deepcopy(current_game)
  
  game_1 = move_left(game_1, ([0,1]))
  game_2 = move_down(game_2, ([0,1]))
  game_3 = move_right(game_3, ([0,1]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)
  score_3 = mannhattan_distance(game_3)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score,bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  if(score_3 > current_score
   or should_make_bad_move(score_3 - current_score,bad_move_chance)):
    return game_3
  return current_game
#end top_wall


def bottom_wall(current_game,bad_move_chance,current_score):
  game_1 = copy.deepcopy(current_game)
  game_2 = copy.deepcopy(current_game)
  game_3 = copy.deepcopy(current_game)

  game_1 = move_right(game_1, ([2,1]))
  game_2 = move_up(game_2, ([2,1]))
  game_3 = move_left(game_3, ([2,1]))

  score_1 = mannhattan_distance(game_1)
  score_2 = mannhattan_distance(game_2)
  score_3 = mannhattan_distance(game_3)

  if(score_1 > current_score
     or should_make_bad_move(score_1 - current_score, bad_move_chance)):
    return game_1
  if(score_2 > current_score
   or should_make_bad_move(score_2 - current_score,bad_move_chance)):
    return game_2
  if(score_3 > current_score
   or should_make_bad_move(score_3 - current_score,bad_move_chance)):
    return game_3
  return current_game


def move_up(game, zero_position):
  x = zero_position[1]
  y = zero_position[0]
  temp = game[y - 1][x]
  game[y-1][x] = 0
  game[y][x] = temp
  return game


def move_left(game, zero_position):
  x = zero_position[1]
  y = zero_position[0]
  temp = game[y][x-1]
  game[y][x-1] = 0
  game[y][x] = temp
  return game


def move_right(game, zero_position):
  x = zero_position[1]
  y = zero_position[0]
  temp = game[y][x+1]
  game[y][x+1] = 0
  game[y][x] = temp
  return game
  

def move_down(game, zero_position):
  x = zero_position[1]
  y = zero_position[0]
  temp = game[y + 1][x]
  game[y+1][x] = 0
  game[y][x] = temp
  return game


## uses formula e^(E/T)
## the above formula finds a chance between 100 and 30 %
## determines if a bad move should be made by generating a
## random number between 0 and 100
def should_make_bad_move(E,T):
  """should_make_bad_move(int) --> boolean"""
  if T < 1:
    return False
  probability = (math.exp(E/T) * 100)

  probability_2 = random.randint(0,100)

  if probability_2 <= probability:
    return True
  #end if number generated is less than projected chance

  else:
    return False
#end should_make_bad_move

  
##prints out a AxB matrix
## 0 becomes a space
def print_my_game(my_game):
  """print_my_game(int[][])"""
  
  for x in range(len(my_game)):
    for y in range(len(my_game[x])):

      if my_game[x][y] == 0:
        print(' ', end = ' ')
      #end if
        
      else:
        print(my_game[x][y], end = ' ')
      #end else
        
    print()
    #end for y
  #end for x
  print_mannhattan_distance(my_game)
#end print_my_game


def print_mannhattan_distance(my_game):
  """print_mannhattan_distance(int[][])"""
  board_score = mannhattan_distance(my_game)

  print("(score = ", end ='')
  print(board_score, end ='')
  print(')')
  print()
#end print_mannhattan_distance


def is_game_won(my_game):
  """is_game_won(int[][]) --> boolean"""
  if mannhattan_distance(my_game) == 0:
    return True
  else:
    return False
#end is_game_won


def mannhattan_distance(my_game):
  current_score = 0
  for x in range(len(my_game)):
    for y in range(len(my_game[x])):
      desired_state = switch (my_game[x][y])

      current_score = current_score + abs(desired_state[0] - x)
      current_score = current_score + abs(desired_state[1] - y)
      
    #end for vertical
  #end for horizontal

  return 0 - current_score
#end mannhattan_distance


## this is an improvised switch statement as
## python does not support switch
## takes a number and returns a position
## uses a dictionary
def switch(key):
  """switch(int)-->int[]"""
  
  desired_positions = {
    0 :[2,2],
    1 :[0,0],
    2 :[0,1],
    3 :[0,2],
    4 :[1,0],
    5 :[1,1],
    6 :[1,2],
    7 :[2,0],
    8 :[2,1]
    }

  return desired_positions[key]
#end switch
