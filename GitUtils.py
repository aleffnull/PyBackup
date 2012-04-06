__author__ = 'Mikhail K. Savkin'

import os.path as path

def IsGitRepo(repoPath):
	isDir = path.isdir(repoPath)
	if not isDir:
		return False

	headFile = path.join(repoPath, "HEAD")
	isRepo = path.exists(headFile)

	return isRepo