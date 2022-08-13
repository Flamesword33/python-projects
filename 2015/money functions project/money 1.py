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
