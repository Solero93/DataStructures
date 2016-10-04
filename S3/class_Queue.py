from class_Node import Node # Import of Node class

# Class that definies the attributes and basic methods of a Queue object
class Queue():
        def __init__(self):
		self.head = None # Initilization of "head"
		self.tail = None # And "tail"
        
        # Method to detect whether the Queue's empty or isn't
        def isEmpty(self):
		if self.head == None: # If there's no head, then it is
			return True
		else:
			return False
		
	# Method to print the elements of the Queue	
        def printQ(self):
		if self.isEmpty(): # If it's empty, a message is shown
			print "Empty Queue!"
			
		else: # In the rest of cases:
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
			print "Empty Queue! Dequeue not allowed!"
		else: # In the rest of cases:
			tmp = self.head # Declaration of a temporal variable, in order to return it after
			self.head = self.head.after # The element after "head" becomes the new "head" 
			return tmp.data # Return of the element deleted	
		
	#class Iterator(Iterator):
		#def __init__(self, queue):
			#super(Queue.Iterator, self).__init__(queue)
			#self._position=0
			
		#def next(self):
			#if self._position >= self._container._count:
				#raise StopIteration
			#obj = self._container._array[self._position]
			#self._position = self._position + 1
			#return obj
		
	#def __iter__(self):
		#return self.Iterator(self)