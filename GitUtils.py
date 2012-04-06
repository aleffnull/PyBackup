__author__ = 'Mikhail K. Savkin'

from os import path

def IsGitRepo(repoPath):
	headFile = path.join(repoPath, "HEAD")
	isRepo = path.exists(headFile)

	return isRepo