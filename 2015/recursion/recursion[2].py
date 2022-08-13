def cheer(n):
    'Prints out hips followed by hooray'
    if n == 0:
        print('hooray')
    elif n < 0:
        print('antiHip', end = ' ')
        n += 1
        cheer(n)
    else:
        print('hip',end = ' ')
        n -= 1
        cheer(n)

def reverse(my_string):
    'Returns the reverse of a string of words.'
    if len(my_string) <= 1:
        return my_string
    return my_string[-1] + reverse(my_string[0:-1]) 
