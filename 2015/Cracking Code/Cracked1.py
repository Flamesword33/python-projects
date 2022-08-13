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
