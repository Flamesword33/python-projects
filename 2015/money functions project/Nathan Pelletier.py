#1
def grossPay (numHOURS,payRATE):
    'Calculates the pay earned by the number of hours worked and the rate of earnings'
    if numHOURS < 0:
        print ('HOW???')
        return 0
    elif numHOURS<=40 and payRATE>=0:
        return payRATE*numHOURS
    elif numHOURS <=60 and payRATE>=0 :
        return ((numHOURS-40)*1.5*payRATE)+(payRATE*40)
    elif numHOURS > 60 and payRATE>=0 :
        return ((numHOURS-60)*2*payRATE)+(20*1.5*payRATE)+(payRATE*40)
    else :
        print ('Your boss is breaking a few laws!')
        return 0
       
print('10 hours at $10:    ', grossPay(10, 10))
print('39 hours at $15:    ', grossPay(39, 15))
print('40 hours at $10:    ', grossPay(40, 10))
print('40.5 hours at $10:  ', grossPay(40.5, 10))
print('50 hours at $10:    ', grossPay(50, 10))
print('59 hours at $10:    ', grossPay(59, 10))
print('60 hours at $10:    ', grossPay(60, 10))
print('60.5 hours at $20:  ', grossPay(60.5, 20))
print('65 hours at $10:    ', grossPay(65, 10))
print('0 hours at$10:     ', grossPay(0, 10))
print('-2 hours at $10:    ', grossPay(-2, 10))

#2
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

#3
#Factoring.py
#
#by Nathan Pelletier
#Oct 6, 2015
#
#This program asks for a number to change into its factors
#It returns the factors in brackets in cronological order if factors are present
#eg. factor (20)
#[1, 2, 4, 5, 10, 20]
#
#known bugs
#negitive numbers are treated as 0
def factors  (number):
    'puts a number into its bace multiples'
    final=[]
    if number >0 :
        for i in range(1,number+1):

            if number%i==0:
#thank you thank you thank you student aid without you the whole code was caput.
                final.append(i)
    return final
            
    
print('49 ', factors(49))
print('60 ', factors(60))
print(' 0 ', factors(0))
print(' -1 ', factors(-1))
print(' 1 ', factors(1))
print(' 2 ', factors(2))
print('17 ', factors(17))
