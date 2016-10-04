# Entrega 1: 100 pel�culas
# Programa hecho por: Christian Jos� Soler
# Grupo F, Estructuras de Datos


# Creamos la funci�n parser, que nos devolver� la matriz de los datos de las 100 pel�culas de forma ordenada
def parser():

    # Hacemos una excepci�n con la apertura del archivo de las 100 pel�culas, por si el programa no lo encontrara:
    try:
        database = open("peliculas100.dat","r")
        database_lines = database.readlines() # Creamos una lista con sus l�neas
    except IOError:
        return -1
        

    # Creamos una matriz vac�a, de 14 columnas y 100 filas(que corresponde con el n�mero de l�neas)
    matrix = [['']*(14) for x in (range(len(database_lines)))]


    # Separamos las l�neas en funci�n del s�mbolo "|" que marca la separaci�n entre campos
    separated = [] 
    for line in database_lines:
        separated.append(line.split("|")) # Los metemos en una lista nueva, separated

    count_row = 0       # Contador de la fila en que estamos en la matriz
    count_column = 0    # Contador de la columna en que estamos en la matriz


    # Empezamos un bucle para rellenar la matriz que vamos a devolver
    
    for line in separated:  # Para cada l�nea del archivo separado
        for element in line: # Para cada elemento de dicha l�nea
            
            if "&&" in element:                 # Si "&&" forma parte del elemento, lo separamos en funci�n de "&&"
                element = element.split("&&")   # Creando as� un elemento tipo lista con los elementos ya separados
                
            matrix[count_row][count_column] = element   # A�adimos el elemento a la posici�n en que estamos en la matriz 
            count_column += 1                           # Cambiamos de columna para a�adir el siguiente elemento de la l�nea
            
        count_column = 0    # Cuando se nos hayan acabado los elementos en la l�nea, volvemos al inicio de columnas
        count_row +=1       # Y cambiamos de fila en la matriz


    database.close() # Cerramos el archivo al acabar
    
    return matrix # Devolvemos la matriz resultante

parser()

def main():
    # Definimos un diccionario con los diferentes par�metros que corresponden a las vi�etas de las columnas de la matriz
    parametres = {1:"Title", 2:"Director", 3:"Cast", 4:"Producer", 5:"Writer", 6:"Country",7:"Language",
                  8:"Year", 9:"Genres", 10:"Votes", 11:"Rating", 12:"Runtime", 13:"Plot", 14:"Cover Url"}
 
    count_parametres = 1  # Establecemos un contador para uso posterior en la impresi�n por pantalla
    
    estructuraDatos = []
    estructuraDatos = parser() # Asignamos la matriz devuelta por parser() a una lista vac�a, estructuraDatos
    if estructuraDatos == -1:
        print "No s'ha trobat el fitxer" # Si nos da error el fichero, imprimimos mensaje y acabamos
        
    else:
        
    # Ahora empezamos un bucle para la impresi�n por pantalla de los resultados:

        count_movies = 1 # Establecemos un contador para poder seguir en la impresi�n por pantalla en qu� pel�cula estamos
        
        for campo in estructuraDatos:   # Para cada fila de la matriz:
            print "THE",count_movies,". MOVIE:" # Imprimimos en qu� pel�cula estamos
            
            for elemento in campo:  # Para cada elemento de la fila:
                print parametres[count_parametres] + ":" # Imprimimos la vi�eta en qu� estamos

                # Si el elemento es una lista, ya que en cuyo caso es que hubo una separaci�n elemento.split("&&"):
                if isinstance(elemento,list): 
                    for a in elemento:      # Empezamos un bucle de impresi�n:
                        print "\t" + a      # A�adimos un tabulador al principio del elemento de la lista de elementos            
                else:
                    print "\t" + elemento   # En el resto de casos imprimimos el elemento precedido por un tabulador

                count_parametres += 1   # Cambiamos de vi�eta
                print ""                # Hacemos una separaci�n

            count_parametres = 1    # Al acabar con la fila, volvemos al principio de las vi�etas
            print ""                # Hacemos una separaci�n
            count_movies += 1       # Cambiamos de pel�cula
        
main()
