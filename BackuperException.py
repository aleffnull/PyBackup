__author__ = 'Mikhail K. Savkin'

class BackuperException(Exception):
	def __init__(self, message, *args, **kwargs):
		super(BackuperException, self).__init__(*args, **kwargs)
		self.__message = message

	@property
	def message(self):
		return self.__message