__author__ = 'Mikhail K. Savkin'

from os.path import exists, isdir, join
from re import match

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

def GetRepoName(directoryName):
	if directoryName is None or len(directoryName) == 0:
		raise ValueError("directoryName parameter must be specified")

	pattern = "(.*)\.git"
	m = match(pattern, directoryName)
	if m is None:
		return directoryName

	repoName = m.group(1)
	return repoName