import os
from divisibility import app
from StringIO import StringIO
import unittest

class TestViews(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_showed(self):
        response = self.app.get('/')
        self.assertTrue(b'Please select the data file for the problem' in response.data)

    def test_invalid_index_potato(self):
        response = self.app.get('/')
        self.assertTrue(not 'potato' in response.data)

    def test_file_upload(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('1\n7 2 4'), 'valid_input.txt'),
            }
        )
        self.assertTrue('2  6' in resp.data)

    def test_invalid_file_extension_upload(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('1\n7 2 4'), 'valid_input.exe'),
            }
        )
        self.assertTrue('The provided file has an invalid format' in resp.data)

    def test_invalid_input_size_file(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('1000000000\n7 2 4\n'), 'valid_input.txt'),
            }
        )
        self.assertTrue('Number of entries bigger than the allowed maximum' in resp.data)

    def test_input_size_mismatch_file(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('2\n7 2 4\n'), 'valid_input.txt'),
            }
        )
        self.assertTrue('Mismatch between informed and actual number of entries' in resp.data)

    def test_entry_size_file(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('1\n7 2 4 5\n'), 'valid_input.txt'),
            }
        )
        self.assertTrue('Invalid entry size' in resp.data)

    def test_entry_range_file(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('1\n7 10 4\n'), 'valid_input.txt'),
            }
        )
        self.assertTrue('Invalid entry range' in resp.data)

    def test_entry_type_file(self):
        client = app.test_client()
        resp = client.post(
            '/upload',
            data = {
                'file': (StringIO('1\n7 2.85 4\n'), 'valid_input.txt'),
            }
        )
        self.assertTrue('Invalid input format' in resp.data)




if __name__ == '__main__':
    unittest.main()
