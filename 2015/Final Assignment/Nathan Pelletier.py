##Company_Sallary.py
##by Nathan Pelletier
##
##TO USE:
##    name = Employee('name', 'name', wage)
##    name = Salaried_Employee('name', 'name', wage, vacation time)
##    name.print_cheque(hours)
##
##Creates two classes that create Employees paid
##hourly and Employees paid yearly
##redefines + to add wages and creates a print_cheque function which
##allows the user to see the employees pay cheque this week after entering the
##time worked that week.
##
##bugs:
##    can't diferentate between symbols, numbers and letters, only correct
##    imput will work (can have man name & , 56 but if wage isn't number
##    program will crash)
##
##    Salaried_Employee needs a wage input in order to change vacation
##    hours, attempts to put in vacation hours only wil result in wage changes

##November 10 
##need to set up class skeleton!
##need to import money function

##November 17
##needs to use locale function!
##needs to hold default wage!
##needs to quickly add new employees!

##November 23
##got add and print_cheque running
##got SalariedEmployee working
##fixed new print_cheque

##TESTING

##>>> ee = Employee('Edward', 'Elric')
##>>> bb = Employee('Bugs', 'Bunney', 20)
##>>> ee
##Employee: Edward Elric: $11.20
##>>> bb + ee
##'$31.20'

import locale
locale.setlocale(locale.LC_ALL, '')

'English_Canada.1252'

class Employee():
    'allows employees and wages to be entered for recipt statements'

    def __init__ (self, f_name, l_name, wage = 11.2):
        '''creates the entries for first name, last name and wage
        if no wage is present minimum wage will be used'''

        self.first_name = f_name
        self.last_name = l_name
        self.wage = wage
        
    def __repr__ (self):
        'prints employee names and wage in easy to read format'

        return 'Employee: ' + str(self.first_name) + \
               ' ' + str(self.last_name) + ': ' + \
               str(locale.currency(self.wage))

    def __add__ (self, another):
        'sets + to add wages of employees for group projects'

        added_pay = (self.wage + another.wage)
        return locale.currency(added_pay)
        ##return self.first_employee.wage + self.second_employee.wage
        ##needless to say didn't work

    def print_cheque(ponie, time_worked):                 #sorry about ponie
        '''prints a cheque for weekly time worked by
           employee and gives amount lost to taxes'''
                                                          #bet with mattias
        if time_worked > 40:      #overtime               #that you'd accept 
            gross_pay = ponie.wage * time_worked + \
                        (time_worked - 40) * ponie.wage   #ponie instead
                                                          #of self
        else:                   #regular
            gross_pay = ponie.wage * time_worked

        if gross_pay > 42000/52:     #high earners
            tax = gross_pay * 0.22
        else:                        #average earners
            tax = gross_pay * 0.15

        final_amount = gross_pay - tax

        print('-' * 50)
        print()
        print('PAY TO:  ', ponie.first_name , ' ', ponie.last_name, \
              ' ', ' ' * 10, 'AMOUNT', locale.currency(final_amount))
        print()
        print()
        print()
        print('Gross Pay:  ', locale.currency(gross_pay))
        print('   Tax       ', locale.currency(tax))
        print('-' * 50)


class Salaried_Employee(Employee):    #off of coding from Employee
    'Creates a yearly paid employee'

    def __init__(self, f_name, l_name, wage = 25000, vacation_time = 0):
        'adds Employee to system'
        
        super().__init__(f_name, l_name, wage)
        self.vacation = vacation_time
            ##didn't know about super until Mattias
            ## calls old function for init
        
    def print_cheque(self, time_worked):     
        '''Prints employee earnings and deductions. Also keeps track of
        vacation hours via time_worked'''
        #didn't have time to super so I re-wrote instead

        gross_pay = self.wage / 52

        tax = gross_pay * 0.15

        benifits = gross_pay * 0.015

        if time_worked > 45:       #adding vacation hours
            self.vacation = self.vacation + (time_worked - 45)
        elif time_worked < 35:     #subtracting vacation hours
            self.vacation = self.vacation - (35 - time_worked)

        final_amount = gross_pay - tax - benifits

        print('-' * 50)
        print()
        print('PAY TO:  ', self.first_name , ' ', self.last_name, \
              ' ', ' ' * 10, 'AMOUNT', locale.currency(final_amount))
        print()
        print()
        print()
        print('Gross Pay:  ', locale.currency(gross_pay))
        print('Deductions:')
        print('   Tax       ', locale.currency(tax))
        print('   Benefits  ', locale.currency(benifits))
        print('Vacation:    ', self.vacation, ' hours')
        print('-' * 50)
