from os import system, name
class View:
	
	@classmethod
	def game_menu(cls):
		cls.clear()
		message = '1.START\n' + \
			'2.TOP SCORES\n' + \
			'3.SHOW PPROFILE DETAILS\n' +\
			'0. EXIT\n'+\
			'Choose: '
		return input(message)
		
	@classmethod	
	def show_stats(cls, user):
		cls.clear()
		message = 'Name: ' + user.get_name() + '\n' + \
		'Max length: ' + str(user.get_max_len()) + '\n' + \
		'\n\nEnter any key to continue ...'
		
		return input(message)
		
	@classmethod	
	def main_menu(cls):
		cls.clear()
		message = '1. Play\n' + \
				'2. Exit\n'
		return input(message)

	@staticmethod
	def clear():
		system('cls' if name == 'nt' else 'clear')
	
	@classmethod
	def print_board(cls, board):
		cls.clear()
		to_print = ''
		for row in board:
			for col in row:
				to_print += col
			to_print += '\n'
		print(to_print)