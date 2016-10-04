from class_Artist import Artist

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# Class that represents the object user
class User():
    def __init__(self, uid="EmptyUid",
                 age = "EmptyAge",
                 gender = "EmptyGender",
                 country = "EmptyCountry",
                 songs = ["EmptyArtists"],
                 most = "EmptyArtist",
                 relevance = 0):
        self.uid = uid
        self.age = age
        self.gender = gender
        self.country = country
        self.songs = songs
        self.most = most
        self.relevance = relevance # Builder of class
        
    def __str__(self): # Overload of __str__
        return "User: %s \n Country: %s \n Age: %s \n Most played: %s %s" % (str(self.uid), str(self.country), str(self.age), str(self.most), str(self.relevance))
    
    def getMost(self): # Getter of self.most (encapsulation)
        return self.most
    
    def getRelevance(self): # Getter of self.relevance (encapsulation)
        return self.relevance
    
    def searchRelevance(self,begin,end): # Method to search in the application
        return (self.relevance <= end and self.relevance >= begin)
    
    def __cmp__(self, other): # Overload of __cmp__ in terms of relevance
        if self.relevance < other.relevance:
            return -1
        if self.relevance == other.relevance:
            return 0
        else:
            return 1
        
        