from class_Queue import Queue
from class_User import User
from class_Artist import Artist

def parser(user_file):
	"Parses the file of users"
	estructuraDeDatos = Queue()
	with open(user_file,'r') as usersFile:
		for line in usersFile:
			tmpList = [] ## como si fuera tmp
			user = map(lambda x: x.split("&&"), line.split("||"))
			user[4] = map(lambda x: x.rsplit("::"), user[4])
			for element in user[4]:
				tmpArtist = Artist(element[0], int(element[1]))
				tmpList.append(tmpArtist)
			tmpUser = User(user[0],user[1],user[2],user[3],tmpList,user[5][0],float(user[5][1][:-1]))
			estructuraDeDatos.enqueue(tmpUser)					
	return estructuraDeDatos

# linea a linea, (/n) usuario
# || atributo
# && yuxtaposicion de artistas
# artista :: numero de reproducciones del artista