from class_PriorityQueue import PriorityQueue
from class_User import User
from class_Artist import Artist

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# All comments made in parserLastFM apply to this function
def parserP(user_file):
	"Parses the file of users"
	estructuraDeDatos = PriorityQueue()
	with open(user_file,'r') as usersFile:
		for line in usersFile:
			tmpList = []
			user = map(lambda x: x.split("&&"), line.split("||"))
			user[4] = map(lambda x: x.rsplit("::"), user[4])
			for element in user[4]:
				tmpArtist = Artist(element[0], int(element[1]))
				tmpList.append(tmpArtist)
			tmpUser = User(user[0][0],user[1][0],user[2][0],user[3][0],tmpList,user[5][0],float(user[5][1]))
			estructuraDeDatos.enqueue(tmpUser)					
	return estructuraDeDatos