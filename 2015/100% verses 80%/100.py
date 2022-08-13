def factors(anINT):
    '''Take anINT which is an interger and returns a list of the factors
       of the interger, with the string "Factors or '_' as the first element
       in this list'''
    #Just returns empty list on negitive or 0
    if anINT <1:
        return []
    lowfactorLIST=['Factors of' +str(anINT)]
    highfactorLIST=[]
    for i in range (1,int(anINT**.5)):
        #only need to go as far as square root
        if anINT%i==0: #i divides evenly
                #I will keep 2 lists to avoid sorting
            lowfactorLIST.append(i)
            highfactorLIST.insert(0,anINT//i)
    if anINT%int(anINT**0.5)==0:
        lowfactorLIST.append(int(anINT**0.5))
    return lowfactorLIST+highfactorLIST 
def multiplesINcolums(size):
    for n in range (1,size+1):
        print('{:10}'.format(n*2),'{:6}'.format( n*3),'{:12}'.format (n*5))
