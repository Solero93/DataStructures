from class_Queue import *
from class_Node import *
from types import *

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

class PriorityQueue(Queue):
    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty(): 
	# If it's empty proceed as in a Queue()
            self.head = node
            self.tail = node
        else:
            tmp = self.head
	    if tmp.data <= node.data: 
	    # Initial check in case the node should become self.head
		node.after = self.head
		self.head = node
	    else:
		while not isinstance(tmp.after,NoneType) and tmp.after.data >= node.data:
		# While tmp.after isn't None and the place of node hasn't been found, advance
		    tmp = tmp.after
		if isinstance(tmp.after,NoneType): 
		# If the place of node hasn't been found, it becomes self.tail
		    self.tail.after = node
		    self.tail = node
		else:
		# In the rest of cases, it's inserted at its place
		    node.after = tmp.after
		    tmp.after = node