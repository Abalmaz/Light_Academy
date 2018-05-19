from random import randint
from unit import Unit
from soldier import Soldier
from clock import Clock as clock
from harmonic_mean import harmonic_mean


class Vehicle(Unit):
    def __init__(self, health, reacharge, count_operators, operators):
        self._health = health
        self._reacharge = reacharge
        self._attack_success = 0
        self._damage = 0
        self.count_operators = count_operators
        self.operators = operators
        self._total_health = 0
        self.time_reacharge = 0

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

    reacharge = property()
    
    @reacharge.setter
    def reacharge(self, value):
        if value < 1000:
            self._recharge = 1000
        elif value > 2000:
            self._recharge = 2000
        else:
            self._recharge = value

    @reacharge.getter
    def reacharge(self):
        return self._recharge       


    @property
    def total_health(self):
        sum_health_of_operators = 0
        for n in range(self.count_operators):
            sum_health_of_operators += self.operators[n].health
        self._total_health = (sum_health_of_operators + self.health) /(self.count_operators + 1)
        return self._total_health   

    
    @property
    def attack_success(self):
        operators_attack = []
        for n in range(self.count_operators):
            operators_attack.append(self.operators[n].attack_success)            
        operator_attack_succes = harmonic_mean(operators_attack)   
        self._attack_success = 0.5 * (1 + self.health / 100) * operator_attack_succes
        return self._attack_success

    @property
    def damage(self):
        operators_experience = 0
        for n in range(self.count_operators):
            operators_experience += self.operators[n].experience / 100
        self._damage = 0.1 + operators_experience 
        return self._damage

    def is_live(self):
        if self.count_operators >= 0 and self.health > 0:
            return True
        return False

    def check_operators(self):
        '''
        если у одного из операторов жизнь = 0 то count_operators -= 1
        проверяем после каждой атаки
        '''
        for n in range(self.count_operators):
            if self.operators[n].is_live() == False:
                del self.operators[n]
                self.count_operators -= 1

    def damage_received(self, damage):
        '''
        60% of the total damage is inflicted on the vehicle
        20% of the total damage is inflicted on a random vehicle operator
        The rest of the damage is inflicted evenly to the other operators (10% each)
        set time_reacharge
        check operators
        '''
        self.health -= damage * 0.6

        range_operator = randint(0, self.count_operators - 1)
        for n in range(self.count_operators):
            if count_operators == 3:
                if range_operator == n:
                    self.operators[n].damage_received(damage * 0.2)
                else:
                    self.operators[n].damage_received(damage * 0.1)
            elif count_operators == 2:
                if range_operator == n:
                    self.operators[n].damage_received(damage * 0.3)
                else:
                    self.operators[n].damage_received(damage * 0.2)
            else:
                self.operators[n].damage_received(damage * 0.4)

        self.time_recharge = clock.set_time(self.reacharge)
        self.check_operators() 

    def is_reacharge(self):
        if self.time_reacharge:
            if clock.is_time(self.time_reacharge):
                return True
        return False                            
       