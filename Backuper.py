__author__ = 'Mikhail K. Savkin'

from BackuperException import BackuperException
from os import path

class Backuper:
	def __init__(self, repoPath):
		self.__repoPath = path.normpath(path.abspath(repoPath))

	def run(self):
		self.__runChecks()
		print "Creating backup of repository '%s'" % self.__repoPath

		repoName = self.__getDirectoryName(self.__repoPath)
		print "Repository name is '%s'" % repoName

	def __runChecks(self):
		if not path.isdir(self.__repoPath):
			message = "path to repository should be an existing directory: %s" % self.__repoPath
			raise BackuperException(message)

	def __getDirectoryName(self, directoryPath):
		dummyFile = path.join(directoryPath, "dummy.txt")
		directory = path.dirname(dummyFile)
		directoryName = path.split(directory)[1]

		return directoryName
