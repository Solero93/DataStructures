# Busca recursivamente si un elemento está en una lista

def existeix(lista,x):
    if len(lista)==1:
        if lista==[x]:
            return True
        else:
            return False
    else:
        return existeix(lista[:len(lista)/2],x) or existeix(lista[len(lista)/2:],x)
        
# Gira una lista recursivamente

def girar(lista):
    if len(lista)==1:
        return lista
    else:
        return girar(lista[len(lista)/2:]) + girar(lista[:len(lista)/2])
    

# Ordena una lista recursivamente

def iguales(lista1,lista2):
    if len(lista1)==len(lista2) and len(lista1)==1 or len(lista2)==1:
        return lista1[0] == lista2[0]
    else:
        return iguales(lista1[len(lista1)/2:],lista2[len(lista2)/2:]) and iguales(lista1[:len(lista1)/2],lista2[:len(lista2)/2])
        
# Cuenta el número de ocurrencias de un elemento
    
def ocurrencia(lista,x):
    if len(lista)==1:
        if lista==[x]:
            return 1
        else:
            return 0
    else:
        return ocurrencia(lista[:len(lista)/2],x) + ocurrencia(lista[len(lista)/2:],x)
    
# màxim comú divisor de dos nombres    
def mcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    else:
        if a<b:
            return mcd(a,b%a)
        else:
            return mcd(a%b,b)

# máxim comú divisor divisor de una llista (patrocinat i aprobat per l'Arnau)
def mcdLlista(lista):
    if len(lista) == 1:
        return lista[0]
    if len(lista) == 2:
        return mcd(lista[0],lista[1])
    else:
        return mcdLlista([mcdLlista(lista[:len(lista)/2])] + [mcdLlista(lista[len(lista)/2:])])