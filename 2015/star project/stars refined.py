import turtle
s=turtle.Screen()
t=turtle.Turtle ()

t.left(60)
t.fillcolor('purple')
t.begin_fill()
#
for star in range(0,4):
    t.forward(50)
    t.left(150)
    t.forward(50)
    t.right(77)

t.forward(50)
t.left(150)
t.goto(0,0)
t.end_fill()
#2
t.penup()
t.goto(150,0)
t.pendown()

t.left(50)
t.fillcolor('red')
t.begin_fill()
for star in range(0,5):
#
    t.forward(50)
    t.left(130)
    t.forward(50)
    t.right(70)
t.forward(50)
t.left(130)
t.forward(50)
t.end_fill()
#3
t.penup()
t.goto(-250,-100)
t.pendown()
t.left(40)
t.fillcolor('lime green')
t.begin_fill()
#
for star in range(0,6):
    t.forward(50)
    t.left(100)
    t.forward(50)
    t.right(48)
t.forward(50)
t.goto(-250,-100)
t.end_fill()
t.hideturtle()
