class Pila:
    def __init__(self):
        self.items = []
        self.size = 0

    def esta_vacia(self):
        return self.size == 0

    def apilar(self, elemento):
        self.items.append(elemento)
        self.size +=1

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
            self.size-=1
        else:
            return "La pila está vacía"

    def tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def tamano(self):
        return self.size