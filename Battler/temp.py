from soldier import Soldier
from random import randint
from clock import Clock as clock

class Vehicle():
	def __init__(self, health, count_operator, recharge):
		self.health = health
		self.count_operator = count_operator
		self.recharge = recharge
		self.operators = [Soldier() for _ in range (count_operator)]
		self.time_reacharge = None


	def check_operators(self):
		for n in range(self.count_operator):
			if self.operators[n].is_live() == False:
				del self.operators[n]
				self.count_operator -= 1

	def damage_received(self, damage):
		'''
		60% of the total damage is inflicted on the vehicle
		20% of the total damage is inflicted on a random vehicle operator
		The rest of the damage is inflicted evenly to the other operators (10% each)
		set time_reacharge
		'''
		self.health -= damage * 0.2

		range_operator = randint(0, self.count_operator - 1)
		for n in range(self.count_operator):
			if self.count_operator == 3:
				if range_operator == n:
					self.operators[n].damage_received(damage * 0.9)
				else:
					self.operators[n].damage_received(damage * 0.1)
			elif self.count_operator == 2:
				if range_operator == n:
					self.operators[n].damage_received(damage * 0.3)
				else:
					self.operators[n].damage_received(damage * 0.1)
			elif self.count_operator == 1:
				self.operators[n].damage_received(damage * 0.4)

		self.time_recharge = clock.set_time(self.recharge)
		print("health of vehicle: {}".format(self.health))
		for n, operator in enumerate(self.operators):
			print("health of operator {}: {}".format(n, operator.health))

		self.check_operators()	



vehicle = Vehicle(100, 2, 100)
vehicle.damage_received(100)

for n in range(vehicle.count_operator):
	print(vehicle.operators[n].health)

vehicle.damage_received(100)

for n in range(vehicle.count_operator):
	print(vehicle.operators[n].health)

print(vehicle.count_operator)		
	          