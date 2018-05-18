from abc import ADCMeta

class Unit(metaclass=ABCMeta):
	def __init__(self, health = 100, recharge, attack_success = None, damage = None, time_recharge = None):
		self._health = health
		self.recharge = recharge
		self._attack_success = attack_success
		self._damage = damage
		self.time_recharge = time_recharge

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


	def is_reacharge(self):
		if self.time_reacharge:
			if clock.is_time(self.time_reacharge):
				return True
		return False

	
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

	@abstractmethod
	def damage_received(self, damage)::
	    pass	    	    	


		