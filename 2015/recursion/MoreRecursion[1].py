def banana(x, y):
    if (x > y):
        return x
    return y + banana(x + 1, y - 1)

def cheer(n):
    '''prints out <n> 'hip's followed by 'hooray'
    '''
    if n == 0:
        print('hooray')
    elif n < 0:
        print('antiHip', end = ' ')
        n += 1
        cheer(n)
    else:
        print('hip', end = ' ')
        n -= 1
        cheer(n)


def reverse(aString):
    '''Returns the string reversed
    '''
    if len(aString) <= 1:
        return aString #Maybe something
    return aString[-1] + reverse(aString[0:-1])

def power(x, y):
    '''returns x to the power of y
       x and y must be integers
       return value is a float
    '''
    if y == 0:
        return 1
    elif y > 0:
        return x * power(x, y - 1)
    else: #y < 0
        return 1 / power(x, -y)

def fibonacci(n):
    '''returns the nth fibonacci number
       e.g. fibonacci(6) = 8
            fibonacci(7) = 13
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    #elif n == 2:
    #    return 1
    else:
        
        return fibonacci(n - 1) + fibonacci(n - 2)

fibList = [1, 1]   
def fibonacci2(n):
    '''returns the nth fibonacci number
       e.g. fibonacci(6) = 8
            fibonacci(7) = 13
    '''
    if n <= 0:
        return 0
    elif n == 1:

        return 1

    elif len(fibList) <= n - 1:
        fibNminus1 = fibList[n - 1]
        fibNminus2 = fibList[n - 2]
        sumOf2 = fibNminus1 + fibNminus2
        fibList = fibList + sumOf2
        return sumOf2
    else:
        return fibonacci2()
############################################################################
###########################################################################
import turtle
def koch(n):
    '''return turtle directions for drawing curve
       koch(n)'''
    if n == 0:
        return 'F'
    temp = koch(n - 1)
    return temp + 'L' + temp + 'R' + temp + 'L' + temp


def drawKoch(n):
    'draw nth Koch curve using turtle'
    s = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    directions = koch(n)
    for char in directions:
        if char == 'F':
            t.forward(300/3**n)
        elif char == 'L':
            t.left(60)
        elif char == 'R':
            t.right(120)
        else:
            print('ERROR in code')
