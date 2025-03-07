class Pila:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self): # esta_vacia
        return self.size == 0

    def push(self, elemento): # Apilar
        self.items.append(elemento)
        self.size +=1

    def pop(self): # Desapilar
        if not self.is_empty():
            return self.items.pop()
            self.size-=1
        else:
            return "La pila está vacía"

    def peek(self): # Tope
        if not self.is_empty():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def size(self): # Tamaño
        return self.size