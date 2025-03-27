class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar_nodo(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente

    def recorrer_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")
        
    def recorrer_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def insertar_en_indice(self, indice, dato):
        if indice == 0:
            self.insertar_al_principio(dato)
        elif indice >= self.obtener_longitud():
            self.insertar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(indice - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo

    def obtener_longitud(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def eliminar_en_indice(self, indice):
        if indice == 0:
            if self.cabeza:
                self.cabeza = self.cabeza.siguiente
                if self.cabeza:
                    self.cabeza.anterior = None
                else:
                    self.cola = None
        else:
            actual = self.cabeza
            for _ in range(indice):
                if actual is None:
                    return  # Índice fuera de rango
                actual = actual.siguiente
            if actual:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cola:
                    self.cola = actual.anterior

# Ejemplo de uso
lista = ListaDoblementeEnlazada()

# Insertar al final
lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_final(3)
print("Lista después de insertar al final:")
lista.mostrar_lista()  # Salida: 1 <-> 2 <-> 3 <-> None

# Insertar al principio
lista.insertar_al_principio(0)
print("\nLista después de insertar al principio:")
lista.mostrar_lista()  # Salida: 0 <-> 1 <-> 2 <-> 3 <-> None

# Insertar en índice específico
lista.insertar_en_indice(2, 5)
print("\nLista después de insertar en índice 2:")
lista.mostrar_lista()  # Salida: 0 <-> 1 <-> 5 <-> 2 <-> 3 <-> None

# Eliminar nodo por valor
lista.eliminar_nodo(2)
print("\nLista después de eliminar el nodo con valor 2:")
lista.mostrar_lista()  # Salida: 0 <-> 1 <-> 5 <-> 3 <-> None

# Eliminar nodo por índice
lista.eliminar_en_indice(1)
print("\nLista después de eliminar el nodo en el índice 1:")
lista.mostrar_lista()  # Salida: 0 <-> 5 <-> 3 <-> None

print("Recorrido hacia adelante:")
lista.recorrer_adelante()  # Salida: 0 <-> 5 <-> 3 <-> None

print("\nRecorrido hacia atrás:")
lista.recorrer_atras()  # Salida: 3 <-> 5 <-> 0 <-> None