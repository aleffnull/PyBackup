__author__ = 'Mikhail K. Savkin'

from mock import patch
from os import rmdir, path
from unittest import main, TestCase
import tempfile

from Backuper import Backuper

class MyTestCase(TestCase):

	def test_run_NoRepo(self):
		backuper = Backuper(None)
		self.assertRaises(ValueError, backuper.run)

	def test_run_NotGitRepo(self):
		emptyDir = tempfile.mkdtemp()
		try:
			backuper = Backuper(emptyDir)
			self.assertRaises(ValueError, backuper.run)
		finally:
			rmdir(emptyDir)

	def test_run_GitRepo(self):
		repoPath = self.__getGitRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_run_TempGitIsCleaned(self):
		tempDir = tempfile.mkdtemp()
		self.assertTrue(path.exists(tempDir))

		repoPath = self.__getGitRepoPath()
		with patch('tempfile.mkdtemp') as mkdtemp_mock:
			mkdtemp_mock.return_value = tempDir
			backuper = Backuper(repoPath)
			backuper.run()

		self.assertFalse(path.exists(tempDir))

	def __getGitRepoPath(self):
		currentDir = path.dirname(path.abspath(__file__))
		repoPath = path.join(currentDir, "repo.git")

		return repoPath

if __name__ == '__main__':
	main()
