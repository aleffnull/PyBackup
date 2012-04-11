__author__ = 'Mikhail K. Savkin'

from unittest import main, TestCase
from DateUtils import GetTimestampAsFileName

class GetTimestampAsFileNameTests(TestCase):

	def test_NotEmpty(self):
		timestamp = GetTimestampAsFileName()
		self.assertIsNotNone(timestamp)
		self.assertNotEqual(timestamp, "")

	def test_Format(self):
		timestamp = GetTimestampAsFileName()
		self.assertRegexpMatches(timestamp, "\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}")

if __name__ == '__main__':
	main()
