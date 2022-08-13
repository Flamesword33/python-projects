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
