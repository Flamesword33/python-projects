#dimond.py
#
#by Nathan Pelletier
#29 Sept 2015
#
#This program asks the user to imput their name
#It prints thier name in the form of a dimond
#eg
#input James
#
#    J
#   a a
#  m   m
# e     e
#s       s
# e     e
#  m   m
#   a a
#    J
#Varients with single letters
#eg without if statement
#a
#aa
#a
#eg with if statement and indenting
#a
#Known bugs: only prints back input in desired format (won't distinguish
#symbols, numbers, or functions from letters)

name=input ('Please enter your name: ')
number=len(name)
        
        #top
print(number*' '+name[0])
        #mid
number=len(name)-1
inverse=1

#if len(name)> 1 :

#input previous line with indentation of all below lines if you only want one
#letter for a one letter input

for letter in name[1:-1]:
    print((number*' ')+letter+(inverse*' ')+letter)

    number=number-1
    inverse=inverse+2
            #end letter
print((' '+name[-1])+(inverse*' ')+name[-1])

        #2nd layer
number=1
inverse=len(name)*2-2
    #i=-1
        #need to talk to teacher about inverting the range 
    
for letter in range(1,len(name)-1):#need a way to go from -1 to 1
    print(((number+1)*' ')+name[len(name)-letter-1]+((inverse-3)*' ')+name[len(name)-letter-1])
       # i=(1-i)
    number=number+1
    inverse=inverse-2
            #end
number=len(name)
print(number*' '+name[0])
    
