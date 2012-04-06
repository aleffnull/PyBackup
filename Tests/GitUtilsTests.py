__author__ = 'Mikhail K. Savkin'

import os
import shutil
import tempfile
import unittest

import GitUtils

class IsGitRepoTests(unittest.TestCase):

	def test_File_NotRepo(self):
		tempFile = tempfile.NamedTemporaryFile()
		try:
			result = GitUtils.IsGitRepo(tempFile.name)
			self.assertFalse(result)
		finally:
			tempFile.close()

	def test_EmptyDirectory_NotRepo(self):
		emptyDir = tempfile.mkdtemp()
		try:
			result = GitUtils.IsGitRepo(emptyDir)
			self.assertFalse(result)
		finally:
			os.rmdir(emptyDir)

	def test_HeadFilePresent_IsRepo(self):
		dir = tempfile.mkdtemp()
		try:
			headFile = os.path.join(dir, "HEAD")
			open(headFile, "w").close()
			result = GitUtils.IsGitRepo(dir)
			self.assertTrue(result)
		finally:
			shutil.rmtree(dir)

if __name__ == '__main__':
	unittest.main()
