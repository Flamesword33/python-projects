##testaverageroll.py
##by Nathan Pelletier
##July 7 2022

##Was hacked out to test the law of averages given different rolls
##Outputs each potential result and its percent chance
##Tested 4d6 drop the lowest, 3d6, 2d20 take the higher number

from random import randint

def test_dice():
  total = 0
  roll = 0
  rolled = []
  for x in range(1000000):
    ###########################################################
    ## THIS IS THE LINE TO CHANGE WHEN TESTING DIFFERENT DICE
    roll = roll_advantage_d20()
    ###########################################################
    total = roll + total
    rolled.append(roll)
  #for
    
  output_results(total, rolled)
#main

def output_results(total, rolled):
  print("Average roll: ", end='')
  print(total/1000000)

  for y in range(min(rolled), max(rolled) + 1):
    print("Percentage rolled ", end='')
    print(y, end='')
    print(": ", end='')
    print(rolled.count(y)/10000)
  #for
#results

def roll_4d6():
  lowest = 7
  total = 0
  
  for x in range(4):
    roll = randint(1,6)
    if roll < lowest:
      lowest = roll
    #if
      
    total = total + roll
  #for
    
  total = total - lowest
  return total
#roll_4d6

def roll_3d6():
  total = 0
  
  for x in range(3):
    total = randint(1,6) + total
  #for
  
  return total
#roll_3d6

def roll_advantage_d20():
  roll1 = randint(1,20)
  roll2 = randint(1,20)

  if roll1 > roll2:
    return roll1
  else:
    return roll2
  
#roll_advantage_d20


test_dice()
