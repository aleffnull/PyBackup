__author__ = 'Mikhail K. Savkin'

import unittest
from DirectoryUtils import GetFullAbsolutePath, GetDirectoryName

class GetFullPathTests(unittest.TestCase):
	def testIsNotEmpty(self):
		result = GetFullAbsolutePath(".")
		self.assertNotEqual(len(result), 0)

	def testIsAbsoluteForCurrentDirectory(self):
		result = GetFullAbsolutePath(".")
		self.assertFalse("." in result)

	def testIsAbsoluteForParentDirectory(self):
		result = GetFullAbsolutePath("..")
		self.assertFalse(".." in result)

class GetDirectoryNameTests(unittest.TestCase):
	def testRelativePathSlash(self):
		result = GetDirectoryName("foo/")
		self.assertEqual(result, "foo")

	def testRelativePathNoSlash(self):
		result = GetDirectoryName("foo")
		self.assertEqual(result, "foo")

	def testAbsolutePathSlash(self):
		result = GetDirectoryName("/foo/")
		self.assertEqual(result, "foo")

	def testAbsolutePathNoSlash(self):
		result = GetDirectoryName("/foo")
		self.assertEqual(result, "foo")

	def testLongAbsolutePathSlash(self):
		result = GetDirectoryName("/foo/bar/buz")
		self.assertEqual(result, "buz")

if __name__ == '__main__':
	unittest.main()
