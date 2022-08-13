import turtle
s= turtle.Screen()
t= turtle.Turtle()

#epillepsy!!!
t.speed (10)

t.pencolor('white')

t.dot(100, 'green')
t.dot(100, 'green')


#now to make it move...somehow
t.dot(100, 'white')
t.forward(10)
t.dot(100, 'green')
t.dot(100, 'green')

#that was the repeated code so

for ball in range(150):
    t.dot(100, 'white')
    t.forward(10)
    t.dot(100, 'green')
    t.dot(100, 'green')
    
