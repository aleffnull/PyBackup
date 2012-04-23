__author__ = 'Mikhail K. Savkin'

from TestHelpers import GetBareRepoPath, GetCommonRepoPath

from os.path import exists
from unittest import main, TestCase

class GetBareRepoPathTests(TestCase):

	def test_pathExists(self):
		path = GetBareRepoPath()
		result = exists(path)

		self.assertTrue(result)

class GetCommonRepoPathTests(TestCase):

	def test_pathExists(self):
		path = GetCommonRepoPath()
		result = exists(path)

		self.assertTrue(result)

if __name__ == '__main__':
	main()
