import turtle
s=turtle.Screen()
t=turtle.Turtle ()

t.penup()
t.fillcolor('red')
t.begin_fill()
t.backward(290)
t.forward(580)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.left(180)
t.circle(50,200)
t.end_fill()

#house structure

t.fillcolor('purple')
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.circle(50)
t.end_fill()

t.goto(50,0)
t.forward(200)
t.begin_fill()
t.circle(50)
t.end_fill()

t.goto(150,100)
t.right(180)
t.begin_fill()
t.circle(50)
t.goto(290,0)
t.goto(150,0)
t.end_fill()
#windows

#door
t.goto(100,0)
t.fillcolor ('black')
t.begin_fill()
t.left(180)
t.circle(100,180)
t.end_fill()

