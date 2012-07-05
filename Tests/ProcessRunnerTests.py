__author__ = 'Mikhail K. Savkin'

from os import sep
from unittest import main

from BaseLoggingTestCase import BaseLoggingTestCase
from ProcessRunner import ProcessRunner

class RunTests(BaseLoggingTestCase):

	def test_AttribCommand_NoArguments_Success(self):
		ProcessRunner("attrib")

	def test_PythonCommand_VersionArgument_Success(self):
		ProcessRunner("python", "--version")

	def test_InvalidCommand_Error(self):
		self.assertRaises(RuntimeError, ProcessRunner, "foo")

	def test_PythonCommand_NotZeroExitCode(self):
		script = "Data%snon_zero_exit_code.py"% sep
		scriptPath = self._getFullPath(script)
		self.assertRaises(RuntimeError, ProcessRunner, "python", scriptPath)

	def test_ShellCdCommand_NoArguments_Success(self):
		ProcessRunner("cd")

if __name__ == '__main__':
	main()
