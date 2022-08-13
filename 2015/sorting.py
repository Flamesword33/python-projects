killer=[17,25,2,8,16]
def sort(intList):
    'sorts list from biggest to smallest'
    awnser=[]
    for p in range(len(intList)):
        biggest= intList[0]
        
        for index in range (1,len(intList)) :
            if intList[index]>biggest:
                biggest=intList[index]

        awnser.append(biggest)
        intList.remove(biggest)
    return awnser
