# EDD Pila
class Pila():
    def __init__(self): # Constructor # generadoras
        self.items = []
        self.size = 0
    
    #modificadoras
    def apilar(self,item):
        self.items.append(item)
        self.size +=1

    def desapilar(self):
        if self.esta_vacia():
            print("La pila esta vacia")
        else:
            self.items.pop()
            self.size -=1
    # consultores

    def esta_vacia(self):
        return self.size == 0
    
    def tamano(self):
        return self.size
    
    def cima(self):
        if self.esta_vacia():
            return "La pila esta vacia"
        else:
            return self.items[-1]
    

# inicio de las pruebas
pila = Pila()
print(pila.esta_vacia())
pila.apilar(1)
pila.apilar(2)
pila.apilar(6)
pila.apilar(5)
print(pila.esta_vacia())
print(pila.cima())
print(pila.tamano())
pila.desapilar()
print(pila.cima())
print(pila.tamano())
print("comienzo del for")
for i in range(4):
    pila.desapilar()

print(pila.cima())
print(pila.tamano())