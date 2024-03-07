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
class Monk(Character):
    def _init__(self, level, ability):
        self.ki = level
class Rogue(Character):
    def _init__(self, level, ability):
        self.isSneak = True
        self.numOfSneakDice = ceil(level/2)
        return super()._init__(level, ability)
