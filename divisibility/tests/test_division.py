import unittest
from ..division import *

class TestDivision(unittest.TestCase):
	def test_divisible1(self):
		self.assertTrue(is_divisible(10,10))

	def test_divisible2(self):
		self.assertTrue(is_divisible(10,2))

	def test_not_divisible1(self):
		self.assertTrue(not is_divisible(3,2))

	def test_not_divisible2(self):
		self.assertTrue(not is_divisible(10,3))

	def test_divide_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			is_divisible(10,0)

	def test_get_divisible1(self):
		self.assertTrue(get_divisible(7,2,4) == [2,6])

	def test_get_divisible2(self):
		self.assertTrue(get_divisible(35,5,12) == range(5,35,5))

	def test_stress(self):
		self.assertTrue(len(get_divisible(99999,2,3)) == 33333)

if __name__ == '__main__':
    unittest.main()
