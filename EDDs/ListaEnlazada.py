class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        ultimo_nodo = self.cabeza
        while ultimo_nodo.siguiente:
            ultimo_nodo = ultimo_nodo.siguiente
        ultimo_nodo.siguiente = nuevo_nodo

    def insertar_en_indice(self, dato, indice):
        if indice < 0:
            print("El índice debe ser mayor o igual que 0.")
            return
        if indice == 0:
            self.insertar_al_principio(dato)
            return
        nuevo_nodo = Nodo(dato)
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual and posicion < indice - 1:
            nodo_actual = nodo_actual.siguiente
            posicion += 1
        if nodo_actual is None:
            print("Índice fuera de rango.")
            return
        nuevo_nodo.siguiente = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo

    def eliminar_al_principio(self):
        if self.cabeza is None:
            return
        self.cabeza = self.cabeza.siguiente

    def eliminar_al_final(self):
        if self.cabeza is None:
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        nodo_actual = self.cabeza
        while nodo_actual.siguiente.siguiente:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = None

    def eliminar_en_indice(self, indice):
        if self.cabeza is None:
            return
        if indice < 0:
            print("El índice debe ser mayor o igual que 0.")
            return
        if indice == 0:
            self.eliminar_al_principio()
            return
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual.siguiente and posicion < indice - 1:
            nodo_actual = nodo_actual.siguiente
            posicion += 1
        if nodo_actual.siguiente is None:
            print("Índice fuera de rango.")
            return
        nodo_actual.siguiente = nodo_actual.siguiente.siguiente

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("Ninguno")