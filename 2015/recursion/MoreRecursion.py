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
    'Returns x to the power of y'
    if y == 0:
        return 1
    elif y > 0:
        return x * power(x, y - 1)
    else:  #y < 0
        return 1 / power(x, -y)

def fibonacci(n):
    'returns the nth fibonacci number'

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = fibonacci(n - 2)
        return (n - 1) + temp


def fibonacci_2(n):
    pass
