#CRITICAL INFO
name = input('Please enter your name: ')

number=1
#Way 1
#for letter in name:
    #print(str(number)+'. '+letter)
    #number=number+1

#Way 2
for index in range(len(name)):
    print(str(index+1)+'. '+name[index])
    
