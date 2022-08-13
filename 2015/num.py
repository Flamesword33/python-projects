num1=int(input ('Please enter number 1: '))
num2=int(input ('Please enter number 2: '))
num3=int(input ('Please enter number 3: '))

if num1 < 0 or num2 <0 or num3 <0 :
    print('error')
else :
    print('The average is.',(num1 + num2 + num3)/3)
average=(num1 + num2 + num3)/3
if average >= 83:
    print ('awsome')
elif average>= 70:
    print('good work')
elif average>= 60:
    print ('work harder')
elif average>= 50:
    print ('see prof')
else :
    print ('get out fast')
