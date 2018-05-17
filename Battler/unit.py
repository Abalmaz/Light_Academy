from abc import ADCMeta

class Unit(metaclass=ABCMeta):
	def __init__(self, health = 100, recharge, attack_success = None, damage = None):
		self.health = health
		self.recharge = recharge
		self._attack_success = attack_success
		self._damage = damage

	@property
	@abstractmethod
	def attack_success(self):
		pass

	@property
	@abstractmethod
	def damage(self):
		pass

	@abstractmethod
	def is_live(self):
	    pass	


		