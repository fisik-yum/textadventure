#library for text adventure games?
import random

#simple stuff!
def chance(chance_of_happens):#percentage
    if random.randint(0,100)<=chance_of_happens:
        return 1
    if random.randint(0,100)>chance_of_happens:
        return 0
def addToInventory(inventory, item):#inventory must be a list
    inventory.append(item)
def removeFromInventory(inventory, item):
    inventory.remove(item)

#now to character-based stuff!
class character:
    def __init__(player, name, job, level, healthInc):
        player.name=name
        player.job=job
        player.level=level
        player.maxhealth=level*healthInc

class mob:
    def __init__(mob, race, weapon, level, minDamage, maxDamage):
        mob.race=race
        mob.level=level
        mob.weapon=weapon
        mob.minDamage=minDamage
        mob.maxDamage=maxDamage
        mob.damageDone
                