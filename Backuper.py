__author__ = 'Mikhail K. Savkin'

from BackuperException import BackuperException
from DirectoryUtils import GetFullAbsolutePath,GetDirectoryName
from os import path

class Backuper:

	def __init__(self, repoPath):
		self.__repoPath = GetFullAbsolutePath(repoPath)

	def run(self):
		self.__runChecks()
		print "Creating backup of repository '%s'" % self.__repoPath

		repoName = GetDirectoryName(self.__repoPath)
		print "Repository name is '%s'" % repoName

	def __runChecks(self):
		if not path.isdir(self.__repoPath):
			message = "path to repository should be an existing directory: %s" % self.__repoPath
			raise BackuperException(message)
