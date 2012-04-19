__author__ = 'Mikhail K. Savkin'

from logging import getLogger
from shutil import rmtree
import tempfile

from DirectoryUtils import GetDirectoryName, GetFullAbsolutePath
from GitUtils import IsGitRepo

class Backuper:

	def __init__(self, repoPath, tempDir=None):
		self.__log = getLogger(__name__)
		self.__repoPath = GetFullAbsolutePath(repoPath)
		self.__tempDir = tempDir

	def run(self):
		self.__runChecks()
		self.__log.info("Creating backup of repository '%s'" % self.__repoPath)
		repoName = GetDirectoryName(self.__repoPath)
		self.__log.info("Repository name is '%s'" % repoName)

		removeTempDir = self.__tempDir is None
		tempDir = tempfile.mkdtemp() if self.__tempDir is None else self.__tempDir

		try:
			self.__doBackup(tempDir)
		finally:
			if removeTempDir:
				rmtree(tempDir)

	def __runChecks(self):
		if self.__repoPath is None:
			raise ValueError("Path to repository is required")

		isRepo = IsGitRepo(self.__repoPath)
		if not isRepo:
			raise ValueError("'%s' is not Git repository" % self.__repoPath)

	def __doBackup(self, tempDir):
		pass
