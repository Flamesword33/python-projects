"""
flare-fall-roll-average.py
by Nathan Pelletier
started Febuary 4 2025

Basic idea came from Trekiros- Flare Fall Combat Tutorial 5:05
https://youtu.be/Zi1OHAJ6IAI?t=305
In flare fall if a dice roll is at its max it rolls again, infinitly
I want to test this with different dice to determine what average value
will come from rolls of this style. 

Below I will test: 
  average value overall,
  max value from each dice,
  how often a second roll occurs on a given dice,
"""

from random import randint

class Explosive_Dice:
    """Explosive dice is a game feature where a max rolled dice is rolled again.
       This class is designed to test multiple cases to determine game balance shifts from
       adding said mechanic."""
    def __init__(self, face_count: int, number_of_tests: int):
        """Class conducts number_of_tests on a dice with a given face_count"""
        self.face_count = face_count
        self.number_of_tests = number_of_tests

    def roll(self):
        return randint(1, self.face_count)
    
    def average_overall(self):
        '''Finds average roll over x tests'''
        total = 0
        for test in range(self.number_of_tests):
            total = total + self.explosive_roll_total()
        return total/self.number_of_tests
    
    def explosive_roll_total(self):
        """Rolls a dice and if it hits max value then it rolls again.
        Returns the sum of all rolls"""
        roll = self.roll()
        if roll == self.face_count:
            return roll + self.explosive_roll_total()
        else:
            return roll

    def max_value(self):
        '''Finds max roll over x tests'''
        max = 0
        current = 0
        for test in range(self.number_of_tests):
            current = self.explosive_roll_total()
            if max < current:
                max = current
        return max

    def frequency_of_multi_roll(self):
        """Rolls exploding dice and prints off the frequency of how many times the dice exploded"""
        frequency = [0]*10
        current_roll = 0
        for test in range(self.number_of_tests):
            current_roll = self.explosive_roll_count()
            if current_roll <= len(frequency):
                frequency[current_roll-1] += 1
            else:
                for x in range(current_roll - len(frequency)):
                    frequency.append(0)
                frequency[current_roll-1] += 1
        self.frequency_print(frequency)

    def explosive_roll_count(self):
        """Rolls a dice and if it hits max value then it rolls again.
        Returns number of times the dice was rolled."""
        counter = 1
        roll = self.roll()
        if roll == self.face_count:
            return counter + self.explosive_roll_count()
        else:
            return counter
        
    def frequency_print(self, frequency: list):
        """Formats printing of a frequency list for excel graphing."""
        for i in range(len(frequency)):
            print(i+1, " :", frequency[i], end="\n")

        
    

