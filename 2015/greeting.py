#square.py
#
#by AUCSC 111
#22 Sept 2015
#
#This program asks the user for an input number
#between 1 and 10
#It then prints a square of that size
#eg
#Input 3
#
#* * *
#*   *
#* * *
#Known bugs: does not check whether input is an interger

#name=input('Please enter your name: ')
#color=input('What is you favorite color: ')
#food=input('What is the best food you\'ve ever eaten: ')

#print('Hi',name,'is it true that you like',color,'and',food,'?')

number=int(input('Please enter a favorite number between 1 and 10: '))
if number<=10 and number > 1 :
   
    #for letter in name :
           #print(letter *number)
#else:
    #print('ERROR')

            #top
        print('* '* number)
            #mid
        little=number - 2#number of middle lines, same as spaces in between
        for middle in range(0,little) :
                print('*'+'  '* (number - 2) + ' *')
            #bot
        print('* '*number)

elif number == 1:
        print('*') 
else:
    print('ERROR')
