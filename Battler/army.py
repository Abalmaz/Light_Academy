from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
# from clock import Clock as clock

class Army:
    def __init__(self, name, strategy, squads):
        self.name = name
        self.strategy = strategy
        self.squads = squads

    def check_squads(self):
        for n, squad in enumerate(self.squads):
            if squad.is_live() == False: 
                del self.squads[n]

    def is_live(self):
        self.check_squads()
        return True if len(self.squads) > 0 else False             

    	    