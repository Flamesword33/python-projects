#infinite example
#x=5
#while x>0:
   # print('How are you')
#print('why')


def locationINlist(item,aList):
    answer= []
    index = 0
    while index < len(aList):
        if item == aList[index]:
            answer.append(index)
            #same as awnser=awnser+[aList[index]
        index = index + 1 
    return answer      
