from abc import ABCMeta
'''
класс для всех, счет времени для восстанавления
'''
class Clock:
    def __init__(self):
        self.i = i
    def tick(self):
        self.i += 1
    def time(self):
        return self.i    

class Unit(metaclass = ABCMeta):
	
    '''
      при аттаке приплюсовываем время для воостановления
      target.take_demage()
      self._recharge_to = self.clock.time()+1000
      активны все у кого recharge <= текущего времени   
    '''
    @abstractmethod
    def attack(self, target):
        pass
    
    @abstractmethod
    def take_demage(self, dmg):
        pass

    @property
    @abstractmethod
    def alive(self):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def attack_power(self):
        pass

    '''
    когда recharge == 0 можно аттаковать
    '''
    @property
    @abstractmethod
    def recharge(self):
        pass

    '''
    
    '''
                	