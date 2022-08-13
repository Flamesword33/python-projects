#This function changes letters between lower and upper case


def swapCASE(aLetter):
    'Returns aLetter(a single character) in its opposite case: lower to upper'
    letterASnumber=ord(aLetter) #convert into an interger
    if letterASnumber >= 65 and letterASnumber <=90 : #capitol letter
        letterASnumber = letterASnumber +32
        
    elif letterASnumber >= 97 and letterASnumber <=122: #lower case
        letterASnumber= letterASnumber-32
    #else non alpha-- omit this condition

    return chr(letterASnumber)

