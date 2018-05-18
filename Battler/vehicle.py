from random import randint
from unit import Unit
from soldier import Soldier

class Vehicle(Unit):
	def __init__(self, health, reacharge, attack_success = None, damage = None, count_operators = 3)
	    super().__init__(_health, reacharge, _attack_success, _damage)
	    self.count_operators = count_operators
	    self.operators = [Soldier() for _ in range count_operators]
	    self._total_health


	@property
	def total_health(self):
		sum_health_of_operators = 0
		for operator in self.operators:
			sum_health_of_operators += operator.health
		self._total_health = (sum_health_of_operators + self.health) / self.count_operators + 1
		return self._total_health	

	
	@property
	def attack_success(self):
		self._attack_success = 0.5 * (1 + self.health / 100) * gavg(operators.attack_success)
	    return self._attack_success

	@property
	def damage(self):
		self._damage = 0.1 + sum(operators.experience / 100)
	    return self._damage

	def is_live(self):
		if self.count_operators and self.health:
			return True
	    return False

	def check_operators(self):
		'''
		если у одного из операторов жизнь = 0 то count_operators -= 1
		проверяем после каждой атаки
		'''

	def damage_received(self, damage):
	    '''
	    60% of the total damage is inflicted on the vehicle
		20% of the total damage is inflicted on a random vehicle operator
		The rest of the damage is inflicted evenly to the other operators (10% each)
	    '''	
       