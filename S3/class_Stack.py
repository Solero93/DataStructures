from class_Node import Node # Import of Node class

# Class that definies the attributes and basic methods of a Stack object
class Stack():
	def __init__(self):
		self.head = None # Initialization of "head"
		
	# Method to detect whether the Stack is empty or not	
	def isEmpty(self): 
		if self.head == None: # If there's no "head", then it is.
			return True
		else:
			return False
	
	# Method to print the elements of the Stack	
	def printStack(self): 
		if self.isEmpty(): # If it's empty, a message is shown
			print "Empty Stack!"
			
		else: # In the rest of cases:
			tmp = self.head # Declaration of a temporal variable, in order to not to lose head
			while tmp != None: # While it's not the end of the Stack
				print tmp.data.GetTitle() # The current element's title is printed
				tmp = tmp.after # Moves on to the next one	
	
	# Method to delete an element of the list (on the beginning)
	def push(self,data):
		node = Node(data)		
		node.after = self.head # The new element will point to "head"
		self.head = node # The new element becomes the new "head"
		
	# Method to add an element to the list (on the beginning)	
	def pop(self):
		if self.isEmpty(): # If it's empty we just show a message
			print "Empty Stack! Pop is not allowed!"
			
		else: # In the rest of cases:
			tmp = self.head # Declaration of a temporal variable, in order to return it after
			self.head = self.head.after # The element after "head" becomes the new "head" 
			return tmp.data # Return of the movie deleted