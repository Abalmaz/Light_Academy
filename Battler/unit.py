from abc import ABCMeta

class Unit(metaclass = ABCMeta):
	
	@abstractmethod
	def attack(self, target):
		pass
    
    def take_demage(self, dmg):
    	pass

    @property
    @abstractmethod
    def alive(self):
        pass

    def healf(self):
        pass

    def attack_power(self):
        pass        	