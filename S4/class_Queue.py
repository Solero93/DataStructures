from class_Node import Node # Import of Node class
from class_User import User

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# Class that definies the attributes and basic methods of a Queue object
class Queue():
        def __init__(self):
		self.head = None # Initilization of "head"
		self.tail = None # And "tail"
        
        # Method to detect whether the Queue's empty or isn't
        def isEmpty(self):
		return self.head == None # If there's no head, then it is
		
	# Method to print the elements of the Queue	
        def printQ(self):
		tmp = self.head # Declaration of a temporal variable, in order to not to lose head
		while tmp != None: # While it's not the end of the Queue
			print str(tmp.data) # The current element's title's printed
			tmp = tmp.after # Moves on to the next one
		
	# Method to add an element to the Queue (after the "tail")
        def enqueue(self, data):
		node = Node(data)
		if self.isEmpty(): # If it's empty, the element will became both head and tail
			self.head = node
			self.tail = node
			
		else: # The rest of cases:
			self.tail.after = node # "Tail" points to the new element
			self.tail = node # The new element becomes "tail"
	
	# Method to delete an element from the Queue (the "head")		
        def dequeue(self):
		if self.isEmpty(): # If it's empty, a message is shown
			return None
		else: # In the rest of cases:
			tmp = self.head # Declaration of a temporal variable, in order to return it after
			self.head = self.head.after # The element after "head" becomes the new "head" 
			return tmp.data # Return of the element deleted	
	
	# Return self.head
	def peek(self): 
		return self.head
	
	# Return the next of node (encapsulation)
	def peekAfter(self,node): 
		return node.after