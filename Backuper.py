__author__ = 'Mikhail K. Savkin'

from logging import getLogger
from os import path
from shutil import rmtree
import tempfile

from DateUtils import GetTimestampAsFileName
from DirectoryUtils import GetDirectoryName, GetFullAbsolutePath
from GitUtils import GetRepoName, IsGitRepo
from ProcessRunner import ProcessRunner

class Backuper:

	def __init__(self, repoPath, tempDir=None):
		self.__log = getLogger(__name__)
		self.__repoPath = GetFullAbsolutePath(repoPath)
		self.__tempDir = tempDir

	def run(self):
		self.__runChecks()
		self.__log.info("Creating backup of repository '%s'" % self.__repoPath)

		removeTempDir = self.__tempDir is None
		tempDir = tempfile.mkdtemp() if self.__tempDir is None else self.__tempDir

		try:
			self.__doBackup(tempDir)
		finally:
			if removeTempDir:
				rmtree(tempDir)

	def __runChecks(self):
		# Path to repository must be specified.
		if self.__repoPath is None:
			raise ValueError("Path to repository is required")

		# Repository must be a Git repository.
		isRepo = IsGitRepo(self.__repoPath)
		if not isRepo:
			raise ValueError("'%s' is not Git repository" % self.__repoPath)

		# `git' command must be accessible.
		self.__log.debug("Checking `git' command availability")
		try:
			ProcessRunner("git", "--version")
		except:
			raise RuntimeError("`git' command is not accessible")
		self.__log.debug("`git' is available")

	def __doBackup(self, tempDir):
		directoryName = GetDirectoryName(self.__repoPath)
		repoName = GetRepoName(directoryName)
		timestamp = GetTimestampAsFileName()
		bundleName = "%s_%s.bundle" % (repoName, timestamp)
		bundlePath = path.join(tempDir, bundleName)

		self.__log.info("Creating bundle '%s'" % bundlePath)
