##Rock Paper Scissors Game
##
##AUCSC 111
##16 November 2015
##
##This program plays this simple game.
##User will enter choice as a string
##(ie by typing it).
##The computer will make a choice at random.
##User decides how many rounds to play.

import random  #for computer choice

class Choice:
    value = ''
    valid_choices = ['rock', 'paper', 'scissors']

    def __init__(self, value):
        '''Constructor '''
        self.value = value

    def __gt__(self, another):
        '''Setting up '>' operator.
           rock > scissors, scissors > paper, paper > rock
        '''
        if self.value == 'rock':
            if another.value == 'scissors':
                return True
        elif self.value == 'scissors':
            if another.value == 'paper':
                return True
        elif self.value == 'paper':
            if another.value == 'rock':
                return True

        return False

class User_Choice(Choice):
    def get_choice(self):
        '''Gets choice form user. Loops until valid'''
        self.value = ''
        while self.value not in self.valid_choices:
            self.value = input('Please enter your choice as (\'rock\',\
\'paper\',\'scissors\'): ').lower()

class Computer_Choice(Choice):
    def get_choice(self):
        '''Generates random choice for cpu'''
        self.value = self.valid_choices[random.randrange(0, 3)]

def start_game():
    num_games = int(input('How many rounds do you want to go: '))
    for i in range (num_games):
        your_choice = User_Choice('')
        my_choice = Computer_Choice('')
        my_choice.get_choice()
        your_choice.get_choice()
        print('My choice: ' + my_choice.value + '\nYour choice: ' + your_choice.value)

        if my_choice > your_choice:
            print('Lose')
        elif my_choice < your_choice:
            print('Winner!')
        else:
            print('Tie')
