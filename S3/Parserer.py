from class_Movie import Movie # Import of Movie class
import sys

class Parser():
    def parserFile(self,filename):
	"""Function that parses the file "peliculas100.dat"""
	
	try: # parser() tries to open the file "peliculas100.dat" in reading mode and read its lines:
	    database = open(filename,"r")
	    database_lines = database.readlines()
	
	except IOError: # In case it can't for any reason, it shows a message and finishes the whole process
	    print "File not found, the program will now close."
	    sys.exit()
    
	# We parse the file in the same manner as we did in "Entrega1"
	matrix = [['']*(14) for x in (range(len(database_lines)))]
    
	separated = []
	for line in database_lines:
	    separated.append(line.split("|"))
    
	count_row = 0
	count_column = 0
    
	for line in separated:
	    for element in line:
		if "&&" in element:
		    element = element.split("&&")
		matrix[count_row][count_column] = element
		count_column += 1
	    count_column = 0
	    count_row += 1
	database.close()
	lista = self.makeMovieList(matrix)
	return lista
    
    def makeMovieList(self,matrix):
	movieList = []
	
	for i in range(100): # We assign the attributes of each movie with the contstructor of the class 
	    peli = Movie(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],matrix[i][5],matrix[i][6],matrix[i][7],matrix[i][8],matrix[i][9],matrix[i][10],matrix[i][11],matrix[i][12],matrix[i][13])
	
	    movieList.append(peli) # We add the element to the list of movies
	return movieList