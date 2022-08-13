def f(x):
    print('incoming x:', x)
    if x >= 1:
        print(x * '*')
        f(x // 2)
    print('on the way out x:', x)

c = 7
f(c)
print(c)

##Write a blast off method that counts down from n (make sure
##n is positive) and prints "BLAST OFF" when it gets to 0
##Do this with recursion

def blast_off(n):
    if n > 0:
        print(n)
        blast_off(n-1)
    else:
        print('BLAST OFF')

def blast_off2(b):
    for i in range (b):
        print(n - i)
    print('BLAST OFF')
