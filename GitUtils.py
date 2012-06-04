__author__ = 'Mikhail K. Savkin'

from os.path import exists, isdir, join

def IsGitRepo(repoPath):
	GitDir = ".git"
	HeadFile = "HEAD"

	isDir = isdir(repoPath)
	if not isDir:
		return False

	headFile = join(repoPath, HeadFile)
	headExists = exists(headFile)
	if headExists:
		return True

	headFile = join(repoPath, GitDir, HeadFile)
	headExists = exists(headFile)
	if headExists:
		return True

	return False