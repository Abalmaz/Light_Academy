import time
from random import randint
from unit import Unit
from soldier import Soldier
import clock
from harmonic_mean import harmonic_mean


class Vehicle(Unit):
    def __init__(self, health, recharge, operators):
        self._health = health
        self._recharge = recharge
        self._attack_success = 0
        self._damage = 0
        self.operators = operators
        self._total_health = 0
        self.time_recharge = time.time()

    health = property()

    @health.setter
    def health(self, value):
        if value <= 0:
            self._health = 0
        elif value >= 100:
            self._health = 100
        else:
            self._health = value

    @health.getter
    def health(self):
        return self._health

    recharge = property()
    
    @recharge.setter
    def recharge(self, value):
        if value < 1000:
            self._recharge = 1000
        elif value > 2000:
            self._recharge = 2000
        else:
            self._recharge = value

    @recharge.getter
    def recharge(self):
        return self._recharge       


    @property
    def total_health(self):
        sum_health_of_operators = 0
        for operator in self.operators:
            sum_health_of_operators += operator.health
        self._total_health = (sum_health_of_operators + self.health) /len(self.operators)
        return self._total_health   

    
    @property
    def attack_success(self):
        operators_attack = []
        for operator in self.operators:
            operators_attack.append(operator.attack_success)            
        operator_attack_success = harmonic_mean(operators_attack)   
        self._attack_success = 0.5 * (1 + self.health / 100) * operator_attack_success
        return self._attack_success

    @property
    def damage(self):
        operators_experience = 0
        for operator in self.operators:
            operators_experience += operator.experience / 100
        self._damage = 0.1 + operators_experience 
        return self._damage

    def check_operators(self):
        for n, operator in enumerate(self.operators):
            if operator.is_live() == False:
                del self.operators[n]


    def is_live(self):
        self.check_operators()
        if len(self.operators) > 0 and self.health > 0:
            return True
        return False



    def damage_received(self, damage):
        '''
        60% of the total damage is inflicted on the vehicle
        20% of the total damage is inflicted on a random vehicle operator
        The rest of the damage is inflicted evenly to the other operators (10% each)
        set time_recharge
        check operators
        '''
        self.health -= damage * 0.6

        range_operator = randint(0, len(self.operators)-1)
        for n, operator in enumerate(self.operators):
            if len(self.operators) == 3:
                if range_operator == n:
                    operator.damage_received(damage * 0.2)
                else:
                    operator.damage_received(damage * 0.1)
            elif len(self.operators) == 2:
                if range_operator == n:
                    operator.damage_received(damage * 0.3)
                else:
                    operator.damage_received(damage * 0.2)
            else:
                operator.damage_received(damage * 0.4)


    def is_recharge(self):
        return clock.is_time(self.time_recharge)
                          
       