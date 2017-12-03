from tail import *

class Snake:
	
	def __init__(self, position = (1,1), direction = (0,1)):
		self.max_len = 2
		self.length = 2		#one for head and one for tail
		self.name = ''
		self.tail = []
		self.set_position()
		self.set_direction()
		
	def increase_length(self):
		self.length += 1
		self.set_max_len(self.length)
		self.add_tail()
		
	def get_length(self):
		return self.length
	
	def set_max_len(self, new_len):
		if new_len > self.max_len:
			self.max_len = new_len
			
	def set_name(self, name):
		self.name = name
		
	def get_max_len(self):
		return self.max_len
	
	def get_name(self):
		return self.name
		
	def add_tail(self):
		self.tail.append(Tail(self.position, self.direction))

	def set_position(self, position = (1,1)):
		self.position = position
	
	def set_direction(self, direction = (0,1)):
		self.direction = direction
	
	def move(self):
		self.set_position((self.position[0] + self.direction[0], self.position[1] + self.direction[1]))
		self.pull_tail()
	
	def pull_tail(self):
		for i, tail_cell in enumerate(self.tail):
			if i == 0 :
				direction = self.direction
			else:
				direction = self.tail[i-1].direction
			tail_cell.move(direction)