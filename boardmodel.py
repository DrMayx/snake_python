from apple import *
from random import randint
#plansza do gry

class Board:
	
	# constants
	ZERO = 0
	
	def __init__(self, width=40, height=20):
		self.width = width
		self.height = height
		self.board = self.generate_board()
		self.apple = None
		
	def get_board(self):
		return self.board
		
	def generate_board(self):
		board =[]
		
		for row in range(self.height):
			board.append([])
			if row == Board.ZERO or row == self.height - 1:		# number 1 is for fitting in the range of 'range' function
				for col in range(self.width):
					board[row].append('#')
			else:
				board[row].append('#')
				for col in range(self.width-2):					# number 2 is self.width minus chars at the begining and the end of line
					board[row].append(' ')
				board[row].append('#')
				
		return board
		
	def change_cell_state(self, position = (1, 1), direction = (0,0), char = 'O', last=' '):		
		'''
		direction:		
			UP : 	(-1,0)
			RIGHT: 	(0,1)
			DOWN:	(1,0)
			LEFT:	(0,-1)
		position:	(y,x) where x,y are the indexes of current cell
		'''
		
		X = 1 # index of x axis in direction and position
		Y = 0 # index of y axis in direction and position

		if position[X] + direction[X] < 0 or \
			position[Y] + direction[Y] < 0 or \
			position[X] + direction[X] >= self.width or \
			position[Y] + direction[Y] >= self.height or \
			self.board[position[Y]][position[X]] == '#' or \
			self.board[position[Y]+direction[Y]][position[X]+direction[X]] == '#':
			
			raise ValueError

		self.board[position[Y]][position[X]] = last
		self.board[position[Y]+direction[Y]][position[X]+direction[X]] = char

	def get_middle(self):
		return ( int(self.height//2), int(self.width//2))
		
	def clear_board(self):
		self.board = self.generate_board()
		
	def generate_apple(self):
		apple_x = 0
		apple_y = 0
		
		while self.board[apple_y][apple_x] in ('#', 'O', 'o'):
			apple_x = randint(1,self.width-1)
			apple_y = randint(1,self.height-1)
		
		self.apple = Apple((apple_y, apple_x))
		print(self.apple.position)
		self.change_cell_state(position = self.apple.position, char = '*')
		
		