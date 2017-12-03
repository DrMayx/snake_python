import unittest
from snakemodel import *
from random import randint
from boardmodel import *
from gamecontroller import *

class BoardTester(unittest.TestCase):

	def test_board_creation(self):
		board = Board()
		
	def test_default_board_initialization(self):
		board = Board()
		self.assertEqual(board.width, 40)
		self.assertEqual(board.height, 20)
		self.assertIsInstance(board, Board)
		
	def test_custom_board_initialization(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			self.assertEqual(board.width, width)
			self.assertEqual(board.height, height)
	
	def test_change_cell_state_default(self):
		board = Board()
		board.change_cell_state()
		self.assertEqual(board.board[1][1], 'O')

	def test_change_cell_state_custom(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			if cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x))
			else:
				board.change_cell_state(position = (cell_y, cell_x))
				self.assertEqual(board.board[cell_y][cell_x], 'O')
				
	def test_change_cell_when_moving_up(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			top_edge_overflow = cell_y - 1 < 1
			
			if on_edge or top_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (-1,0))
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (-1,0))
				self.assertEqual(board.board[cell_y][cell_x], ' ')
				self.assertEqual(board.board[cell_y-1][cell_x], 'O')
		
	def test_change_cell_when_moving_down(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			bottom_edge_overflow = cell_y + 1 > height - 1
				
			if on_edge or bottom_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (1,0))
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (1,0))
				self.assertEqual(board.board[cell_y][cell_x], ' ')
				self.assertEqual(board.board[cell_y+1][cell_x], 'O')
			
	def test_change_cell_when_moving_left(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			left_edge_overflow = cell_x - 1 < 1
				
			if on_edge or left_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (0,-1))
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (0,-1))
				self.assertEqual(board.board[cell_y][cell_x], ' ')
				self.assertEqual(board.board[cell_y][cell_x-1], 'O')
	
	def test_change_cell_when_moving_right(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			right_edge_overflow = cell_x + 1 > width - 1
			
			if on_edge or right_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (0,1))
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (0,1))
				self.assertEqual(board.board[cell_y][cell_x], ' ')
				self.assertEqual(board.board[cell_y][cell_x+1], 'O')
				
	def test_change_cell_when_moving_up_with_tail(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			top_edge_overflow = cell_y - 1 < 1
				
			if on_edge or top_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (-1,0), last = 'o')
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (-1,0), last = 'o')
				self.assertEqual(board.board[cell_y][cell_x], 'o')
				self.assertEqual(board.board[cell_y-1][cell_x], 'O')
	
	def test_change_cell_when_moving_down_with_tail(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			bottom_edge_overflow = cell_y + 1 > height - 1
				
			if on_edge or bottom_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (1,0), last = 'o')
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (1,0), last = 'o')
				self.assertEqual(board.board[cell_y][cell_x], 'o')
				self.assertEqual(board.board[cell_y+1][cell_x], 'O')
			
	def test_change_cell_when_moving_left_with_tail(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			left_edge_overflow = cell_x - 1 < 1
				
			if on_edge or left_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (0,-1), last = 'o')
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (0,-1), last = 'o')
				self.assertEqual(board.board[cell_y][cell_x], 'o')
				self.assertEqual(board.board[cell_y][cell_x-1], 'O')
	
	def test_change_cell_when_moving_right_with_tail(self):
		for i in range(50):
			width = randint(10,100)
			height = randint(5,50)
			board = Board(width, height)
			
			height -= 1
			width -= 1
			cell_x = randint(0,width)
			cell_y = randint(0,height)
			
			on_edge = cell_x == 0 or cell_y == 0 or cell_y == height or cell_x == width
			right_edge_overflow = cell_x + 1 > width - 1
			
			if on_edge or right_edge_overflow:
				with self.assertRaises(ValueError):
					board.change_cell_state(position = (cell_y, cell_x), direction = (0,1), last = 'o')
			else:
				board.change_cell_state(position = (cell_y, cell_x), direction = (0,1), last = 'o')
				self.assertEqual(board.board[cell_y][cell_x], 'o')
				self.assertEqual(board.board[cell_y][cell_x+1], 'O')
				
class GameTester(unittest.TestCase):

	def test_game_init(self):
		game = Game()
		self.assertTrue(isinstance(game.board, Board))
		self.assertTrue(isinstance(game.snake, Snake))
	
	def test_in_game_board_creation(self):
		game = Game()
		self.assertTrue(isinstance(game.gameboard, list))
	
	def test_in_game_snake_creation(self):
		game = Game()
		self.assertTrue(isinstance(game.snake.length, int))
	
class SnakeTester(unittest.TestCase):

	def test_snake_init(self):
		snake = Snake()
		self.assertEqual(snake.length, 3)
		self.assertIsInstance(snake, Snake)
	
	def test_snake_grow(self):
		snake = Snake()
		snake.increase_length()
		self.assertEqual(snake.get_length(), 4)
	
	def test_snake_name(self):
		snake = Snake()
		name = 'wunsz'
		snake.set_name(name)
		self.assertEqual(snake.name, 'wunsz')
	
	def test_set_max_len(self):
		snake = Snake()
		
		for i in range(30):
			old_max = snake.get_max_len()
			new_value = randint(0,i*10)
			snake.set_max_len(new_value)
			if new_value >= old_max:
				self.assertEqual(snake.get_max_len(), new_value)
			else:
				self.assertEqual(snake.get_max_len(), old_max)
	
	def test_snake_grow_and_increase_max_len(self):
		snake = Snake()

		length = snake.get_length()
		for i in range(30):
			old_max = snake.get_max_len()
			snake.increase_length()
			length += 1
			if length >= old_max:
				self.assertEqual(snake.get_max_len(), length)
			else:
				self.assertEqual(snake.get_max_len(), old_max)
		
			
			
		
		
if __name__ == '__main__':
	unittest.main(verbosity = 2)