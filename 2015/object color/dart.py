x=int(input('Please input horizontal coordinate: '))
y=int(input('Please input vertical coordinate: '))
import math
if x**2+y**2<=25:
    print ('Bulls eye!')
#Lane helped me with the square.
elif abs(x)<=10 and abs(y)<=10:
    print ('You hit it!')
else:
    print ('''And that was the wall... I hope your paying for that.
           I mean honestly who hits  the wall. In 1883 maybe but come on
           the twenty first centry is here people.''')
        
