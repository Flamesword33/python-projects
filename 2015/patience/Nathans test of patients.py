myFile=open('data.txt','r')

#simply prints file
##for banana in myFile :
##    print(banana, end='')
##print('___________')

#finds how many entries are in file
##total=0
##for line in myFile:
##    listOFline=line.split();
##    #print(len(listOFline))
##    total=(len(listOFline))+total
##print('Number of entries:' , total)

numTOfind= input('Please enter an interger to find: ')
##lineNUM=0
##continueCheck= True
##for line in myFile :
##    if continueCheck==True
##    lineNUM=lineNUM+1
##    lineList = line.split()
##    for entry in lineList:
##        if numTOfind==entry:
##            print (lineNUM)    
##            continueCheck=False
##            break

def findValueInData(x,myFile):
    lineNum=0
    for line in myFile:
        lineNum=lineNum+1
        lineList=line.split()
        for entry in lineList:
            if x == entry:
                return (lineNum)
print(findValueInData(numTOfind,myFile))

        
myFile.close()
