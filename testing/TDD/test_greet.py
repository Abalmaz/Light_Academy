import unittest
from unittest.mock import Mock, patch
from greeter import Greeter

class TestClassGreeter(unittest.TestCase):
	@patch('greeter.datetime')		
	def test_greet(self, mock_time):
		mock_time.now.return_value.hour = 20
		self.assertEqual(Greeter.greet("Ivan"), "Добрый вечер Ivan")

	@patch('greeter.datetime')	
	def test_trim(self, mock_time):
		mock_time.now.return_value.hour = 20
	    self.assertEqual(Greeter.greet("  Ivan  "), "Добрый вечер Ivan")

	@patch('greeter.datetime')
	def test_upper(self, mock_time):
	    self.assertEqual(Greeter.greet("ivan"), "Добрый вечер Ivan")

	@patch('greeter.datetime')
	def test_good_morning(self, mock_time):
		mock_time.now.return_value.hour = 7
		self.assertEqual(Greeter.greet("Ivan"), "Доброе утро Ivan")

	@patch('greeter.datetime')
	def test_good_evening(self, mock_time):
		mock_time.now.return_value.hour = 20
		self.assertEqual(Greeter.greet("Ivan"), "Добрый вечер Ivan")	

	@patch('greeter.datetime')
	def test_good_night(self, mock_time):
		mock_time.now.return_value.hour = 23
		self.assertEqual(Greeter.greet("Ivan"), "Доброй ночи Ivan")		  		    		

