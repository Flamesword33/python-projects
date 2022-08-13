## The IDEXINAION.py
## by Nathan Pelletier
## November 10 2015

## Saves file to list, changes it to lower case. Splits it into colums and
## separate words. Uses words greater than 3 letters to fill dictionary.
## Prevents duplicate values for keys. Uses finished dictionary in a sorted
## format to print an alphabetical list of keys with corisponding values.

##BUGS:
##  accepts symbols and numbers as words(toying with alphabetical values
##  wil fix said problem but I'm out of time)
##  Needs to be reformated for different files 
 
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

##November 9, 2015
##  completed: dictionary creation, line recignition, rejection
##  of three letters or less, no longer duplicates values

##  needs to still: make dictionary all lower cases
##      format into neat colums
##      find a way to make it look through code only once
##      find a way to remove brackets (again... blarg)     

my_file = open('test.txt','r')
def indexMarker(text_file):
    '''Creates a dictionary that sorts and prints all words bigger than 3
        letters in length with their corisponding lines of occurance.'''
    
    sentance = text_file.read()
    lower_sentance = sentance.lower()
    #print(sentance)            #for quick testing of varibles

    word_count = {}       #my dictionary
    
    list_of_words = lower_sentance.split('\n')   #splits it into colums
    #print (list_of_words)       

    for rows in range(0, len(list_of_words)):   
        #print(rows)             
        words = list_of_words[rows].split()   #splits into seperate words
        #print(words)

        for word in words:               #used to separate 4 lettered words

            if len(word) > 3 :
                #print(word)
                
                if word in word_count:              #old key
                    if word_count[word].count(rows + 1) < 1:   #Parleys idea to
                        word_count[word].append(rows +1)        #remove doubles 
                else:
                    word_count[word] = [rows + 1]   #new key

    
    sorted_word_count = sorted(word_count)
    
    for final in sorted_word_count:
        #print(final)
        print('{:9}'.format(final), str(word_count[final])[1:-1])
                                           
indexMarker(my_file)
my_file.close()
