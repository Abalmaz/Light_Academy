import json
import functools
from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
from army import Army
from clock import Clock as clock


with open('army.json', 'r') as f:
	data = json.load(f)

for army in data['armies']:
	army_name = 'army_' + army['name']
	squads = []
	
	for squad in army['squads']:

		if squad['type'] == 'soldiers':
			units = []
			for unit in squad['units']:
				unit = Soldier(health = unit['health'], recharge = unit['recharge'])
				units.append(unit)
			squads.append(Squad(squad['type'], squad['count_units'], units))		

		elif squad['type'] == 'vehicles':
			units = []
			for unit in squad['units']:
				operators = []
				for operator in unit['operators']:
					operators.append(Soldier(operator['health'], operator['recharge']))
				units.append(Vehicle(unit['health'], unit['recharge'], unit['count_operators'], operators))
			squads.append(Squad(squad['type'], squad['count_units'], units))
	
	vars()[army_name] = Army(army['name'], army['strategy'], squads)	


print(army_USA.name)
print(army_USA.strategy)
for squad in army_USA.squads:
	print(squad.type)
	for unit in squad.units:
		print(unit.health)

print(army_USA.squads[0].units[1].health)