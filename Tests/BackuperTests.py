__author__ = 'Mikhail K. Savkin'

from mock import patch
from os import rmdir, path
from shutil import rmtree
from tempfile import mkdtemp
from unittest import main, TestCase

from Backuper import Backuper
from TestHelpers import GetBareRepoPath

class RunTests(TestCase):

	def test_NoRepo_Error(self):
		backuper = Backuper(None)
		self.assertRaises(ValueError, backuper.run)

	def test_NotGitRepo_Error(self):
		emptyDir = mkdtemp()
		try:
			backuper = Backuper(emptyDir)
			self.assertRaises(ValueError, backuper.run)
		finally:
			rmdir(emptyDir)

	def test_GitRepo_Success(self):
		repoPath = GetBareRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_GitRepo_NoTempDir_TempDirIsCleaned(self):
		tempDir = mkdtemp()
		self.assertTrue(path.exists(tempDir))

		repoPath = GetBareRepoPath()
		with patch('tempfile.mkdtemp') as mkdtemp_mock:
			mkdtemp_mock.return_value = tempDir
			backuper = Backuper(repoPath)
			backuper.run()

		mkdtemp_mock.assert_called_once_with()
		self.assertFalse(path.exists(tempDir))

	def test_GitRepo_GotTempDir_NoTempDirCreated(self):
		repoPath = GetBareRepoPath()
		tempDir = mkdtemp()
		try:
			with patch('tempfile.mkdtemp') as mkdtemp_mock:
				backuper = Backuper(repoPath, tempDir)
				backuper.run()

			self.assertFalse(mkdtemp_mock.called)
		finally:
			rmtree(tempDir)

if __name__ == '__main__':
	main()
