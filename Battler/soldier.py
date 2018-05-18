from random import randint
from unit import Unit
from clock import Clock as clock

class Soldier(Unit):
	def __init__(self, health, reacharge = None, attack_success = None, damage = None, time_reacharge = None, experince = 0):
		super().__init__(_health, reacharge, _attack_success, _damage, time_reacharge)
		self._experience = experience

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
	    return health


	def damage_received(self, damage):
	    self.health -= damage
		
	                         	    	