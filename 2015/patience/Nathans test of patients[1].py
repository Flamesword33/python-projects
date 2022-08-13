#Adding lines.py
#
#by Nathan Pelletier
#Oct 6, 2015
#
#Prints the total for each line of code
#
#known bugs:
#will not count symbols or words 

#frustration report:
#can't figure how to convert string of code into interger
#can't find placement of indent
#data.txt isn't defined
#dual synact errors when running function
#one more problem to ruin my day

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

