import random
import json
import logging

armies_name_area = ["USA", "Canada", "Germany", "France", "Italy", "UK", "Russia", "Israel", "South Korea", "China"]
strategy_area = ["random", "strongest", "weakest"]
squad_area = ["soldiers", "vehicles"]

n = random.randint(5, 10)

count_armies = random.randint(2, n)

armies_name = random.sample(armies_name_area, count_armies)

def generate_units(type_of_squad):
    unit = {}
    if type_of_squad == 'soldiers':
        health = 100
        recharge = random.randint(100, 1000)
        unit.update({"health": health, "recharge": recharge})
    elif type_of_squad == 'vehicles':
        health = 100
        recharge = random.randint(1000, 2000)
        operators = []
        count_operators = random.randint(1, 3)
        for _ in range(count_operators):
            health = 100
            recharge = random.randint(100, 1000)
            operators.append({"health":health, "recharge": recharge})
        unit.update({"health": health, "recharge": recharge, "operators": operators})
    return unit                


armies = []
for i in range(count_armies):
    name = armies_name[i]
    strategy = random.choice(strategy_area)
    squads = []
    count_squad = random.randint(2, n) 
    for _ in range(count_squad):
        type_of_squad = random.choice(squad_area)
        units = []
        count_units = random.randint(5, 10)
        for _ in range(count_units):
            units.append(generate_units(type_of_squad))    
        squads.append({"type": type_of_squad, "units": units})            
    armies.append({"name": name, "strategy": strategy, "squads": squads})

logging.basicConfig(filename = "create_json.log", format = u'%(filename)s[%(asctime)s]  %(message)s', filemode='w', level = logging.INFO)    

logging.info("Creats {} armies: ".format(count_armies))
for army in armies:
    logging.info("		'{}' with {} squads:".format(army["name"], len(army["squads"])))
    for m, squad in enumerate(army["squads"]):
        logging.info("				{}. type '{}' with {} units".format(m + 1, squad["type"], len(squad["units"])))

json_data = {"armies": armies}

with open('armies.json', 'w') as f:
    json.dump(json_data, f)    