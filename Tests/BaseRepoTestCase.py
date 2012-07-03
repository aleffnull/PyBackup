__author__ = 'Mikhail K. Savkin'

from os import listdir, sep
from os.path import abspath, dirname, isdir, join, split
from shutil import rmtree
from tempfile import mkdtemp
from zipfile import ZipFile

from BaseLoggingTestCase import BaseLoggingTestCase

class BaseRepoTestCase(BaseLoggingTestCase):

	__BareRepoFileName = "Data%srepo.git.zip" % sep
	__CommonRepoFileName = "Data%srepo.zip" % sep

	__bareRepoPath = None
	__commonRepoPath = None

	@classmethod
	def setUpClass(cls):
		super(BaseRepoTestCase, cls)
		cls.__bareRepoPath = cls.__extractArchive(cls.__BareRepoFileName)
		cls.__commonRepoPath = cls.__extractArchive(cls.__CommonRepoFileName)

	@classmethod
	def tearDownClass(cls):
		super(BaseRepoTestCase, cls)
		bareRepoParentPath = cls.__getParentPath(cls.__bareRepoPath)
		commonRepoParentPath = cls.__getParentPath(cls.__commonRepoPath)
		rmtree(bareRepoParentPath)
		rmtree(commonRepoParentPath)

	@classmethod
	def _getBareRepoPath(cls):
		return cls.__bareRepoPath

	@classmethod
	def _getCommonRepoPath(cls):
		return cls.__commonRepoPath

	@classmethod
	def __getFullPath(cls, path):
		currentDir = dirname(abspath(__file__))
		fullPath = join(currentDir, path)

		return fullPath

	@classmethod
	def __getParentPath(cls, path):
		return split(path)[0]

	@classmethod
	def __extractArchive(cls, archivePath):
		path = cls.__getFullPath(archivePath)
		zipfile = ZipFile(path)
		dir = mkdtemp()
		zipfile.extractall(dir)
		contents = [d for d in listdir(dir) if isdir(join(dir, d))]
		if len(contents) != 1:
			raise ValueError("Archive %s must have exactly one top-level directory" % archivePath)
		repoPath = join(dir, contents[0])

		return repoPath