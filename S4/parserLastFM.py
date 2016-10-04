from class_Queue import Queue
from class_User import User
from class_Artist import Artist

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

def parser(user_file):
	"Parses the file of users"
	estructuraDeDatos = Queue() # Declaration of the Queue to return
	with open(user_file,'r') as usersFile:
		for line in usersFile: # For each line of the file
			tmpList = []
			user = map(lambda x: x.split("&&"), line.split("||"))
			user[4] = map(lambda x: x.rsplit("::"), user[4]) # Users are split by attributes
			for element in user[4]:
				tmpArtist = Artist(element[0], int(element[1]))
				tmpList.append(tmpArtist)
			tmpUser = User(user[0][0],user[1][0],user[2][0],user[3][0],tmpList,user[5][0],float(user[5][1])) # The User object is made from its attributes
			estructuraDeDatos.enqueue(tmpUser) # It's added to the Queue 				 	
	return estructuraDeDatos # The parsed file is returned as a Queue