##Cracked.py
##by Nathan Pelletier
##Oct 31,2015

#Program decodes by letter shifting; program will crack
#cypher based on the formula (distance*300+40)//2=f. Once the shift
#is found the program will shift all letters the set distance and
#print said letters.

#input
##(To ensure the function will work save
##this program in the same folder as your code)
##
##             Please paste the name of a file you wish to decode: message2.txt
#output
##==++==++==++==++==++==++==++==++==++==++==++==
##
##  My AUCSC 111 class is absolutely brillant!
##      I brag about them to other profs.
##
##==++==++==++==++==++==++==++==++==++==++==++==

#Bugs:
#If file name isn't exactly the same as inputed file will crash
#to reinitate program without restarting will yeild:
#>>> file = 'message2.txt'
#>>> myFile
#<_io.TextIOWrapper name='message2.txt' mode='r' encoding='cp1252'>
#(which I think is totally cool, please give me
# feedback on whats actually happening, thank you!)

##   Project status: Completed              (!=done)
## Needs to crack cypher automaticly!
##Needs to take cypher and use it!
## Needs to print hidden message without changing symbols!

##Needs to print in a proper line!
## Needs to add 26 to numbers lower than u!
##Needs to work with other code!
file = input('''(To ensure the function will work save
this program in the same folder as your code)

             Please paste the name of a file you wish to decode: ''')       
myFile = open(file,'r')
#change to input latter for her ease of acess
def fDecrypt(inF):
    '''Input a file to be decoded by letter shifting; program will crack
    cypher based on the formula (distance*300+40)//2=f. Once the shift
    is found the program will shift all letters the set distance and
    print said letters.'''
    
    number_form = []  #puts letters into number equivilent

    first_number = int(inF.readline()) #coded cypher is now usable 

    cypher = ((first_number*2-40)//300)  #code key given and reversed

    raw_code = inF.read()  # code is now usable

    print()  #makes final code more readable

    for letters in raw_code: 
        number_form = ord(letters)  #code is now all numbers
       
        if number_form >= 65 and number_form <= 90:  #caps
            final_number = number_form - cypher

            if final_number < 65:                 #loops alphabet
                checked_number = final_number + 26
                print(chr(checked_number),end='') #end='' puts columed code 
                                                  #into proper rows
            else:
                print(chr(final_number),end='')

        elif number_form >=  97 and number_form <= 122:   #no caps
            final_number = number_form - cypher

            if final_number < 97:
                check_number = final_number + 26
                print(chr(check_number),end='')

            else:
                print(chr(final_number),end='')

        else:     #other
            print(letters,end='')
                

fDecrypt(myFile) #opens program for you after input
myFile.close()

#Completion_Chart.py
#by: Nathan Pelletier
#November 2, 2015

#Creates numbered graph and then uses a matrix to convert the given tuple
#to a usable format. It then fills the grid with the apropriate stars

#bugs:
#     can not use a non-tuple or list format for star_points 
#     can not use letters or symbols

#feed back corner:
#Please explain how to remove brackets from a printed list.
#Though I may seem to have a grasp on indexing and matrixes I am still
#thoroughly lost in the topic
#OH and cool quotes from Einstine

##Project goals:INCOMPLETE                                          !=done
##          Print a row and colum of numbers assigned to a varible!
##          Use a user inputed matrix into a grid format!
##          Print stars in said spots!
##          If not a grid print error!
##          If out of range print error!
##          removing the brackets 

def displayGrid (size,star_points):
    '''Uses a given number to create a grid, then uses a list of data as
       co-ordanite points to place stars on the grid
       use a [(5,1),(4,3),(1,1)] format to enter data for star_points'''
    control = 0    #limits the matrix in its for loop
    matrix=[]       #a matrix with coordinates to use the tuple

    if size > 0:    #create grid

        for creation in range(0,size):    #creates loop to fill matrix
            matrix1 = [''] * size
            matrix.append(matrix1)

        for index in star_points:       #reads and interprets tuple
            y = index[1]
            x = index[0]

            if size >= x and size >= y:     #adds a star to list
                matrix[x-1][y-1] = ('*')

            else:                           #avoids an error and explains
                print('ERROR -- ','(', x,',',y,') OUT OF RANGE')
            
        for col in range(1,size+1):     #creates numbers for colums
            print(' ',col,end='')
        print()

        for row in range(1,size+1):     #creates numers for rows and
            print(row,matrix[control])  #adds the filled matrix
            control = control + 1       #while control keeps matrix to one
                                        #copy
    else:    #doesn't create grid
        print('ERROR -- FAILED TO CREATE GRID')
displayGrid(7, [[1,2],(5,1),(3,4),(3,4),(6,1)]) #testing

##print(1,2,3,4,5) 
##for i in range(1,6):
##    print(i,end=' ')
##finding universal code that equivilates to 

