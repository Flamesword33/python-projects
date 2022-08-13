name=input ('Please enter your name: ')
number=len(name)
        
        #top
print(number*' '+name[0])
        #mid
number=len(name)-1
inverse=1

if len(name)> 1 :
    for letter in name[1:-1]:
        print((number*' ')+letter+(inverse*' ')+letter)

        number=number-1
        inverse=inverse+2
            #bot
        #Mattias fixed the brackets
    print((' '+name[-1])*(len(name)))
