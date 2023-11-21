#critical_rolls_proof.py
#by Nathan Pelltier
#started November 21, 2023

# This project was originally to win an argument.
# 
# In D&D there is an optional rule to encourage dice rolls. Rolling a 1 or a 20 on a d20 grant 
# rolls instant failure and success respectivly. 
# There are also 2 systems to hit an opponent, DC (difficulty class?) and AC (armor class)
#   If a DC check is succeeded the opponent takes 1/2 damage while if an AC roll is failed no damage occurs
#   DC --> an opponent makes a skill check/save to beat a difficult spell or trap. For these rolling under the DC maximizes damage
#   AC --> a character rolls to break through someones armor. For these tests rolling above the AC maximizes damage
# 
# To keep things fair given a d20 roll, we will keep the chance of rolling a success or failure the same
#   DC 0 = AC 21 
#   DC 1 = AC 20
#   DC 2 = AC 19
#   ...
#   DC 10 = AC 11
# 
# I will also use a consistent average damage of 14 as guiding bolt and catapult both do roughly 14 average damage.
#
# This program will go through all posible combinations of roll with and without the critical system
#   anaylisis will follow.


def main():
    dc_without_crit = []
    dc_with_crit = []
    ac_without_crit = []
    ac_with_crit = []

    for dc in range(0, 21):
        dc_without_crit.append(roll_dc_without_crit(dc))
        dc_with_crit.append(roll_dc_with_crit(dc))

    for ac in range(21, 0, -1):
        ac_without_crit.append(roll_ac_without_crit(ac))
        ac_with_crit.append(roll_ac_with_crit(ac))
        
    analyze_dc(dc_without_crit, dc_with_crit)
    analyze_ac(ac_without_crit, ac_with_crit)


def roll_dc_without_crit(dc):
    damage = 0
    for roll in range(1,20):
        if roll < dc:
            damage = damage + 14
        else:
            damage = damage + 7
    return damage

def roll_dc_with_crit(dc):
    damage = 0
    for roll in range(1,20):
        if roll == 1:
            damage = damage + 28
        elif roll == 20:
            pass
        elif roll < dc:
            damage = damage + 14
        elif roll >= dc:
            damage = damage + 7
    return damage

def roll_ac_without_crit(ac):
    damage = 0
    for roll in range(1,20):
        if roll >= ac:
            damage = damage + 14
    return damage

def roll_ac_with_crit(ac):
    damage = 0
    for roll in range(1,20):
        if roll == 20:
            damage = damage + 28
        elif roll >= ac and roll > 1:
            damage = damage + 14
    return damage

def analyze_dc(without_crit, with_crit):
    pass

def analyze_ac(without_crit, with_crit):
    pass