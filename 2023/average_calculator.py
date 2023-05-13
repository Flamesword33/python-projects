#average_calculator.py
#by Nathan Pelletier
#May 13 2023

#simple function, takes 2 numbers and brute forces the average
#take a sample of 10 000 random samples of the same roll and averages them

import random

def average_num(number_of_rolls:int, number_to_roll:int):
    result = 0
    for x in range(10000):
        #print('Roll number '+ str(x) +':', end='')
        result = roll(number_of_rolls, number_to_roll) + result
    return result/10000

def roll(number_of_rolls, number_to_roll):
    current_num = 0
    result = 0
    for x in range(number_of_rolls):
        current_num = random.randint(1, number_to_roll)
        result = current_num + result
        #print(str(current_num) + ', ', end='')
    #print('= ' + str(result))
    return result

def advantage_average(number_to_roll:int):
    num1 = 0
    num2 = 0
    result = 0
    for x in range(10000):
        #print('Roll number '+ str(x) +':', end='')
        num1 = roll(1, number_to_roll)
        num2 = roll(1, number_to_roll)
        result = greater(num1, num2) + result
    return result/10000

def greater(x, y):
    if x >= y:
        return x
    else:
        return y


def disadvantage_average(number_to_roll:int):
    num1 = 0
    num2 = 0
    result = 0
    for x in range(10000):
        #print('Roll number '+ str(x) +':', end='')
        num1 = roll(1, number_to_roll)
        num2 = roll(1, number_to_roll)
        result = lesser(num1, num2) + result
    return result/10000

def lesser(x, y):
    if x <= y:
        return x
    else:
        return y
    
        
random.seed()
