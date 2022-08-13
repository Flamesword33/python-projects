##project goals:
##November 3, 2015
##  create a dictionary that uses words as keys
##  subcatigorize occurance locations
##  reject less than 3 letter letters

## Reasurch :
## str to list
## list to dictionary 

## NOT YET!!!
##  bonus: only one pass over text_file
##  all words should be lower case
##  bonus: accepts symbols and numbers


my_file = open('hump.txt','r')
def indexMarker(text_file):
    '''Creates a dictionary that sorts and returns all words bigger than 3
        letters in length with their corisponding lines of occurance.'''
    words = text_file.read()
    
    print(words)
    
    word_count = {}






indexMarker(my_file)

my_file.close()
