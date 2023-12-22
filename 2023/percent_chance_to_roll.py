
import random

def main():
    

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

main()