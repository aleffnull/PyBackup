__author__ = 'Mikhail K. Savkin'

from unittest import main

from BaseLoggingTestCase import BaseLoggingTestCase
from DirectoryUtils import GetFullAbsolutePath, GetDirectoryName

class GetFullAbsolutePathTests(BaseLoggingTestCase):

	def test_None_NoneReturned(self):
		result = GetFullAbsolutePath(None)
		self.assertIsNone(result)

	def test_ResultIsNotEmpty(self):
		result = GetFullAbsolutePath(".")
		self.assertNotEqual(len(result), 0)

	def test_CurrentDirectory_IsAbsolute(self):
		result = GetFullAbsolutePath(".")
		self.assertFalse("." in result)

	def test_ParentDirectory_IsAbsolute(self):
		result = GetFullAbsolutePath("..")
		self.assertFalse(".." in result)

class GetDirectoryNameTests(BaseLoggingTestCase):

	def test_RelativePathSlash(self):
		result = GetDirectoryName("foo/")
		self.assertEqual(result, "foo")

	def test_RelativePathNoSlash(self):
		result = GetDirectoryName("foo")
		self.assertEqual(result, "foo")

	def test_AbsolutePathSlash(self):
		result = GetDirectoryName("/foo/")
		self.assertEqual(result, "foo")

	def test_AbsolutePathNoSlash(self):
		result = GetDirectoryName("/foo")
		self.assertEqual(result, "foo")

	def test_LongAbsolutePathSlash(self):
		result = GetDirectoryName("/foo/bar/buz")
		self.assertEqual(result, "buz")

if __name__ == '__main__':
	main()
