from StudentDataManager import StudentDataManager
from Student import Student

manager = StudentDataManager('Data/alunos.csv')

def create_emails(name):
	emails = []
	names = name.lower().split()

	uffmail = names[0]+names[-1]+'@id.uff.br'
	if not manager.uffmail_exists(uffmail):
		emails.append(uffmail)

	uffmail = names[0][0]+names[-1]+'@id.uff.br'
	if not manager.uffmail_exists(uffmail):
		emails.append(uffmail)

	uffmail = names[0] + ''.join(list((name[0] for name in names[1:-1]))) + names[-1] + '@id.uff.br'
	if not manager.uffmail_exists(uffmail):
		emails.append(uffmail)

	uffmail = names[0] + ''.join(list((name[0] for name in names[1:]))) + '@id.uff.br'
	if not manager.uffmail_exists(uffmail):
		emails.append(uffmail)

	uffmail = ''.join(list((name[0] for name in names[:-1])))+ names[-1] + '@id.uff.br'
	if not manager.uffmail_exists(uffmail):
		emails.append(uffmail)

	size = len(emails)
	end = 1
	while size < 5:
		uffmail = names[0]+names[-1]+str(end)+'@id.uff.br'
		if not manager.uffmail_exists(uffmail):
			emails.append(uffmail)
			size += 1
		end += 1
	
	return emails


def main():
	
	number = input('Digite sua matrícula: ')
	student = manager.get_student(number)
	print('Aluno(a) '+ student.name)
	
	emails = create_emails(student.name)
	if student.uffmail == '' and student.status:
		print('Escolha uma das opções abaixo para o seu UFFMail')
		for i in range(len(emails)):
			print(str(i+1) + ' - ' + emails[i])

		choosen = input('\n')
		student.uffmail = emails[int(choosen)-1]
		print('\nO endereço de email '+student.uffmail+' foi selecionado e será criado nos próximos minutos.')
		print('Um SMS foi enviado para '+student.phone+' com a sua senha de acesso.')
		manager.write_student(student)

	elif student.uffmail != '':
		print('Esse(a) aluno(a) já possui um UFFMail cadastrado.')
	else:
		print('Esse(a) aluno(a) não está ativo.')

if __name__ == '__main__':
	main()