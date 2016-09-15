import tempfile
import unittest
from ..parser import *

class TestParser(unittest.TestCase):
	def test_valid_parse(self):
		self.assertTrue(parse_line("7 2 4") == [7,2,4])

	def test_invalid_input_char(self):
		with self.assertRaises(ValueError):
			parse_line("7 a 4")

	def test_invalid_input_string(self):
		with self.assertRaises(ValueError):
			parse_line("7 potato 4")

	def test_invalid_input_double(self):
		with self.assertRaises(ValueError):
			parse_line("7 2.4 4")

	def test_invalid_input_specialchar(self):
		with self.assertRaises(ValueError):
			parse_line("7 ! 4")

	def test_valid_file_reading(self):
		file_f = tempfile.TemporaryFile(mode='w+r')
		file_f.write('1\n7 2 4')
		file_f.seek(0)
		self.assertTrue(parse_file(file_f) == [[7,2,4]])
		file_f.close()

	def test_invalid_file_reading(self):
		file_f = tempfile.TemporaryFile(mode='w+r')
		file_f.write('1\na 2 4')
		file_f.seek(0)
		with self.assertRaises(InputError):
			parse_file(file_f)
		file_f.close()

	def test_empty_file(self):
		file_f = tempfile.TemporaryFile(mode='w+r')
		with self.assertRaises(InputError):
			parse_file(file_f)
		file_f.close()

if __name__ == '__main__':
    unittest.main()
