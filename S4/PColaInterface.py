from Tkinter import *
from PparserLastFM import *
from class_Interface import *
from class_Node import *
import time

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# All comments made in ColaInterface.py apply to here
def main():
    global mainQueue, inter
    mainQueue = parserP("LastFM_small.dat")
    inter = Interface()
    
    root = Tk()
    root.title("Users LastFM")
    app = LastFMAppP(root)
    root.mainloop()
    
class LastFMAppP():
    def __init__(self, root):

        self.frame = Frame(root)
        self.frame.grid()
	self.appQueue = PriorityQueue()
	self.searchQueue = PriorityQueue()
	self.currentNode = Node("No user is selected")
        
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
	
    def addUsers(self):
	t1 = time.clock()
	for a in xrange(1000):
	    self.appQueue.enqueue(mainQueue.dequeue())
	t2 = time.clock()
	self.addCost.set("%0.3f s" %(t2-t1))
	self.currentNode = self.appQueue.peek()
	
	self.frame.mainloop()
	
    def searchUsers(self):
	begin = self.beginEntry.get()
	end = self.endEntry.get()
	if end == "": end = 100
	if begin == "": begin = 0
	begin = int(begin)
	end = int(end)
	
	t3 = time.clock()
	
	tmpQueue = PriorityQueue()
	tmpNode = self.appQueue.peek()
	while not isinstance(self.appQueue.peekAfter(tmpNode),NoneType):
	    tmpData = self.appQueue.peekAfter(tmpNode).data
	    if tmpData.searchRelevance(begin,end):
		tmpQueue.enqueue(tmpData)
	    tmpNode = self.appQueue.peekAfter(tmpNode)
	self.searchQueue = tmpQueue
	
	t4 = time.clock()
	self.searchCost.set("%0.3f s" %(t4-t3))
	
	if self.searchQueue.isEmpty():
	    self.currentNode = Node("Nothing")
	else:
	    self.currentNode = self.searchQueue.peek()
	
	self.frame.mainloop()
    
    def displayNext(self):    
	if isinstance(self.currentNode.data,str):
	    self.displayUser.set(str(self.currentNode.data))
	    self.displayArtist.set(str(self.currentNode.data))
	else:
	    self.displayUser.set(str(self.currentNode.data))
	    self.displayArtist.set("Artist: %s \n Relevance: %s" %(str(self.currentNode.data.getMost()), str(self.currentNode.data.getRelevance())))
	    self.currentNode = self.currentNode.after
	
	self.frame.mainloop()
main()