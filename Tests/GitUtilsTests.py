__author__ = 'Mikhail K. Savkin'

import unittest
from os import rmdir, path
from shutil import rmtree
from tempfile import mkdtemp

from GitUtils import IsGitRepo

class IsGitRepoTests(unittest.TestCase):

	def test_EmptyDirectory_NotRepo(self):
		emptyDir = mkdtemp()
		try:
			result = IsGitRepo(emptyDir)
			self.assertFalse(result)
		finally:
			rmdir(emptyDir)

	def test_HeadFilePresent_IsRepo(self):
		dir = mkdtemp()
		try:
			headFile = path.join(dir, "HEAD")
			open(headFile, "w").close()
			result = IsGitRepo(dir)
			self.assertTrue(result)
		finally:
			rmtree(dir)

if __name__ == '__main__':
	unittest.main()
