class Xorra():
    def __init__(self, i=4):
        self.i = i
    def __str__(self):
        return str(self.i)

    
a = Xorra("se")
b = Xorra()

lista = [a,b]
print a
print ", ".join(lista)