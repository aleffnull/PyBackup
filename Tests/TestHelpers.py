__author__ = 'Mikhail K. Savkin'

from os.path import abspath, dirname, join

def GetBareRepoPath():
	path = __getFullPath("repo.git")
	return path


def GetCommonRepoPath():
	path = __getFullPath("repo")
	return path

def __getFullPath(path):
	currentDir = dirname(abspath(__file__))
	fullPath = join(currentDir, path)

	return fullPath