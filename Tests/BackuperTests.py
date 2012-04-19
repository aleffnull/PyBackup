__author__ = 'Mikhail K. Savkin'

from mock import patch
from os import rmdir, path
from unittest import main, TestCase
import tempfile

from Backuper import Backuper

class RunTests(TestCase):

	def test_NoRepo_Error(self):
		backuper = Backuper(None)
		self.assertRaises(ValueError, backuper.run)

	def test_NotGitRepo_Error(self):
		emptyDir = tempfile.mkdtemp()
		try:
			backuper = Backuper(emptyDir)
			self.assertRaises(ValueError, backuper.run)
		finally:
			rmdir(emptyDir)

	def test_GitRepo_Success(self):
		repoPath = self.__getGitRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_GitRepo_NoTempDir_TempDirIsCleaned(self):
		tempDir = tempfile.mkdtemp()
		self.assertTrue(path.exists(tempDir))

		repoPath = self.__getGitRepoPath()
		with patch('tempfile.mkdtemp') as mkdtemp_mock:
			mkdtemp_mock.return_value = tempDir
			backuper = Backuper(repoPath)
			backuper.run()

		mkdtemp_mock.assert_called_once_with()
		self.assertFalse(path.exists(tempDir))

	def __getGitRepoPath(self):
		currentDir = path.dirname(path.abspath(__file__))
		repoPath = path.join(currentDir, "repo.git")

		return repoPath

if __name__ == '__main__':
	main()
