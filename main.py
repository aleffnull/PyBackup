""" Backup local git repositories to CD on Windows """

__author__ = "Mikhail K. Savkin"
__version__ = "1.0"

import logging
import logging.config

def main():
	logging.config.fileConfig("logging.conf")
	log = logging.getLogger()
	log.info("PyBackup %s by %s" % (__version__, __author__))
	log.info("Execution finished")

#	parser = OptionParser()
#	parser.add_option("-r", "--repo", dest="repoPath", help="path to repository")
#	(options, args) = parser.parse_args()
#
#	if options.repoPath is None:
#		parser.error("path to repository is required")
#
#	backuper = Backuper(options.repoPath)
#	try:
#		backuper.run()
#	except BackuperException as exception:
#		print "Error occurred: %s" % exception.message

if __name__ == "__main__":
	main()