__author__ = 'Mikhail K. Savkin'

from datetime import datetime

def GetTimestampAsFileName():
	now = datetime.now()
	timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

	return timestamp
