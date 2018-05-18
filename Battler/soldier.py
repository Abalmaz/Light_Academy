from random import randint
from unit import Unit
from clock import Clock as clock

class Soldier(Unit):
    def __init__(self, health = 100, recharge = 100, experience = 0):
        self._health = health
        self._recharge = recharge
        self._attack_success = None
        self._damage = None
        self.time_recharge = None
        self._experience = experience

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
        if value < 100:
            self._recharge = 100
        elif value > 2000:
            self._recharge = 2000
        else:
            self._recharge = value

    @reacharge.getter
    def reacharge(self):
        return self._recharge

    experience = property()

    @experience.setter
    def experience(self, value):
        if 0 <= value <= 50:
            self._experience = value
        else:
            self._experience = 0

    @experience.getter
    def experience(self):
        return self._experience

    @property
    def attack_success(self):
        self._attack_success = 0.5 * (1 + self.health / 100) * randint(50 + self.experience, 100) / 100
        return self._attack_success

    @property
    def damage(self):
        self._damage = 0.05 + self.experience / 100
        return self._damage

    def is_live(self):
        if self.health == 0:
            return False
        return True


    def damage_received(self, damage):
        self.health -= damage
        self.time_recharge = clock.set_time(self.reacharge)


    def is_reacharge(self):
        if self.time_reacharge:
            if clock.is_time(self.time_reacharge):
                return True
        return False


                                        