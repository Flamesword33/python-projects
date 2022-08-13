import math #for hypotonuse function
# 9/5 c + 32 = f
def convertCtoF (C):
    'Converts celcius to ferenheit'
        #always keep C out of the brackets as 9C = non string but 9*C= what we want
        #can do (9*C/5)+32 instead
    f=(9/5)*C+32
    return f

    # 5/9 (F - 32)
def convertFtoC (F):
    'Converts ferenheit to celcius'
    return(F-32)*(5/9)
    #return can be minipulated further after activation while print will not
    #as the variable dosen't count
    #eg. ( return +1= original statment +1 (print +1 = answer + 1

def compare (a,b) :
    'Compares two varibles finding the larger'
    if a > b:
        print ('Greater')
    elif a==b:
        print ('Equal')
    else :
        print ('Lesser')

#Assume right triangle with two short sides of length
#a and b. Find length of 3rd side.
#Requires math library
def hypotenuse (a,b) :
    'Returns the long side of a right triangle'
    return math.sqrt(a * a + b * b)

def slope(x1,y1,x2,y2):
    'Gives slope of line'
    return(y2-y1)/(x2-x1)
