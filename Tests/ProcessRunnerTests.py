__author__ = 'Mikhail K. Savkin'

from os import sep
from unittest import main

from BaseLoggingTestCase import BaseLoggingTestCase
from ProcessRunner import ProcessRunner

class RunTests(BaseLoggingTestCase):

	def test_AttribCommand_NoArguments_Success(self):
		runner = ProcessRunner()
		runner.run("attrib")

	def test_PythonCommand_VersionArgument_Success(self):
		runner = ProcessRunner()
		runner.run("python", "--version")

	def test_InvalidCommand_WindowsError(self):
		runner = ProcessRunner()
		self.assertRaises(WindowsError, runner.run, "foo")

	def test_PythonCommand_NotZeroExitCode(self):
		runner = ProcessRunner()
		script = "Data%snon_zero_exit_code.py"% sep
		scriptPath = self._getFullPath(script)
		self.assertRaises(RuntimeError, runner.run, "python", scriptPath)

if __name__ == '__main__':
	main()
