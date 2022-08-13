##Number of asterisks and Fancy Grid
##by Nathan Pelletier
##creates a function that counts the number of asterisks in a peice of text
##
##ex
##numAsterisks('*a*')
##2
##numAsterisks('a')
##0
def numAsterisks(aWord):
    'counts the number of asteriks present'
    # i am using count to set up a base to add to 
    count=0
    for asterisk in range(0,(len(aWord))):
        
        #for each letter and symbol the program looks through if it finds
        # a * it will add 1 to count and after it is finished it will print
        #count
        if aWord[asterisk] == '*':
            #it should take asterisk which is counting from 0 to the full
            #length of the word and then impliment it to find the spcific
            # letters in the string which match *
             count = count + 1
    
    print(count)
   
    

##creates a grid of given size. the size determines how many rows to print
## the row determines how many underscores are present
## current state will only produce one per row
##eg
##aFancyGrid(6)
##******
##******_
##******__
##******___
##******____
##******_____
##
## i want
##aFancyGrid(6)
##******
##*_*_*_
##*__*__
##*___*_
##*____*
##*_____
def aFancyGrid(size):
    '''creates a grid based on specified size, grid consists of
    size* rows and size * colum legnth and size * number of
    underscores'''
    #i am creating a variable to divide * by the row number
    row = size
    for i in range(0,size+1):
        #error=1/(i+1)  I want it to repeat the sequence and i want it to
        #stop when the sequence hits the variable for size
        print ('_'*i)
        for j in range(0,size+1):
            inverse=row/(i+1)
            #i can't seem to convert row into an intiger to work with
            #if i could i would multiply it to '*' to make star repeat
            # eg 6 times, than 3 times, 2 times, 2 times, 1 time, 1 time
            print ('*',end='')
            
            
    
