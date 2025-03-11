class Cola:
    def __init__(self):
        self.items = []
        self.tamanio = 0
    
    def encolar(self,item):
        self.items.insert(0,item)
        self.tamanio+=1
    
    def desencolar(self):
        if self.vacia():
            print(self)
        else:
            self.tamanio-=1
            return self.items.pop()
    
    def vacia(self):
        return self.tamanio==0
    
    def __repr__(self):
        if self.vacia():
            return "Cola: [] (Vacía)"
        else:
            elementos = ", ".join(map(str, self.items)) # Convierte los items a string y los une con comas
            return f"Cola: [{elementos}] (Atras -> Frente)"

    

cola = Cola()

print("Elemento desencolado:",cola.desencolar())

print("Cant elementos en la Cola: ",cola.tamanio)
print("Mostramos los elementos dentro de la cola: ",cola)

cola.encolar(1)
cola.encolar(2)
cola.encolar(5)
cola.encolar(4)

print("Cant elementos en la Cola: ",cola.tamanio)
print("Mostramos los elementos dentro de la cola: ",cola)

print("Elemento desencolado:",cola.desencolar())

print("Cant elementos en la Cola: ",cola.tamanio)
print("Mostramos los elementos dentro de la cola: ",cola)