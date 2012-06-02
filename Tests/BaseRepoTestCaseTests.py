__author__ = 'Mikhail K. Savkin'

from os.path import exists
from unittest import main
from BaseRepoTestCase import BaseRepoTestCase

class GetBareRepoPathTests(BaseRepoTestCase):

	def test_Exists(self):
		bareRepoPath = super(GetBareRepoPathTests, self)._getBareRepoPath()
		self.assertTrue(exists(bareRepoPath))

class GetCommonRepoPathTests(BaseRepoTestCase):

	def test_Exists(self):
		commonRepoPath = super(GetCommonRepoPathTests, self)._getCommonRepoPath()
		self.assertTrue(exists(commonRepoPath))

if __name__ == '__main__':
	main()
