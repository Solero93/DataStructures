from class_Artist import Artist

class User():
    #Setters y getters, xk son privados
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
        self.relevance = relevance
        
    def __str__(self):
        s = "User: %s \n Country: %s \n Age: %s \n Most played: %s" % (self.displayUser, self.displayCountry, self.displayAge, self.displayMostPlayed)
        return s
        