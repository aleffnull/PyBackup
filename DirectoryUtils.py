__author__ = 'Mikhail K. Savkin'

from os import path

def GetFullAbsolutePath(relativePath):
	if relativePath is None:
		return None

	absolutePath = path.abspath(relativePath)
	normPath = path.normpath(absolutePath)

	return normPath

def GetDirectoryName(directoryPath):
	dummyFile = path.join(directoryPath, "dummy.txt")
	directory = path.dirname(dummyFile)
	directoryName = path.split(directory)[1]

	return directoryName