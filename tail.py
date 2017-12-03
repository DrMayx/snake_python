class Tail:
	
	def __init__(self, position = (1, 1), direction = (0, 1)):
		self.position = position
		self.direction = direction

	def move(self, direction = (0, 0)):
		self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
		self.direction = direction