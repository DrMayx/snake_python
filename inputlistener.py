from msvcrt import getwch
from threading import Thread
from time import sleep

class InputListener(Thread):

	
	def __init__(self):
		Thread.__init__(self)
		self.key = 'd'
		self.running = False
	
	def run(self):
		self.running = True
		while self.running:
			self.key = getwch()
	
	def stop(self):
		self.running = False
		input('press enter to continue...')
		sleep(1.5)

'''

get = InputListener()
get.start()

try:
	for i in range(3000):
		
		if get.key == 'p':
			get.stop()
			
			del get
			break
		print('a{}'.format(get.key))
		
		sleep(.2)
except:
	get.stop()
'''