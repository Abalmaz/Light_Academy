from unit import Unit
from soldier import Soldier
from vehicle import Vehicle
from clock import Clock as clock
from harmonic_mean import harmonic_mean

class Squad(Unit):
    def __init__(self, types, count_units, units):
        self.count_units = count_units
        self.type = types
        self.units = units
        self._attack_success = 0.0
        self._damage = 0

    
    @property
    def attack_success(self):
        units_attack = []        
        for n in range(self.count_units):
            units_attack.append(self.units[n].attack_success)           
        self._attack_success = harmonic_mean(units_attack)  
        return self._attack_success

    @property
    def damage(self):
        unit_damage = 0
        for n in range(self.count_units):
            unit_damage += self.units[n].damage
        self._damage = unit_damage
        return self._damage 

    def check_units(self):
        for n in range(self.count_units):
            if self.units[n].is_live() == False:
                del self.units[n]
                self.count_units -= 1

    def is_live(self):
        check_units(self)
        if self.count_units > 0:
            return True
        return False

    def damage_received(self, damage):
        '''
        The damage received on a successful attack is distributed evenly to all squad members.
        set time_reacharge
        '''
        damage_part = damage / self.count_units

        for n in range(self.count_units):
            self.count_units[n].damage_received(damage_part)

        self.check_units()  

                    
