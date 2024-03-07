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
    #end _init__

    def attack(self, AC, dmgDice):
        if (self.roll(20) + self.ability + self.proficency) >= AC:
            return self.roll(dmgDice) + self.ability
        return 0
    #end attack
        
    def offHandAttack(self, AC, dmgDice):
        if (self.roll(20) + self.ability + self.proficency) >= AC:
            return self.roll(dmgDice)
        return 0
    #end offHandAttack
        
    def roll(dice):
        return randint(1, dice)
    #end roll
#end Character
    
class Barbarian(Character):
    pass

class Fighter(Character):
    pass


#monk assumptions:
#  offhand attacks get ability modifier to damage unlike every other class
#  They are weilding a greatclub or quarterstaff with 2 hands, giving them d8 attack
#  Every turn they take Flurry of Blows if able
class Monk(Character):
    def _init__(self, level, ability):
        self.ki = level
        #level 1 monks lack ki
        if self.ki == 1:
            self.ki = 0
        #1-4--> d4, 5-10 --> d6, 11-16 --> d8, 17-20 --> d10
        if self.level < 5:
            self.martialDice = 4
        elif self.level < 11:
            self.martialDice = 6
        elif self.level < 17:
            self.martialDice = 8
        else:
            self.martialDice = 10
        return super()._init__(level, ability)
    #end _init__
    
    def turn(self, AC):
        damage = 0
        mainHand = 8
        if mainHand < self.martialDice:
            mainHand == self.martialDice
        damage += self.attack(AC, mainHand)
        damage += self.attack(AC, self.martialDice)
        if self.ki > 0:
            damage += self.attack(AC, self.martialDice)
            self.ki -= 1
        if self.level > 4:
            damage += self.attack(AC, mainHand)
        return damage
    #end turn
#end Monk
    

class Paladin(Character):
    pass

class Ranger(Character):
    pass

class NewRanger(Character):
    pass

#Rogue assumptions:
#  They are always able to activate sneak attack via hitting targets next to allies
#  They are dual weilding short swords to maximize damage and # of attacks a turn at d6
class Rogue(Character):
    def _init__(self, level, ability):
        self.isSneak = True
        self.numOfSneakDice = ceil(level/2)
        return super()._init__(level, ability)
    #end _init__
    
    def turn(self, AC):
        damage = 0
        damage += self.attack(AC, 6)
        damage += self.offHandAttack(AC, 6)
        if damage > 0:
            damage += self.sneakAttack()
        return damage
    #end turn
    
    def sneakAttack(self):
        damage = 0
        for i in range(self.numOfSneakDice):
            damage += self.roll(6)
        return damage
    #end sneakAttack
#end Rogue