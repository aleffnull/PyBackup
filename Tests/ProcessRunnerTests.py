__author__ = 'Mikhail K. Savkin'

from unittest import main

from BaseLoggingTestCase import BaseLoggingTestCase
from ProcessRunner import ProcessRunner

class RunTests(BaseLoggingTestCase):

	def test_AttribCommand_Success(self):
		runner = ProcessRunner()
		result = runner.run("attrib")

		self.assertEqual(result, 0)

if __name__ == '__main__':
	main()
