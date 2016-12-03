from Student import Student
import csv
import shutil

class StudentDataManager:

	def __init__(self, filename):
		self.__filename = filename

	def get_student(self, number):
		with open(self.__filename, newline='') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if row[1] == number:
					student = Student(row[0], row[1], row[2], row[3], row[5] == 'Ativo', row[4])
					return student
			csvfile.close()
		return None

	def write_student(self, student):
		tempfile = open('Data/temp.csv', 'w', newline='')
		with open(self.__filename, 'r') as csvfile:
			reader = csv.reader(csvfile)
			writer = csv.writer(tempfile)
			for row in reader:
				if row[1] == student.number:
					row[0] = student.name
					row[2] = student.phone
					row[3] = student.email
					row[4] = student.uffmail
					if student.status:
						row[5] = 'Ativo'
					else:
						row[5] = 'Inativo'
				writer.writerow(row)

			csvfile.close()
			tempfile.close()
			shutil.move(tempfile.name, self.__filename)

	def uffmail_exists(self, uffmail):
		with open(self.__filename, newline='') as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					if row[4] == uffmail:
						return True
				csvfile.close()
				return False

