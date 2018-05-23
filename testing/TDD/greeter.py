from datetime import datetime

class Greeter:
	# def __init__(self, name):
	# 	self.name = name

	def greet(name):
		new_name = name.strip().capitalize()
		current_time = datetime.now().hour
		if 6 <= current_time <= 12:
			return "Доброе утро " + new_name
		elif 18 <= current_time <= 22:	  
			return "Добрый вечер " + new_name
		elif current_time < 6 or current_time > 22:
			return "Доброй ночи " + new_name

# greet = Greeter("Ivan")
# print(greet.greet()	)	
