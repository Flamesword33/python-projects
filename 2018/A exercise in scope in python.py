x = 12
y = 82
def f(w):
    print("In f top, y is: ", y)
    #print("In f top, x is: ", x)
    def g(y):
        nonlocal x

        def h():
            print("In h, x is: ", x)

        print("In g, x is: ", x)
        x = 55
        h()

    x = 13   #error happens because this is initallizd at to of f by compiler
    g(100)
    print("In f bottom, x is: ", x)

f(x)
print("Global, x is: ", x)
