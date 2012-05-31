__author__ = 'Mikhail K. Savkin'

from unittest import TestCase

class BaseRepoTestCase(TestCase):

	__bareRepoPath = None
	__commonRepoPath = None

	@classmethod
	def setUpClass(cls):
		super(BaseRepoTestCase, cls)
		cls.__bareRepoPath = "bare"
		cls.__commonRepoPath = "common"

	@classmethod
	def tearDownClass(cls):
		super(BaseRepoTestCase, cls)

	@classmethod
	def _getBareRepoPath(cls):
		return cls.__bareRepoPath

	@classmethod
	def _getCommonRepoPath(cls):
		return cls.__commonRepoPath