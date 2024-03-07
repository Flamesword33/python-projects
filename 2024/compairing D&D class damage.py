""" compairing D&D class damage.py
    by Nathan Pelletier
    Started March 6 2024

    Original idea by Peter Lewis
    Said program simulates each of D&D 5e's base classes 
  
"""


from math import ceil
from random import randint

class Character:
    def _init__(self, level, ability):
        self.level = level
        self.ability = ability
        self.proficency = ceil(level/4) + 1

    def attack(self, AC, dmgDice):
        if (self.roll(20) + self.ability + self.proficency) >= AC:
            return self.roll(dmgDice) + self.ability
        
    def offHandAttack(self, AC, dmgDice):
        if (self.roll(20) + self.ability + self.proficency) >= AC:
            return self.roll(dmgDice)
        
    def roll(dice):
        return randint(1, dice)
    
class Monk(Character):
    def _init__(self, level, ability):
        self.ki = level
        if self.ki == 1:
            self.ki = 0

        if self.level < 5:
            self.martialDice = 4
        elif self.level < 11:
            self.martialDice = 6
        elif self.level < 17:
            self.martialDice = 8
        else:
            self.martialDice = 10

        return super()._init__(level, ability)
class Rogue(Character):
    def _init__(self, level, ability):
        self.isSneak = True
        self.numOfSneakDice = ceil(level/2)
        return super()._init__(level, ability)
