__author__ = 'Mikhail K. Savkin'

from logging import getLogger

from DirectoryUtils import GetFullAbsolutePath
from GitUtils import IsGitRepo

class Backuper:

	def __init__(self, repoPath):
		self.__log = getLogger(__name__)
		self.__repoPath = GetFullAbsolutePath(repoPath)

	def run(self):
		isRepo = IsGitRepo(self.__repoPath)
		if not isRepo:
			self.__log.error("'%s' is not Git repository" % self.__repoPath)
			return

		self.__log.info("Creating backup of repository '%s'" % self.__repoPath)
