from Tkinter import *
from parserLastFM import *
from class_Interface import *
from class_Node import *
import time

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

def main():
    global mainQueue, inter
    mainQueue = parser("LastFM_small.dat") # The principal Queue of the application
    ## I won't use LastFM_big.dat because it has errors made by its creator
    inter = Interface() # Class to create the widgets of the application
    
    root = Tk()
    root.title("Users LastFM")
    app = LastFMApp(root) # Initialization of the application
    root.mainloop()
    
class LastFMApp():
    def __init__(self, root):

        self.frame = Frame(root)
        self.frame.grid()
	self.appQueue = Queue() # Queue of the application
	self.searchQueue = Queue() # Queue of the search
	self.currentNode = Node("No user selected") # The current user shown
        
	#Widgets by column made with the class Interface()
        
        #1st column
        inter.button(self.frame,"ADD",self.addUsers,1,1,"left",1,3)	
	self.displayUser, userLabel = inter.labelvar(self.frame,"Users will be shown here",1,4)
        
        #2nd column
        inter.button(self.frame,"SEARCH", self.searchUsers,2,1)
	inter.label(self.frame,"From relevance",2,2)
	self.endEntry = inter.entry(self.frame,3,3)	
	inter.label(self.frame,"To relevance",2,3)
	self.beginEntry = inter.entry(self.frame,3,2)
	
	#3rd column
	self.displayArtist, artistLabel = inter.labelvar(self.frame,"Artists will be shown here",2,4,"center",2,1)
	displayNextButton = inter.button(self.frame,"DISPLAY NEXT", self.displayNext,2,5,"center",2,1)
	
	#4th column
	inter.label(self.frame,"ADDING COST: ",4,1)
	self.addCost, addLabel = inter.labelvar(self.frame,"XXX",4,2)
	inter.label(self.frame,"SEARCHING COST: ",4,3)
	self.searchCost, searchLabel = inter.labelvar(self.frame,"XXX",4,4)
	
	root.mainloop()
    
    # Method to add 1000 Users to the Queue of the application
    def addUsers(self):
	t1 = time.clock() # Timer start
	for a in xrange(1000):
	    self.appQueue.enqueue(mainQueue.dequeue()) 
	    # dequeue 1000 times from MainQueue and add the returned element to appQueue
	t2 = time.clock() # Timer end
	self.addCost.set("%0.3f s" %(t2-t1)) # Set the timer difference as addCost
	self.currentNode = self.appQueue.peek() # The node of the application is the head of appQueue
	
	self.frame.mainloop()
    
    # Method to search between users by their relevance
    def searchUsers(self):
	# Get begin and end from the current entries
	begin = self.beginEntry.get()
	end = self.endEntry.get()
	# If end is the empty String, end=100, same for begin=0
	if end == "": end = 100
	if begin == "": begin = 0
	# Since .get() return a String, it must be converted to float
	begin = float(begin)
	end = float(end)
	
	t3 = time.clock() # Timer start
	
	# Definition of temporal Queue and Node
	tmpQueue = Queue()
	tmpNode = self.appQueue.peek()
	
	while not isinstance(self.appQueue.peekAfter(tmpNode),NoneType):
	# While the appQueue is not finished, check if the current element meets the requirements
	    tmpData = self.appQueue.peekAfter(tmpNode).data
	    if tmpData.searchRelevance(begin,end):
		tmpQueue.enqueue(tmpData) # In case it meets, add it to tmpQueue
	    tmpNode = self.appQueue.peekAfter(tmpNode) # Advance node
	self.searchQueue = tmpQueue # Set the search result, tmpQueue, to self.searchQueue
	
	t4 = time.clock() # Timer end
	self.searchCost.set("%0.3f s" %(t4-t3)) # Set the timer difference as searchCost
	
	if self.searchQueue.isEmpty(): # If there are no matches, the currentNode will show Nothing
	    self.currentNode = Node("Nothing")
	else: # In the rest of cases, the head of the Queue will become the current node
	    self.currentNode = self.searchQueue.peek()
	
	self.frame.mainloop()
    
    # Method to display the next element of the current list
    def displayNext(self):
	# If the Node has a String in it ("Nothing"), just show it
	if isinstance(self.currentNode.data,str):
	    self.displayUser.set(str(self.currentNode.data))
	    self.displayArtist.set(str(self.currentNode.data))
	else: # In the rest of cases, show its content, in the right way
	    self.displayUser.set(str(self.currentNode.data))
	    self.displayArtist.set("Artist: %s \n Relevance: %s" %(str(self.currentNode.data.getMost()), str(self.currentNode.data.getRelevance())))
	    self.currentNode = self.currentNode.after # Advance node in the list
	
	self.frame.mainloop()
main()