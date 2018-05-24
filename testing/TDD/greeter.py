from datetime import datetime
import logging

class Greeter:
	def __init__(self, name):
		self.name = name

	def greet(name):
		new_name = name.strip().capitalize()
		current_time = datetime.now().hour
		greeting = ""
		if 6 <= current_time <= 12:
			greeting = "Доброе утро " + new_name
		elif 18 <= current_time <= 22:	  
			greeting = "Добрый вечер " + new_name
		elif current_time < 6 or current_time > 22:
			greeting = "Доброй ночи " + new_name

		logging.info('You greeting with {}'.format(new_name))
			
		return greeting	
