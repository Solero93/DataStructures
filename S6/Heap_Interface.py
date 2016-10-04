from Tkinter import *
from parserLastFM import *
from class_Interface import *
from class_Heap import *
import time
from itertools import cycle
from operator import attrgetter

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 6: Tkinter y Heaps

def main():
    global mainQueue, inter
    mainQueue = parser("LastFM_small.dat")  # The principal Queue of the application, since adding from a Queue better than from a tree
    ## I won't use LastFM_big.dat because it has errors made by its creator
    inter = Interface()  # Class to create the widgets of the application

    root = Tk()
    root.title("Users LastFM")
    LastFMApp(root)  # Initialization of the application
    root.mainloop()


class LastFMApp():
    def __init__(self, root):

        self.frame = Frame(root)
        self.frame.grid()
        self.appHeap = Heap()  # Heap of the application
        self.searchList = []  # List of the search
        self.currentUser = "No user selected"  # The current user shown

        #Widgets by column made with the class Interface()

        #1st column
        inter.button(self.frame, "ADD", self.addUsers, 1, 1, "left", 1, 3)
        self.displayUser, userLabel = inter.labelvar(self.frame, "Users will be shown here", 1, 4)

        #2nd column
        inter.button(self.frame, "SEARCH", self.searchUsers, 2, 1)
        inter.button(self.frame, "DELETE", self.deleteUser, 3, 1)
        inter.label(self.frame, "From relevance", 2, 2)
        self.endEntry = inter.entry(self.frame, 3, 3)
        inter.label(self.frame, "To relevance", 2, 3)
        self.beginEntry = inter.entry(self.frame, 3, 2)

        #3rd column
        self.displayArtist, artistLabel = inter.labelvar(self.frame, "Artists will be shown here", 2, 4, "center", 2, 1)
        inter.button(self.frame, "DISPLAY NEXT", self.displayNext, 2, 5, "center", 2, 1)

        #4th column
        inter.label(self.frame, "ADDING COST: ", 4, 1)
        self.addCost, addLabel = inter.labelvar(self.frame, "XXX", 4, 2)
        inter.label(self.frame, "SEARCHING COST: ", 4, 3)
        self.searchCost, searchLabel = inter.labelvar(self.frame, "XXX", 4, 4)
        inter.label(self.frame, "DELETE COST: ", 4, 5)
        self.deleteCost, deleteLabel = inter.labelvar(self.frame, "XXX", 4, 6)

        root.mainloop()

    # Method to add 1000 Users to the Tree of the application
    def addUsers(self):
        t1 = time.clock() # Timer start
        for a in xrange(5000):
            tmp = mainQueue.dequeue()
            self.appHeap.insert(tmp)
            # dequeue 1000 times from MainQueue and add the returned element to appHeap
        t2 = time.clock() # Timer end
        self.addCost.set("%0.3f s" % (t2 - t1))  # Set the timer difference as addCost
        self.search(0, 100)  # We search the users

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

        t3 = time.clock()  # Timer start
    
        self.search(begin, end)

        t4 = time.clock() # Timer end
        self.searchCost.set("%0.3f s" % (t4 - t3))  # Set the timer difference as searchCost

        if len(self.searchList) == 0:
            self.currentUser = "No user selected"
        else:
            self.currentUser = self.searchIter.next()

        self.frame.mainloop()
    
    # Support method for search    
    def search(self, begin, end):
        tmp = self.appHeap.getContainer()
        self.searchList = sorted(filter(lambda x: begin <= x.relevance <= end, tmp), None, key=attrgetter('relevance'))
        self.searchList.reverse()
        self.searchIter = cycle(self.searchList)

    # Method to delete users in a range of relevance
    def deleteUser(self):
        t3 = time.clock()

        self.appHeap.remove() # We call remove of Heap
        self.searchList.pop(0) # We delete the the first element of the search list
        self.searchIter = cycle(self.searchList)

        t4 = time.clock()  # Timer end
        self.deleteCost.set("%0.3f s" % (t4 - t3))  # Set the timer difference as searchCost

        self.frame.mainloop()

    # Method to display the next element of the current list
    def displayNext(self):
        # If no search has been made, we force the user to make one
        if len(self.searchList) == 0:
            self.displayUser.set("Make a search before displaying")
            self.displayArtist.set(str("None"))
        else:  # In the rest of cases, show its content, in the right way
            self.displayUser.set(str(self.currentUser))
            self.displayArtist.set("Artist: %s \n Relevance: %s" % (str(self.currentUser.getMost()), str(self.currentUser.getRelevance())))
            self.currentUser = self.searchIter.next()  # Advance node in the list

        self.frame.mainloop()


main()