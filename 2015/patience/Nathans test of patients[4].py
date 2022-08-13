##  Nathan's Journal report
##actually did this on my own without any help from Landen or Mattis unlike(90%)
##previous questions (please help me understand previous questions)
##note to self: need to find way to add row and col before starting new row of
## chart. Also need to find out if numbers are correct
## good news chart is correct
## still can't get row and col to print first
## can't get rows and coloms to line up
##I SAY A WHAT WHAT!(10:57)
## ok now to just get the top working
## top row almost works now prints 2 - 2 -
##Got it working finally with Mattias's help

#Remainders table.py

#by Nathan Pelletier
#Oct 6,2015

#Prompts user to give two numbers for division table, re-prompts
#if numbers are zero or lower. The program then creates a table
#of remainders eg.
#Please input a positive number: 2
#Please input a positive number to divide by: 2
#
#    2 2
#    - -
#2 : 0 1
#2 : 0 0

#Known bugs:
# will accept words, symbols which will lead to an error
#thankfully it is not an uncontrolled infinite loop(keep ctrl-c close just
# in case)

def remainders(row,col):
    'prints a remainder chart starting at one and going to desired numbers'
    print('   ',row*(str(row)+' '),'\n','  ',row*'- ')
    for j in range (1,col+1):    
        print(col,':',end=' ')
        for i in range (1,row+1):
            
            print(j%i, end= ' ')
        print()
    
row=0
col=0
while row<=0 or col<=0:
    row=int(input('Please input a positive number: '))
    col=int(input('Please input a positive number to divide by: '))

remainders(row,col)
