class Cola():
    def __init__(self,Elementos = None): # Generador
        self.elementos = []
        if Elementos != None:
            for item in Elementos:
                self.elementos.insert(0,item) # {Pos: la pila no esta vacía} 
        self.tamanio = len(self.elementos)

    # Operadores Basicos
    def son_iguales(self, Cola2) -> bool:
        if type(Cola2) != Cola: # Si a y b son dos pilas
            return False
        
        if len(self.elementos) != len(Cola2.elementos):
            return False # Las longitudes de a y b son iguales
        
        for elem, elem2 in zip(self.elementos, Cola2.elementos):
            if elem != elem2: # cada elemento en a es igual al correspondiente elemento en b. 
                return False
        return True

    def tamaño(self) -> int:
        return self.tamanio
    
    def mostrar(self):
        print(f"inicio -> {str(self.elementos).replace(","," ->").replace("'","")}")
    
    def es_vacia(self) -> bool:
        return self.tamanio == 0
    
    def frente(self) -> type:
        return self.elementos[-1]
    
    # Otras operaciones 
    def encolar(self,elemento):
        # {Pos: la pila no esta vacía} 
        try:
            for item in elemento:
                self.elementos.insert(0,item)
        except TypeError:
            self.elementos.insert(0,elemento)
    
    def desencolar(self) -> type:
        """
        {Pre: la pila tiene al menos un elemento} 
        {Pos: la pila perdió el tope que tenía antes de desapilar}
        """
        return self.elementos.pop()
#################################################################     
a = Cola() # {Post: La pila retornada esta vacía}
b = Cola("aloh") # {Post: La pila contiene apilados los elementos de la secuencia recibida}


a.mostrar()
b.mostrar()

print(a.tamaño())
print(b.tamaño())

print(a.son_iguales(b))

b.encolar(12)
b.mostrar()
print(b.frente())
b.desencolar()
b.mostrar()
