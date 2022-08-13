#Adding lines.py
#
#by Nathan Pelletier
#Oct 6, 2015
#
#Prints the total for each line of code
#
#known bugs:
#will not count symbols or words 
myFile = open('data.txt','r')
def totalOnLines(inF):
    'an open input file, ready for reading'
    total = 0
    for line in inF:
        listOFline=line.split();
            #Mattias helped me work this for loop
        for number in listOFline:
            total = total + int(number)
        print (total)
        total=0
            
totalOnLines(myFile)

myFile.close()

#Maximum lines.py

#by Nathan Pelletier
#Oct 13, 2015
#
#Prints the maximum number in a line of a program
#
#known bugs:
#It will not discriminate between words, symbols and numbers.

myFile = open('data.txt','r')
def biggestOnLines(inF):
    'an open input file, ready for reading'
    for line in inF:
        variable=[]
        listOFline=line.split();
        for number in listOFline:
            variable.append(int(number))
        if len(variable) > 0:
            print(max(variable))
        else :
            print()
biggestOnLines(myFile)

myFile.close()

#Count.py

#by Nathan Pelletier
#Oct 6, 2015

#prints the total number of ocerances of a specified number in the data
#set eg.
#Please enter a number for counting: -100
#100

#Known bugs:
#please tell me if every three tab presses brings up a paste menu
#Will not repromt user upon mis-type
#will not accept letters or symbols
        
myFile = open('data.txt','r')
def howMany(inF,num):
    '''an open input file, ready for reading,
       num to find in file'''
    fullLIST = []
    for line in inF:
        listOFline=line.split()
        for number in listOFline:
            fullLIST.append(int(number))
    return fullLIST.count(num)
num=int(input('Please enter a number for counting: '))

print('Total occurences of', num, 'is',howMany(myFile,num))

myFile.close()

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
