
class Student:

	def __init__(self, name, number, phone, email, uffmail=None, status=False):
		self.__name = name
		self.__number = number
		self.__phone = phone
		self.__email = email
		self.__uffmail = uffmail
		self.__status = status

	@property
	def name(self):
		return self.__name

	@property
	def number(self):
		return self.__number

	@property
	def phone(self):
		return self.__phone

	@property
	def email(self):
		return self.__email

	@property
	def uffmail(self):
		return self.__uffmail

	@uffmail.setter
	def uffmail(self, uffmail):
		self.__uffmail = uffmail

	@property
	def status(self):
		return self.__status