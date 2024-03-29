#percent_chance_to_roll.py
#by Nathan Pelletier
#started December 21

#This is to help with mass combat rolls (seriously 10+ rolls makes any table top game slow)
#I expect each roll to have a 1/20 chance to come up so I expect the final formula to be 
#   number_of_rolls * 1/20 * (20 + attack modifier - AC)/100
#   number_of_rolls *(20 + attack modifier - AC)/2000

#   Yup key result was what I expected although with less rolls the average for each became more sparatic 


import random

def main():
    percent_roll()
    

def roll(how_many = 1, face_count = 20):
    total = 0
    for x in range(0, how_many):
        total = total + random.randint(1, face_count)
    return total

def multi_roll(how_many = 1, face_count = 20, modifiyer = 0,num_to_beat = 10):
    counter = 0
    fails = 0
    crits = 0
    for x in range(1, how_many):
        c_roll = roll(1,face_count) + modifiyer
        if c_roll >= num_to_beat:
            counter = counter + 1
        if c_roll == modifiyer + 1:
            fails = fails + 1
        if c_roll == modifiyer + face_count:
            crits = crits + 1
            
    print(counter, " hits")
    print(fails, " fails")
    print(crits, " crits")

def percent_roll(number_of_rolls = 10000):
    # Remember roll is offset starting its index at 0-19
    #             1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    roll_tally = [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    current_roll = 0
    for i in range(number_of_rolls):
        current_roll = roll(1, 20)
        #2 ways to proceed, simply enter if statement for each number from 1 to 20... im an idot
        roll_tally[current_roll-1] = roll_tally[current_roll-1] + 1
    
    for x in range(len(roll_tally)):
        roll_tally[x] = roll_tally[x]/number_of_rolls
        print (roll_tally[x])
    
    return roll_tally

main()