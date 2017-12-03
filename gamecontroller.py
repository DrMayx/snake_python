from boardmodel import *
from snakemodel import *
from inputlistener import *
from time import sleep
from view import View as view

class Game:

	def __init__(self):
		self.board = Board()
		self.snake = Snake()
		self.new_game = True

	def get_snake(self):
		return self.snake
	
	def save(self):
		pass
		
	def run(self):
		apple_on_the_board = False
		middle = self.board.get_middle()
		self.snake.position = middle
		self.board.change_cell_state(position = self.snake.position)
		self.snake.add_tail()
		
		try:
			get = InputListener()
			get.start()
			
			dir_char = get.key
			
			last_sleep = .1
			
			in_game = True
			
			while in_game:
				snake_growing = False
				view.print_board(self.board.board)
				
				if get.key == 'p':
					get.stop()
					break
				elif get.key == 'w':
					self.snake.set_direction((-1,0))
				elif get.key == 's':
					self.snake.set_direction((1,0))
				elif get.key == 'a':
					self.snake.set_direction((0,-1))
				elif get.key == 'd':
					self.snake.set_direction((0,1))
				
				if not apple_on_the_board:
					self.board.generate_apple()
					apple_on_the_board = True
				
				if self.snake.position == self.board.apple.position:
					self.snake.increase_length()
					snake_growing = True
					
				self.board.change_cell_state(position = self.snake.position, direction = self.snake.direction)
				if not snake_growing:
					for tail_cell in self.snake.tail:
						tail_pos_y = tail_cell.position[0] + tail_cell.direction[0]
						tail_pos_x = tail_cell.position[1] + tail_cell.direction[1]
						self.board.change_cell_state(position = (tail_pos_y, tail_pos_x), char = 'o')
						pos_to_clear =(tail_pos_y - tail_cell.direction[0], tail_pos_x - tail_cell.direction[1])
				
						self.board.change_cell_state(position = pos_to_clear, char = ' ')
				self.snake.move()
				
				if get.key == 'a' or get.key == 'd':
					last_sleep = .1
				elif get.key == 'w' or get.key == 's':
					last_sleep = .2
				sleep(last_sleep)
				
		except (KeyboardInterrupt):#, ValueError):
			get.stop()