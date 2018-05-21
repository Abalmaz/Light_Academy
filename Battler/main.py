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
attacking_squads = randint(0, len(armies[attacking_army].squads)-1)
attacking_squad = armies[attacking_army].squads[attacking_squads]

print("Attacking army: {}".format(armies[attacking_army].name))
target = strategy.choise_target(armies[attacking_army], armies)
print("Choise target type: {}".format(target.type))
print("Choise target count units: {}".format(target.count_units))
print("Choise target attacking success: {}".format(target.attack_success))
print("Attacking army attacking success: {}".format(attacking_squad.attack_success))

for unit in target.units:
    print("Unit health befor attack: {}".format(unit.health))

if attacking_squad.attack_success > target.attack_success:
    print("Choise target attacking success: {}".format(target.attack_success))
    print("Attacking army attacking success: {}".format(attacking_squad.attack_success))
    target.damage_received(attacking_squad.damage)

for unit in target.units:
    print("Unit health after attack: {}".format(unit.health))
	


	
