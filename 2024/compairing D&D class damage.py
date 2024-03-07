""" compairing D&D class damage.py
    by Nathan Pelletier
    Started March 6 2024

    Original idea by Peter Lewis
    Said program simulates each of D&D 5e's base classes 
    In said sim the program will test:
      AC from 1-30
      Levels 1-20
    Users can control: 
      how many rounds combat takes
      A given characters ability modifier
      which fighter is tested
"""


from math import ceil
from random import randint

class Character:
    def _init__(self, level, ability, weapon, offHandWeapon):
        self.level = level
        self.ability = ability
        self.weapon = weapon
        self.offHandWeapon = offHandWeapon
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
#  Every turn they take Flurry of Blows if able
class Monk(Character):
    def _init__(self, level, ability, weapon, offhand):
        self.ki = level
        self.level = level
        self.ability = ability
        self.weapon = weapon

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
        if self.weapon < self.martialDice:
            self.weapon = self.martialDice
    #end _init__
    
    def turn(self, AC):
        damage = 0
        damage += self.attack(AC, self.weapon)
        damage += self.attack(AC, self.martialDice)
        if self.ki > 0:
            damage += self.attack(AC, self.martialDice)
            self.ki -= 1
        if self.level > 4:
            damage += self.attack(AC, self.weapon)
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
class Rogue(Character):
    def _init__(self, level, ability, weapon, offHandWeapon):
        self.isSneak = True
        self.numOfSneakDice = ceil(level/2)
        return super()._init__(self, level, ability, weapon, offHandWeapon)
    #end _init__
    
    def turn(self, AC):
        damage = 0
        damage += self.attack(AC, self.weapon)
        damage += self.offHandAttack(AC, self.offHandWeapon)
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