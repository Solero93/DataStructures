# Class Node will create objects for Stack and Queue
class Node:
	def __init__(self, data, after=None):
		self.data = data # The attribute that will stand for movie			
		self.after = after # The attribute that will point to the next element of the list