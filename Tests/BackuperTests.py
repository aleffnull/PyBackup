__author__ = 'Mikhail K. Savkin'

from os import rmdir
from tempfile import mkdtemp
from unittest import main, TestCase

from Backuper import Backuper

class MyTestCase(TestCase):

	def test_runNotGitRepo(self):
		emptyDir = mkdtemp()
		try:
			backuper = Backuper(emptyDir)
			self.assertRaises(ValueError, backuper.run)
		finally:
			rmdir(emptyDir)

if __name__ == '__main__':
	main()
