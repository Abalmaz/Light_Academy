from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
from clock import Clock as clock

class Army:
    def __init__(self, name, strategy, squads):
        self.name = name
        self.strategy = strategy
        self.squads = squads

    	    