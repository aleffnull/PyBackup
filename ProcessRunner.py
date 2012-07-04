__author__ = 'Mikhail K. Savkin'

from logging import getLogger
from subprocess import PIPE, Popen

class ProcessRunner:

	def __init__(self):
		self.__log = getLogger(__name__)

	def run(self, command, *args):
		self.__log.debug(
			"Running process '%s' with arguments (%s)",
			command, ", ".join(args))
		argsList = [command]
		if len(args):
			argsList += args
		process = Popen(argsList, stdout=PIPE, stderr=PIPE)
		(outputData, errorData) = process.communicate()

		self.__log.debug("Process STDOUT: %s", outputData)
		self.__log.debug("Process STDERR: %s", errorData)

		result = process.returncode
		if result:
			raise RuntimeError("Not zero process return code: %d", result)