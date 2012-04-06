__author__ = 'Mikhail K. Savkin'

from os import path

def IsGitRepo(repoPath):
	isDir = path.isdir(repoPath)
	if not isDir:
		return False

	headFile = path.join(repoPath, "HEAD")
	isRepo = path.exists(headFile)

	return isRepo