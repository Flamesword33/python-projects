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
