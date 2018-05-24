import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

	def test_empty_string(self):
		self.assertEqual(StringCalculator.add(''), 0)

	def test_single_number(self):
		self.assertEqual(StringCalculator.add('10'), 10)

	def test_if_separated_comma(self):
		self.assertEqual(StringCalculator.add('10,20'), 30)

	def test_if_separated_new_line(self):
		self.assertEqual(StringCalculator.add('1\n2'), 3)

	def test_more_two_numbers_with_diff_separate(self):
		self.assertEqual(StringCalculator.add('1\n2,3\n4'), 10)

	def test_negative_number(self):
		self.assertEqual(StringCalculator.add('-1,2,-3'), 'отрицательные числа запрещены: -1,-3')

	def test_ignore_number_more_1000(self):
		self.assertEqual(StringCalculator.add('1000, 2, 3'), 5)

	def test_one_char_separat(self):
		self.assertEqual(StringCalculator.add('//#\n1#2#3#1000'), 6)

	def test_multi_char_separat(self):
		self.assertEqual(StringCalculator.add('//###\n1###2###5'), 8)					