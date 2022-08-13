def factors(anINT):
    '''Take anINT which is an interger and returns a list of the factors
       of the interger, with the string "Factors or '_' as the first element
       in this list'''
    if anINT <1:
        return []
    factorLIST=['Factors of' +str(anINT)]
    for i in range (1,anINT +1):
        if anINT%i==0: #i divides evenly
            factorLIST.append(i)
    return factorLIST 
