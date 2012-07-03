__author__ = 'Mikhail K. Savkin'

from logging.config import fileConfig
from unittest import TestCase

class BaseLoggingTestCase(TestCase):

	fileConfig("Tests/logging.conf")