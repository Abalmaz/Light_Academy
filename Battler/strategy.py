from random import randint

def weakest(armies):
    target_squad = []
    for n in range(len(armies)):
       for i in range(len(armies[n].squads )-1):
            target_squad = armies[n].squads[i]
            if armies[n].squads[i + 1].attack_success > target_squad.attack_success:
                target_squad = armies[n].squads[i + 1]        

    return target_squad    


def strongest(armies):
    target_squad = []
    for n in range(len(armies)):
       for i in range(len(armies[n].squads)-1):
            target_squad = armies[n].squads[i]
            if armies[n].squads[i + 1].attack_success < target_squad.attack_success:
                target_squad = armies[n].squads[i + 1]

    return target_squad              

def random(armies):
    army = randint(0, len(armies - 1))
    squad = randint(0, len(army.squrds - 1))
    target_squad = armies[army][squad]
    
    return target_squad

def choise_target(attacking_army, armies):
    target = []
    target_armies = []
    for army in armies:
        if army.name != attacking_army.name:
            target_armies.append(army)

    if attacking_army.strategy == 'weakest':
        target = weakest(target_armies)
     


    elif attacking_army.strategy == 'strongest':
        target = strongest(target_armies)        


    else:
        target = random(target_armies)        

    return target       


