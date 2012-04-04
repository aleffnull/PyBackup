__author__ = 'Mikhail K. Savkin'

from os import path

def GetFullAbsolutePath(relativePath):
	return path.normpath(path.abspath(relativePath))

def GetDirectoryName(directoryPath):
	dummyFile = path.join(directoryPath, "dummy.txt")
	directory = path.dirname(dummyFile)
	directoryName = path.split(directory)[1]

	return directoryName