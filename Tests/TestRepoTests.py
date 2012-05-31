__author__ = 'Mikhail K. Savkin'

from unittest import main
from BaseRepoTestCase import BaseRepoTestCase

class GetBareRepoPathTests(BaseRepoTestCase):

	def test_Exists(self):
		print super(GetBareRepoPathTests, self)._getBareRepoPath()

class GetCommonRepoPathTests(BaseRepoTestCase):

	def test_Exists(self):
		print super(GetCommonRepoPathTests, self)._getCommonRepoPath()

if __name__ == '__main__':
	main()
