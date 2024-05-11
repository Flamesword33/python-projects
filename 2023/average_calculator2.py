import random

def roll_average(num_of_dice=1, dice_type=6, test_pool=1000000):
    average = 0
    total = 0
    for x in range(0, test_pool):
        total = total + roll(num_of_dice, dice_type)
    average = total/test_pool
    return average

def roll_mod_average(num_of_dice=1, dice_type=6, mod=0, test_pool=1000000):
    average = 0
    total = 0
    for x in range(0, test_pool):
        total = total + roll_mod(num_of_dice, dice_type, mod)
    average = total/test_pool
    return average

def roll_dis_average(dice_type=6, test_pool=1000000):
    average = 0
    total = 0
    for x in range(0, test_pool):
        total = total + disadvantage(dice_type)
    average = total/test_pool
    return average

def roll_adv_average(dice_type=6, test_pool=1000000):
    average = 0
    total = 0
    for x in range(0, test_pool):
        total = total + advantage(dice_type)
    average = total/test_pool
    return average

def drop_lowest_average(dice_type=6, test_pool=1000000):
    average = 0
    total = 0
    for x in range(0, test_pool):
        r1 = roll(1, dice_type)
        r2 = roll(1, dice_type)
        r3 = roll(1, dice_type)
        r4 = roll(1, dice_type)
        total = total + drop_lowest(r1,r2,r3,r4)
    average = total/test_pool
    return average

def roll_mod(how_many = 1, face_count = 6, modifiyer=0):
    return roll(how_many, face_count) + modifiyer
    

def roll(how_many = 1, face_count = 6):
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

def advantage(face_count):
    num1 = roll(1, face_count)
    num2 = roll(1, face_count)
    return max(num1, num2)

def disadvantage(face_count):
    num1 = roll(1, face_count)
    num2 = roll(1, face_count)
    return min(num1, num2)

def drop_lowest(x1=0, x2=0, x3=0, x4=0):
    total = x1+x2+x3+x4
    minimum = min(x1,x2,x3,x4)
    return total - minimum

def stat():
    return drop_lowest(roll(), roll(), roll(), roll())

def stats():
    for i in range(6):
        print(stat())
