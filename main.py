from characters.boss import Boss
from characters.hero import Hero
from characters.fighter import General_Fighter

"""
Polymorphism, Inheritance practice 
"""
simple_fighter = General_Fighter("Raza")
simple_fighter.special_abilities("Left Punch", "Right Punch")
simple_fighter.lets_fight()

print("\n")

hero = Hero("Ali")
hero.special_abilities("Left Punch", "Right Punch", "Upper Cut", "Left Leg", "Right Leg", "Side Hook")
hero.lets_fight()

print("\n")

boss = Boss("Jack")
boss.special_abilities(True, True, True, False, True, True)
boss.lets_fight()
