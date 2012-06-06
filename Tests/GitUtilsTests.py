__author__ = 'Mikhail K. Savkin'

from os import mkdir, rmdir
from os.path import join
from shutil import rmtree
from tempfile import mkdtemp, NamedTemporaryFile
from unittest import main, TestCase

from BaseRepoTestCase import BaseRepoTestCase
from GitUtils import GetRepoName, IsGitRepo

class IsGitRepoTests(BaseRepoTestCase):

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

	def test_EmptyBareRepository_NotRepo(self):
		dir = mkdtemp()
		try:
			emptyRepo = join(dir, "repo.git")
			mkdir(emptyRepo)
			result = IsGitRepo(emptyRepo)
			self.assertFalse(result)
		finally:
			rmtree(dir)

	def test_EmptyCommonRepository_NotRepo(self):
		dir = mkdtemp()
		try:
			emptyRepo = join(dir, ".git")
			mkdir(emptyRepo)
			result = IsGitRepo(emptyRepo)
			self.assertFalse(result)
		finally:
			rmtree(dir)

	def test_BareRepo_IsRepo(self):
		path = super(self.__class__, self)._getBareRepoPath()
		result = IsGitRepo(path)
		self.assertTrue(result)

	def test_CommonRepo_IsRepo(self):
		path = super(self.__class__, self)._getCommonRepoPath()
		result = IsGitRepo(path)
		self.assertTrue(result)

class GetRepoNameTests(TestCase):

	def test_NoneDirectory_ValueError(self):
		self.assertRaises(ValueError, GetRepoName, None)

	def test_EmptyDirectoryName_ValueError(self):
		self.assertRaises(ValueError, GetRepoName, "")

	def test_CommonRepoName_SameNameReturned(self):
		repoName = GetRepoName("repo")
		self.assertEqual(repoName, "repo")

	def test_BareRepoName_GitSuffixStripped(self):
		repoName = GetRepoName("repo.git")
		self.assertEqual(repoName, "repo")

if __name__ == '__main__':
	main()
