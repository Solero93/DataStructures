# Made by: Christian José Soler
# Entrega 3: Stacks and Queues
# Estructures de Dades, Grup F

from Parserer import Parser # import of the parser method
from class_Queue import Queue # import of Queue class
from class_Stack import Stack # import of Stack class
from class_Node import Node # import of Node class



# call to parser to create the list of objects type Movie
parser = Parser()
movieList = parser.parserFile('peliculas100.dat')
movieList = movieList[0:20]
























## THIS IS TO TEST YOUR CODE - STACK
newStack = Stack()
newStack.printStack()

newNode = Node(movieList[0])
newStack.push(newNode)
newStack.printStack()

newStack.push(Node(movieList[1]))
newStack.printStack()

newStack.push(Node(movieList[2]))
newStack.printStack()

m1 = newStack.pop()
newStack.printStack()

m2 = newStack.pop()
newStack.printStack()

m3 = newStack.pop()
newStack.printStack()

m4 = newStack.pop()
newStack.printStack()

print m1.GetTitle()
print m2.GetTitle()
print m3.GetTitle()
#print m4.GetTitle()  GUESS WHAT HAPPENS...
# What we notice here is that since m4 is an empty object,
# The method GetTitle() cannot be applied to it, and an error is raised.

######### THIS IS TO TEST YOUR CODE - QUEUE
newQ = Queue()
newQ.printQ()

newNode = Node(movieList[0])
newQ.enqueue(newNode)
newQ.printQ()

newQ.enqueue(Node(movieList[1]))
newQ.printQ()

newQ.enqueue(Node(movieList[2]))
newQ.printQ()

m1 = newQ.dequeue()
newQ.printQ()

m2 = newQ.dequeue()
newQ.printQ()

m3 = newQ.dequeue()
newQ.printQ()

m4 = newQ.dequeue()
newQ.printQ()

print m1.GetTitle()
print m2.GetTitle()
print m3.GetTitle()
#print m4.GetTitle()  GUESS WHAT HAPPENS...
# What we notice here is that since m4 is an empty object,
# The method GetTitle() cannot be applied to it, and an error is raised.
	
	
	
