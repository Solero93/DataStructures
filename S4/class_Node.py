# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# Class Node will create objects for Stack and Queue
class Node():
	def __init__(self, data=None, after=None):
		self.data = data # The attribute that will stand for movie			
		self.after = after # The attribute that will point to the next element of the list
	def __str__(self):
		return str(self.data) # Overload of __str__