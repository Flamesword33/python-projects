# A_simple_retry.py
# by Nathan Pelletier

import turtle              
s = turtle.Screen()
t = turtle.Turtle()

def rectangle():
    for i in range(4):                              #rectangle
        h = 'yellow', 'green', 'blue', 'orange'
        t.dot(5, h[i])
        t.forward(50)
        t.right(90)

def dimond():
    t.left(45)
    for j in range(4):
        g = 'red','purple','red','purple'
        t.pencolor(g[j])
        t.forward(150)
        t.right(90)

def stars(n):
    'star 1, 2, 3'
    if n == 1:
        t.left(60)
        t.fillcolor('purple')
        t.begin_fill()

        for star in range(4):
            t.forward(50)
            t.left(150)
            t.forward(50)
            t.right(77)

        t.forward(50)
        t.left(150)
        t.goto(0,0)
        t.end_fill()
    elif n == 2:
        t.left(50)
        t.fillcolor('red')
        t.begin_fill()

        for star in range(6):
            t.forward(50)
            t.left(130)
            t.forward(50)
            t.right(70)
        t.end_fill()
    elif n == 3:
        t.left(40)
        t.fillcolor('lime green')
        t.begin_fill()
#
        for star in range(6):
            t.forward(50)
            t.left(100)
            t.forward(50)
            t.right(48)

        t.forward(50)
        t.goto(0,0)
        t.end_fill()
    else:
        print('WHY!')

def mega_star(m):
    t.speed(0)
    t.penup()
    t.fillcolor('green')
    t.begin_fill()
    if m == 1:
        for i in range (170):
            stars(1)
    elif m == 2:
        for j in range (40):
            stars(2)
    elif m == 3:
        for k in range (45):
            stars(3)
    t.end_fill()
    

