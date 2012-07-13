__author__ = 'Mikhail K. Savkin'

from mock import patch
from os import listdir, rmdir, path
from shutil import rmtree
from tempfile import mkdtemp
from unittest import main

from Backuper import Backuper
from BaseRepoTestCase import BaseRepoTestCase

@patch('Backuper.ProcessRunner')
class RunTests(BaseRepoTestCase):

	def test_NoRepo_Error(self, processRunnerMock):
		backuper = Backuper(None)
		self.assertRaises(ValueError, backuper.run)

	def test_NotGitRepo_Error(self, processRunnerMock):
		emptyDir = mkdtemp()
		try:
			backuper = Backuper(emptyDir)
			self.assertRaises(ValueError, backuper.run)
		finally:
			rmdir(emptyDir)

	def test_BareGitRepo_Success(self, processRunnerMock):
		repoPath = super(self.__class__, self)._getBareRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_CommonGitRepo_Success(self, processRunnerMock):
		repoPath = super(self.__class__, self)._getCommonRepoPath()
		backuper = Backuper(repoPath)
		backuper.run()

	def test_BareGitRepo_NoTempDir_TempDirIsCleaned(self, processRunnerMock):
		tempDir = mkdtemp()
		self.assertTrue(path.exists(tempDir))

		repoPath = super(self.__class__, self)._getBareRepoPath()
		with patch('tempfile.mkdtemp') as mkdtemp_mock:
			mkdtemp_mock.return_value = tempDir
			backuper = Backuper(repoPath)
			backuper.run()

		mkdtemp_mock.assert_called_once_with()
		self.assertFalse(path.exists(tempDir))

	def test_BareGitRepo_GotTempDir_NoTempDirCreated(self, processRunnerMock):
		repoPath = super(self.__class__, self)._getBareRepoPath()
		tempDir = mkdtemp()
		try:
			with patch('tempfile.mkdtemp') as mkdtemp_mock:
				backuper = Backuper(repoPath, tempDir)
				backuper.run()

			self.assertFalse(mkdtemp_mock.called)
		finally:
			rmtree(tempDir)

	def test_BareGitRepo_GotTempDir_TempDirIsCleaned(self, processRunnerMock):
		repoPath = super(self.__class__, self)._getBareRepoPath()
		tempDir = mkdtemp()
		try:
			backuper = Backuper(repoPath, tempDir)
			backuper.run()

			tempDirContents = listdir(tempDir)
			self.assertEqual(len(tempDirContents), 0)
		finally:
			rmtree(tempDir)

	def test_BareGitRepo_GitIsNotAccessible_Error(self, processRunnerMock):
		processRunnerMock.side_effect = RuntimeError("foo")

		repoPath = super(self.__class__, self)._getBareRepoPath()
		backuper = Backuper(repoPath)
		self.assertRaises(RuntimeError, backuper.run)

if __name__ == '__main__':
	main()
