import unittest
from ..validator import *

class TestValidator(unittest.TestCase):
	def test_valid_range(self):
		self.assertTrue(valid_range(1,2,10))

	def test_invalid_range1(self):
		self.assertTrue(not valid_range(1,20,10))

	def test_invalid_range2(self):
		self.assertTrue(not valid_range(20,1,10))

	def test_mismatched_input_size(self):
		with self.assertRaises(InputError):
			validate(2,[[7,2,4]])

	def test_exceeded_max_input_size(self):
		with self.assertRaises(InputError):
			validate(100,[[]]*100)

	def test_invalid_entry_size1(self):
		with self.assertRaises(InputError):
			validate(1,[[7,2]])

	def test_invalid_entry_size2(self):
		with self.assertRaises(InputError):
			validate(1,[[7,2,3,4]])

	def test_invalid_entry_range1(self):
		with self.assertRaises(InputError):
			validate(1,[[-1,2,3]])

	def test_invalid_entry_range2(self):
		with self.assertRaises(InputError):
			validate(1,[[10000000,2,3]])

	def test_invalid_entry_range3(self):
		with self.assertRaises(InputError):
			validate(1,[[1,10,3]])

	def test_invalid_entry_range4(self):
		with self.assertRaises(InputError):
			validate(1,[[1,-1,3]])

	def test_invalid_entry_range5(self):
		with self.assertRaises(InputError):
			validate(1,[[1,3,10]])

	def test_invalid_entry_range6(self):
		with self.assertRaises(InputError):
			validate(1,[[1,3,-1]])

if __name__ == '__main__':
    unittest.main()
