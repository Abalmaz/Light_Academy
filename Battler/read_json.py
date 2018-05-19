import json
import functools
from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
from army import Army
from clock import Clock as clock

def craete_class_from_json(file):
	armies = []
	with open(file, 'r') as f:
		data = json.load(f)

	for army in data['armies']:
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
		
		army = Army(army['name'], army['strategy'], squads)
		armies.append(army)
	return armies		
