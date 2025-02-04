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
    
