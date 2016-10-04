# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# Class that represents an Artist object
class Artist():
    def __init__(self, name = "EmptyName",
                 played = 0):
        self.name = name
        self.played = played # Builder of the class
        
    def __str__(self): # Overload of __str__
        return "Artist: %s \n Relevance: %s" %(str(self.name),str(self.played))