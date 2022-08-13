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
