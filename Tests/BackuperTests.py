__author__ = 'Mikhail K. Savkin'

from mock import patch
from os import rmdir, path
from shutil import rmtree
from tempfile import mkdtemp
from unittest import main

from Backuper import Backuper
from BaseRepoTestCase import BaseRepoTestCase

class RunTests(BaseRepoTestCase):

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

	def test_BareGitRepo_Success(self):
		repoPath = super(self.__class__, self)._getBareRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_CommonGitRepo_Success(self):
		repoPath = super(self.__class__, self)._getCommonRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_BareGitRepo_NoTempDir_TempDirIsCleaned(self):
		tempDir = mkdtemp()
		self.assertTrue(path.exists(tempDir))

		repoPath = super(self.__class__, self)._getBareRepoPath()
		with patch('tempfile.mkdtemp') as mkdtemp_mock:
			mkdtemp_mock.return_value = tempDir
			backuper = Backuper(repoPath)
			backuper.run()

		mkdtemp_mock.assert_called_once_with()
		self.assertFalse(path.exists(tempDir))

	def test_BareGitRepo_GotTempDir_NoTempDirCreated(self):
		repoPath = super(self.__class__, self)._getBareRepoPath()
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
