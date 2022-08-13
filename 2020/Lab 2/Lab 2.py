## Lab2.py
## 
## by Nathan Pelletier
## Started: Febuary 8, 2020
## Published: Febuary 10, 2020
##
## to do list:
##   create initial function call --> Febuary 8 DONE
##   create overarching game structure
##     should print state and return true if game is done --> Febuary 8 structure created
##     or if recursive call returns true --> Febuary 8 structure created
##     should return false upon finding nothing --> Febuary 8 structure created
##     or failing to be a valid game --> Febuary 8 structure created
##   create all actions AI can take 
##     on the left side --> Febuary 8 Needs testing
##     on the right side --> Febuary 8 Needs testing
##   check that the game is valid 
##     is timer up? --> Febuary 10 DONE
##     is something negitive? --> Febuary 10 DONE
##     are there more cannibles than missionaries? --> Febuary 10 DONE
##     REMEBER TO CHECK
##       missionaries == 0 first --> Febuary 10 DONE
##   check if game is won
##     should only accept (0,0,3,3,True) --> Febuary 9 DONE
##   recursivly print out game states --> Febuary 10 DONE
##   Testing --> Febuary 10 --> DONE

def start(missionaries_left = 3, cannibles_left = 3,
          missionaries_right = 0, cannibles_right = 0,
          is_boat_right = False, turns_left = 15):
  """Starts the missionary and cannible problem with either your base values or :

  my data   data type       what it represents
       3            int          missionaries on the left
       3            int          cannibles on the left
       0            int          missionaries on the right
       0            int          cannibles on the right
       False      boolean  is the boat on the right?
       15           int          turns to find an answer

       WARNING, will never succeed if the number of cannibles != 3
          or if the number of missionaries != 3"""

  if initial_game_valid(missionaries_left, cannibles_left,
                 missionaries_right, cannibles_right,
                 turns_left):

    game_structure(missionaries_left, cannibles_left,
                   missionaries_right, cannibles_right,
                   is_boat_right, turns_left)
#end fuction start


def initial_game_valid(missionaries_left, cannibles_left,
                 missionaries_right, cannibles_right,
                  turns_left):
  """initial_game_valid(int, int, int, int, int) --> boolean

      Ensures that initial state of the game contains:
        3 missionaries
        3 cannibles
        turns to win"""

  if ((missionaries_left + missionaries_right) == 3
      and (cannibles_left + cannibles_right) == 3
      and turns_left > 0):
    return True
  #end if values will result in a result
#end function initial_game_valid


def game_structure(missionaries_left, cannibles_left,
                   missionaries_right, cannibles_right,
                   is_boat_right, turns_left):
  """game_structue(int, int, int, int, boolean, int) --> boolean

      checks if game state is still valid
      checks if game has been won
      if not then recusivly calls itself five times using all posible actions avalible
      prints out current parameters upon recursive calls comming back true
      returns true on successful completion and false on failure"""
  
  if game_valid(missionaries_left, cannibles_left,
                missionaries_right, cannibles_right,
                turns_left):

    if game_won(missionaries_left, cannibles_left,
                missionaries_right, cannibles_right,
                is_boat_right):
      print_final_win(missionaries_left, cannibles_left,
                      missionaries_right, cannibles_right,
                      is_boat_right, turns_left)
      return True
    #end if game won

    else:

      if is_boat_right:
        if boat_is_right_recursion(missionaries_left, cannibles_left,
                                   missionaries_right, cannibles_right,
                                   turns_left):
          print_game_win(missionaries_left, cannibles_left,
                         missionaries_right, cannibles_right,
                         is_boat_right, turns_left)
          return True
        #end if (this looks to see if the game has been won in a future state and prints out this local state)
      else:
        if boat_is_left_recursion(missionaries_left, cannibles_left,
                                  missionaries_right, cannibles_right,
                                  turns_left):
          print_game_win(missionaries_left, cannibles_left,
                         missionaries_right, cannibles_right,
                         is_boat_right, turns_left)
          return True
        #end if (this looks to see if the game has been won in a future state and prints out this local state)

        return False ##edge case where nothing true is found

      #end else game is not won

  else:
    return False
  #end else game is invalid
#end function game_structure

      
def game_valid(missionaries_left, cannibles_left,
                missionaries_right, cannibles_right,
                turns_left):
  """game_valid(int, int, int, int, int) --> boolean

       checks:
         if cannibles outnumber missionaries on either side
           ignores edge case where there are 0 missionaries
        for invalid entries
          negitive numbers
          zero turns left"""

  if missionaries_left < cannibles_left and missionaries_left > 0:
    return False
  #end if missionaries on the left side are outnumbered

  if missionaries_right < cannibles_right and missionaries_right > 0:
    return False
  #end if missionaries on the right side are outnumbered

  if (missionaries_left < 0 or cannibles_left < 0
      or missionaries_right < 0 or cannibles_right < 0
      or turns_left == 0):
    return False
  #end if any varible is negitive or if out of turns

  return True #all varibles are correct, game can continue

#end function game_valid


def game_won(missionaries_left, cannibles_left,
                missionaries_right, cannibles_right,
                is_boat_right):
  """game_won(int, int, int, int, boolean) --> boolean

       checks if game state is:
       3 missionaries right
       3 cannibles right
       boat is right

       If all are correct then it returns true
       I inverted all statements to reduce the number of checks on a bad state"""
  
  if missionaries_left != 0 or cannibles_left != 0:
    return False
  elif missionaries_right != 3 or cannibles_right != 3:
    return False
  elif is_boat_right == False:
    return False
  else:
    return True
#end fuction game_won

  
def boat_is_right_recursion(missionaries_left, cannibles_left,
                            missionaries_right, cannibles_right,
                            turns_left):
  """boat_is_right_recursion(int, int, int, int, int) --> boolean

       goes through the five states the game can be in if the boat is right
       returns true if a winning state was found further down"""
  
  if game_structure(missionaries_left + 1, cannibles_left,
                    missionaries_right - 1, cannibles_right,
                    False, turns_left - 1):
    return True
  #end if one missionary goes left with boat

  if game_structure(missionaries_left, cannibles_left + 1,
                    missionaries_right, cannibles_right - 1,
                    False, turns_left - 1):
    return True
  #end if one cannible goes left with boat

  if game_structure(missionaries_left + 2, cannibles_left,
                    missionaries_right - 2, cannibles_right,
                    False, turns_left - 1):
    return True
  #end if two missionaries go left with boat

  if game_structure(missionaries_left, cannibles_left + 2,
                    missionaries_right, cannibles_right - 2,
                    False, turns_left - 1):
    return True
  #end if two cannibles go left with boat

  if game_structure(missionaries_left + 1, cannibles_left + 1,
                    missionaries_right - 1, cannibles_right - 1,
                    False, turns_left - 1):
    return True
  #end if one missionary and one cannible go left with boat

  return False ##edge case where nothing is found
  
#end fuction boat_is_right_recursion


def boat_is_left_recursion(missionaries_left, cannibles_left,
                           missionaries_right, cannibles_right,
                           turns_left):
  """boat_is_left_recursion(int, int, int, int, int) --> boolean

       goes through the five states the game can be in if the boat is left
       returns true if a winning state was found further down"""
  
  if game_structure(missionaries_left - 1, cannibles_left,
                    missionaries_right + 1, cannibles_right,
                    True, turns_left - 1):
    return True
  #end if one missionary goes right with boat

  if game_structure(missionaries_left, cannibles_left - 1,
                    missionaries_right, cannibles_right + 1,
                    True, turns_left - 1):
    return True
  #end if one cannible goes right with boat

  if game_structure(missionaries_left - 2, cannibles_left,
                    missionaries_right + 2, cannibles_right,
                    True, turns_left - 1):
    return True
  #end if two missionaries go right with boat

  if game_structure(missionaries_left, cannibles_left - 2,
                    missionaries_right, cannibles_right + 2,
                    True, turns_left - 1):
    return True
  #end if two cannibles go right with boat

  if game_structure(missionaries_left - 1, cannibles_left - 1,
                    missionaries_right + 1, cannibles_right + 1,
                    True, turns_left - 1):
    return True
  #end if one missionary and one cannible go right with boat

  return False ##edge case where nothing is found

#end fuction boat_is_right_recursion


def print_final_win(missionaries_left, cannibles_left,
                      missionaries_right, cannibles_right,
                      is_boat_right, turns_left):
  
  print("Goal state achieved")
  print_game_win(missionaries_left, cannibles_left,
                         missionaries_right, cannibles_right,
                         is_boat_right, turns_left)
#end fuction print_final_win


def print_game_win(missionaries_left, cannibles_left,
                         missionaries_right, cannibles_right,
                         is_boat_right, turns_left):

  if is_boat_right:
    print ('(', missionaries_left, ",", cannibles_left, ", 0 ,", missionaries_right, ",", cannibles_right, ", 1)")
  else:
    print ('(', missionaries_left, ",", cannibles_left, ", 1 ,", missionaries_right, ",", cannibles_right, ", 0)")

  print(turns_left, " remaining turns")

#end fuction print_game_win
