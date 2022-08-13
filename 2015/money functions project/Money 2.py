import turtle
s=turtle.Screen()
t=turtle.Turtle()

t.penup()

def drawSquare(xLoc, yLoc, size, color, aTurtle):
    '''Draws a square of desired position, size, color
    (put '' around said color) and please input t.''' 

    t.fillcolor(color)
    t.goto (xLoc,yLoc)
    t.forward(size/2)
    t.begin_fill()
    t.right (90)
    t.forward (size/2)
    t.right (90)
    t.forward (size)
    t.right(90)
    t.forward (size)
    t.right(90)
    t.forward (size)
    t.right(90)
    t.forward (size/2)
    t.end_fill()

drawSquare(-150,20,50,'green',t)
drawSquare(20,20,100,'purple',t)
drawSquare(100,-30, 80,'cyan',t)
drawSquare(-100,-100,150,'magenta',t)
drawSquare(300, 200, 100, 'yellow', t)

t.penup()
t.goto(0,0)
t.pendown()
t.dot(10, 'red')
