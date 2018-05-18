from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):  
    
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
    def damage_received(self, damage):
        pass


    @abstractmethod
    def is_reacharge(self):
        pass


        