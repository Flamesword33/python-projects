#AUCSC111
#October 5,2015

#program to print a stair case of numebers based on the users
# input number. If the user enters a negitive they must try again
#until a positive number is entered.
#eg user enters 5:
#1
#12
#123
#1234
#12345



def stairs (number):
    'prints stair case of size number'
    for j in range(1, number+1):
        for i in range (1,j+1):
    #thanks mattias        
            print( i%10, end = ' ')
        print()
number=0
while number <=0:
    number=int(input('Please enter a positive number: '))


stairs (number)

