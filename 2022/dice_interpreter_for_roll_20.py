##dice_interpreter_for_roll_20
##by Nathan Pelletier
##June 2022

##This quickly hacked out code was done to save on typing in roll 20
##Takes a large pool of dice rolls and turns them into seperate rolls
##  (Seems useless until you need to put a different modifier on each dice rolled) 

def main():
    dice = input("Dice to roll on roll 20: ")
    data = dice.split(sep="d")
    print()
    for x in range(int(data[0])):
        print("/r d", end='')
        print( data[1])

main()
