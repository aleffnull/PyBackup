__author__ = 'Mikhail K. Savkin'

from logging.config import fileConfig
from os.path import abspath, dirname, join
from unittest import TestCase

class BaseLoggingTestCase(TestCase):

	fileConfig("Tests/logging.conf")

	@staticmethod
	def _getFullPath(path):
		currentDir = dirname(abspath(__file__))
		fullPath = join(currentDir, path)

		return fullPath