from Tkinter import *
from parserLastFM import *
from class_Interface import *

def main():
    global mainQueue, inter
    mainQueue = parser("LastFM_small.dat")
    inter = Interface()
    
    root = Tk()
    root.title("Users LastFM")
    app = LastFMApp(root)
    root.mainloop()
    
class LastFMApp(Interface):
    def __init__(self, root):

        self.frame = Frame(root)
        self.frame.grid()
	self.appList = Queue()
        
        inter.button(self.frame,"ADD",self.addUsers,1,1)	
	displayUser, userLabel = inter.labelvar(self.frame,"Users will be shown here",1,2)
        
        inter.button(self.frame, "SEARCH", self.searchUsers,2,1)
	inter.label(self.frame, "From relevance",2,2)
	inter.label(self.frame, "To relevance",2,3)
	entry1 = inter.entry(self.frame,3,2)
	entry2 = inter.entry(self.frame,3,3)
	
	displayArtist, artistLabel = inter.labelvar(self.frame,"Artists will be shown here",2,4)
	displayNextButton = inter.button(self.frame, "NEXT", self.displayNext,2,5)
	
	inter.label(self.frame,"ADDING COST: ",4,1)
	addCost, addLabel = inter.labelvar(self.frame,"XXX",4,2)
	inter.label(self.frame,"SEARCHING COST: ",4,3)
	searchCost, searchLabel = inter.labelvar(self.frame,"XXX",4,4)
	
	root.mainloop()
	
    def addUsers(self):
	print "guapo"
	#for a in range(1000):
	    #self.appList.enqueue(mainList.dequeue())
	self.frame.mainloop()
    def searchUsers(self):
	print "feo"
	tmp = Queue()
	for element in appList:
	    if element.relevance >= begin and element.relevance <= final:
		tmp.enqueue(element)
	
	self.frame.mainloop()
    def displayNext(self):
	print "ayy"
	self.frame.mainloop()
	
	
	
	
		#a, label = inter.labelvar(self.frame,"XORRA",3,0)
		#a.set("asd")
		
		#entry = inter.entry(self.frame,4,0)
		
		
		#Button(self.frame, text="ADD", command = self.addUsers).grid(column=0, row=0)
		
		#self.displayUser = StringVar()
		#self.displayUser.set("Users will be shown here")
		#Label(self.frame, textvariable = self.displayUser).grid(column=0, row=1)	
		
		#self.self.frame = LabelFrame(self.frame).grid(column=1, row=0)
		#Button(self.self.frame, text="SEARCH", command = self.searchUsers).grid(column=0, row=0)	
		#Label(self.self.frame, text = "From relevance").grid(column=0, row=1)
		#Entry(self.self.frame).grid(column=1, row=1)
		#Label(self.self.frame, text = "\n" + "To relevance").grid(column=0, row=2, sticky = "N")
		#Entry(self.self.frame).grid(column=1, row=2)	
		
		
		#Button(self.frame, text="DISPLAY NEXT", command = self.displayNext).grid(column=1, row=1)
		
		#self.displayArtist = StringVar()
		#self.displayArtist.set("Artists will be shown here")
		#self.displayRelevance = StringVar()
		#self.displayRelevance.set("Relevance will be shown here")
		#Label(self.frame, textvariable = ("Artist: %s \n Relevance: %s" %(self.displayArtist, self.displayRelevance))).grid(column=1, row=1)
		
	
		#self.displayAddCost = StringVar()
		#self.displayAddCost.set("-")
		#self.displaySearchingCost = StringVar()
		#self.displaySearchingCost.set("-")
		#Label(self.frame, textvariable = ("ADDING cost: \n %s \n SEARCHING cost \n %s" %(self.displayAddCost, self.displaySearchingCost))).grid(column=2, row=0, columnspan=2)		