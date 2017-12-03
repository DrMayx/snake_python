from gamecontroller import *
from view import View as view

class App:
	
	def main_loop(self):
	
		self.game = Game()
		self.user = self.game.snake
		not_a_new_game = False
		playing = True
		
		while playing:
			if self.game.new_game:
				user_name = input("What's your name?\n::")
				if user_name != '':
					self.user.set_name(user_name)
					self.game.new_game = False
					not_a_new_game = True
			else:
				user_input = view.game_menu()
				if user_input == '1':
					self.game.board.clear_board()
					self.game.run()
				elif user_input == '2':
					pass
				elif user_input == '3':
					view.show_stats(self.user)
				elif user_input == '0':
					self.game.save()
					playing = False
	
	def main(self):
		in_game = True
		while in_game:
			user_input = view.main_menu()
			if user_input == '1':
				self.main_loop()
			elif user_input == '2':
				in_game = False
				
if __name__ == '__main__':
	main = App()
	main.main()