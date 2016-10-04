# Entrega 1: 100 películas
# Programa hecho por: Christian José Soler
# Grupo F, Estructuras de Datos


# Creamos la función parser, que nos devolverá la matriz de los datos de las 100 películas de forma ordenada
def parser():

    # Hacemos una excepción con la apertura del archivo de las 100 películas, por si el programa no lo encontrara:
    try:
        database = open("peliculas100.dat","r")
        database_lines = database.readlines() # Creamos una lista con sus líneas
    except IOError:
        return -1
        

    # Creamos una matriz vacía, de 14 columnas y 100 filas(que corresponde con el número de líneas)
    matrix = [['']*(14) for x in (range(len(database_lines)))]


    # Separamos las líneas en función del símbolo "|" que marca la separación entre campos
    separated = [] 
    for line in database_lines:
        separated.append(line.split("|")) # Los metemos en una lista nueva, separated

    count_row = 0       # Contador de la fila en que estamos en la matriz
    count_column = 0    # Contador de la columna en que estamos en la matriz


    # Empezamos un bucle para rellenar la matriz que vamos a devolver
    
    for line in separated:  # Para cada línea del archivo separado
        for element in line: # Para cada elemento de dicha línea
            
            if "&&" in element:                 # Si "&&" forma parte del elemento, lo separamos en función de "&&"
                element = element.split("&&")   # Creando así un elemento tipo lista con los elementos ya separados
                
            matrix[count_row][count_column] = element   # Añadimos el elemento a la posición en que estamos en la matriz 
            count_column += 1                           # Cambiamos de columna para añadir el siguiente elemento de la línea
            
        count_column = 0    # Cuando se nos hayan acabado los elementos en la línea, volvemos al inicio de columnas
        count_row +=1       # Y cambiamos de fila en la matriz


    database.close() # Cerramos el archivo al acabar
    
    return matrix # Devolvemos la matriz resultante

parser()

def main():
    # Definimos un diccionario con los diferentes parámetros que corresponden a las viñetas de las columnas de la matriz
    parametres = {1:"Title", 2:"Director", 3:"Cast", 4:"Producer", 5:"Writer", 6:"Country",7:"Language",
                  8:"Year", 9:"Genres", 10:"Votes", 11:"Rating", 12:"Runtime", 13:"Plot", 14:"Cover Url"}
 
    count_parametres = 1  # Establecemos un contador para uso posterior en la impresión por pantalla
    
    estructuraDatos = []
    estructuraDatos = parser() # Asignamos la matriz devuelta por parser() a una lista vacía, estructuraDatos
    if estructuraDatos == -1:
        print "No s'ha trobat el fitxer" # Si nos da error el fichero, imprimimos mensaje y acabamos
        
    else:
        
    # Ahora empezamos un bucle para la impresión por pantalla de los resultados:

        count_movies = 1 # Establecemos un contador para poder seguir en la impresión por pantalla en qué película estamos
        
        for campo in estructuraDatos:   # Para cada fila de la matriz:
            print "THE",count_movies,". MOVIE:" # Imprimimos en qué película estamos
            
            for elemento in campo:  # Para cada elemento de la fila:
                print parametres[count_parametres] + ":" # Imprimimos la viñeta en qué estamos

                # Si el elemento es una lista, ya que en cuyo caso es que hubo una separación elemento.split("&&"):
                if isinstance(elemento,list): 
                    for a in elemento:      # Empezamos un bucle de impresión:
                        print "\t" + a      # Añadimos un tabulador al principio del elemento de la lista de elementos            
                else:
                    print "\t" + elemento   # En el resto de casos imprimimos el elemento precedido por un tabulador

                count_parametres += 1   # Cambiamos de viñeta
                print ""                # Hacemos una separación

            count_parametres = 1    # Al acabar con la fila, volvemos al principio de las viñetas
            print ""                # Hacemos una separación
            count_movies += 1       # Cambiamos de película
        
main()
