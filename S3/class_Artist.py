class Artist():
    def __init__(self, name = "EmptyName",
                 played = 0):
        self.name = name
        self.played = played
        
    def __str__(self):
        return str(self.name) + ": " + str(self.played)