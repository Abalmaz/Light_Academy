import strategy
from random import randint
from read_json import craete_class_from_json
import functools
from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
from army import Army
from clock import Clock as clock
from harmonic_mean import harmonic_mean


armies = craete_class_from_json('army.json')

attacking_army = randint(0, len(armies)-1)
attacking_squad = randint(0, len(armies[attacking_army].squads)-1)

print(strategy.choise_target(armies[attacking_army], armies))






	
