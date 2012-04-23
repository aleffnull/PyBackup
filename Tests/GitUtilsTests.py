__author__ = 'Mikhail K. Savkin'

from os import rmdir
from tempfile import mkdtemp, NamedTemporaryFile
from unittest import main, TestCase

from GitUtils import IsGitRepo
from TestHelpers import GetBareRepoPath, GetCommonRepoPath

class IsGitRepoTests(TestCase):

	def test_File_NotRepo(self):
		tempFile = NamedTemporaryFile()
		try:
			result = IsGitRepo(tempFile.name)
			self.assertFalse(result)
		finally:
			tempFile.close()

	def test_EmptyDirectory_NotRepo(self):
		emptyDir = mkdtemp()
		try:
			result = IsGitRepo(emptyDir)
			self.assertFalse(result)
		finally:
			rmdir(emptyDir)

	def test_BareRepo_IsRepo(self):
		path = GetBareRepoPath()
		result = IsGitRepo(path)
		self.assertTrue(result)

	def test_CommonRepo_IsRepo(self):
		path = GetCommonRepoPath()
		result = IsGitRepo(path)
		self.assertTrue(result)

if __name__ == '__main__':
	main()
