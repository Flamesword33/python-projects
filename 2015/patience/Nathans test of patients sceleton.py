
        
myFile = open('data.txt','r')
def biggestOnLines(inF):
    'an open input file, ready for reading'
    finish=[]
    for line in myFile:
        listOFline=line.split();
        for number in listOFline:
            finish.append(int(number))

            
biggestOnLines(myFile)
print(biggestOnLines)
myFile.close()
