import unittest
from unittest import mock
from hash import hash_md5

class MD5TestCase(unittest.TestCase):
	@mock.patch('hash.md5')
	def test_some(self, mock_md5):
		hash_md5('Some string')
		mock_md5.assert_called_with('Some string'.encode())
