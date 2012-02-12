""" Backup local git repositories to CD on Windows """

__author__ = "Mikhail K. Savkin"

from optparse import OptionParser
from os import path

class BackuperException(Exception):
	def __init__(self, message, *args, **kwargs):
		super(BackuperException, self).__init__(*args, **kwargs)
		self.__message = message

	@property
	def message(self):
		return self.__message

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

def main():
	parser = OptionParser()
	parser.add_option("-r", "--repo", dest="repoPath", help="path to repository")
	(options, args) = parser.parse_args()

	if options.repoPath is None:
		parser.error("path to repository is required")

	backuper = Backuper(options.repoPath)
	try:
		backuper.run()
	except BackuperException as exception:
		print "Error occurred: %s" % exception.message

if __name__ == "__main__":
	main()