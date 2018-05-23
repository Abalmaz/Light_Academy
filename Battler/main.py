import time
import logging
import strategy
import clock
from random import randint
from read_json import craete_class_from_json

 
def main():

    logging.basicConfig(filename="battle.log", filemode="w", format = u'%(filename)s[LINE:%(lineno)d]# [%(asctime)s]  %(message)s', level=logging.INFO)
    start_game = clock.Clock()


    logging.info("Battle is started")
    print("Battle is started")
    armies = craete_class_from_json('json_generator/armies.json')
    logging.info("Armies participating in the battle:")
    print("Armies participating in the battle:")
    logging.info("Count of armies %s"%(len(armies)))
    print("Count of armies %s"%(len(armies)))
    for army in armies:
        logging.info("    Army of %s, strategy '%s', count of squads %s"%(army.name, army.strategy, len(army.squads)))
        print("    Army of %s, strategy '%s', count of squads %s"%(army.name, army.strategy, len(army.squads)))

    print("#"*60)    


    while True:
        attacking_army = randint(0, len(armies)-1)
        attacking_squads = randint(0, len(armies[attacking_army].squads)-1)
        attacking_squad = armies[attacking_army].squads[attacking_squads]
        
        logging.info("*"*80)
        
        logging.info("Attacking army: %s, attacking squad (type '%s', counts:  %s)"%(armies[attacking_army].name, attacking_squad.type, len(attacking_squad.units) ))
        target_squad = strategy.choise_target(armies[attacking_army], armies)
        logging.info("Target squad: type: '%s', counts:  %s"%(target_squad.type, len(target_squad.units) ))

        if attacking_squad.attack_success > target_squad.attack_success:           
            
            print("Attacking army: %s, attacking squad (type '%s', counts:  %s)"%(armies[attacking_army].name, attacking_squad.type, len(attacking_squad.units) ))
            print("Target squad: type: '%s', counts:  %s"%(target_squad.type, len(target_squad.units) ))
            logging.info("Attack is successful, damage is %.3f"%(attacking_squad.damage))
            print("Attack is successful, damage is %.3f"%(attacking_squad.damage))
            target_squad.damage_received(attacking_squad.damage)
            
            # Operation with attaking squads
            for n, unit in enumerate(attacking_squad.units):
                unit.time_recharge = clock.set_time(unit.recharge)
                if attacking_squad.type == 'soldiers':
                    unit.experience += 1
                elif attacking_squad.type == 'vehicles':
                    for m, operator in enumerate(unit.operators):
                        operator.experience += 1                                                     
            
            if target_squad.is_live() == False:
                logging.info("Target squad is destroy")
                print("Target squad is  destroy")

            for n, army in enumerate(armies):
                if army.is_live() == False:
                    logging.info("Army %s is destroy"%(army.name))
                    print("Army %s is destroy"%(army.name))
                    del armies[n]
                    logging.info("Count of armies: %s"%(len(armies)))
                    print("Count of armies: %s"%(len(armies)))

            print("*"*80)
            logging.info("*"*80)
            for army in armies:
                print(army.name)
                logging.info(army.name)
                for squad in army.squads:
                    print("    Squad type: %s"%(squad.type))
                    logging.info("    Squad type: %s"%(squad.type))
                    print("    Squad counts: %s"%(len(squad.units)))
                    logging.info("    Squad counts: %s"%(len(squad.units)))
                    for n, unit in enumerate(squad.units):
                        print("        Unit %s health %.2f,  attack success %.3f, time recharge: %s"%(n+1, unit.health, unit.attack_success, time.strftime("%H:%M:%S", time.localtime(unit.time_recharge))))
                        logging.info("        Unit %s health %.2f,  attack success %.3f, time recharge: %s"%(n+1, unit.health, unit.attack_success, time.strftime("%H:%M:%S", time.localtime(unit.time_recharge))))
            logging.info("*"*80)
            print("*"*80)                    

        else:
            logging.info("Attacking squad is lose")

        logging.info("*"*80)

        if len(armies) == 1:
            logging.info("Army %s with strategy '%s' is win!"%(armies[0].name, armies[0].strategy))
            print("Army %s with strategy %s is win!"%(armies[0].name, armies[0].strategy))
            print("Current time of battle is %s"%(start_game.duration_of_games()))
            logging.info("Current time of battle is %s"%(start_game.duration_of_games()))
            break                                  

     

if __name__ == "__main__":
    main()    