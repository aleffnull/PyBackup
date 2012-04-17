__author__ = 'Mikhail K. Savkin'

from os import rmdir, path
from tempfile import mkdtemp
from unittest import main, TestCase

from Backuper import Backuper

class MyTestCase(TestCase):

	def test_run_NoRepo(self):
		backuper = Backuper(None, None)
		self.assertRaises(ValueError, backuper.run)

	def test_run_NotGitRepo(self):
		emptyDir = mkdtemp()
		try:
			backuper = Backuper(repoPath=emptyDir, tempDir=None)
			self.assertRaises(ValueError, backuper.run)
		finally:
			rmdir(emptyDir)

	def test_run_GitRepo(self):
		currentDir = path.dirname(path.abspath(__file__))
		testRepo = path.join(currentDir, "repo.git")
		backuper = Backuper(repoPath=testRepo, tempDir=None)
		backuper.run()

if __name__ == '__main__':
	main()
