from unit import Unit
from soldier import Soldier
from vehicle import Vehicle

from harmonic_mean import harmonic_mean

class Squad(Unit):
    def __init__(self, types, units):
        self.type = types
        self.units = units
        self._attack_success = 0
        self._damage = 0

    
    @property
    def attack_success(self):
        units_attack = []        
        for unit in self.units:
            if unit.is_recharge():
                units_attack.append(unit.attack_success)           
        self._attack_success = harmonic_mean(units_attack) if units_attack else 0 
        return self._attack_success

    @property
    def damage(self):
        unit_damage = 0
        for unit in self.units:
            unit_damage += unit.damage
        self._damage = unit_damage
        return self._damage 

    def check_units(self):
        for n, unit in enumerate(self.units):
            if unit.is_live() == False:
                del self.units[n]

    def is_live(self):
        self.check_units()
        if len(self.units) > 0:
            return True 
        return False

    def damage_received(self, damage):
        '''
        The damage received on a successful attack is distributed evenly to all squad members.
        set time_recharge
        '''
        damage_part = damage / len(self.units)

        for unit in self.units:
            unit.damage_received(damage_part)


                    
