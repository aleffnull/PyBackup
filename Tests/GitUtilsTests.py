__author__ = 'Mikhail K. Savkin'

from os import path, rmdir
from shutil import rmtree
from tempfile import mkdtemp, NamedTemporaryFile
from unittest import main, TestCase

from GitUtils import IsGitRepo

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
	main()
