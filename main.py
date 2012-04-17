""" Backup local git repositories to CD on Windows """

__author__ = "Mikhail K. Savkin"
__version__ = "1.0"

from logging import getLogger
from logging.config import fileConfig
from optparse import OptionParser
from sys import exit

from Backuper import Backuper

def main():
	fileConfig("logging.conf")
	log = getLogger(__name__)
	log.info("PyBackup %s by %s" % (__version__, __author__))

	try:
		parser = OptionParser()
		parser.add_option("-r", "--repo", dest="repoPath", help="path to repository")
		parser.add_option("-t", "--temp", dest="tempDir", help="path to temp directory")
		(options, args) = parser.parse_args()

		if options.repoPath is None:
			log.error("path to repository is required")
			exit()

		backuper = Backuper(options.repoPath, options.tempDir)
		backuper.run()
	except Exception as exception:
		log.exception(exception)

	log.info("Execution finished")

if __name__ == "__main__":
	main()