"https://treeconverter.com/?"
class NodoArbolBinarioBusqueda:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def vaciar(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbolBinarioBusqueda(valor)
        else:
            self.__insertar_recursivo(self.raiz, valor)

    def __insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbolBinarioBusqueda(valor)
            else:
                self.__insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbolBinarioBusqueda(valor)
            else:
                self.__insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self.__buscar_recursivo(self.raiz, valor)

    def __buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self.__buscar_recursivo(nodo.izquierda, valor)
        else:
            return self.__buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self.__eliminar_recursivo(self.raiz, valor)

    def __eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self.__eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self.__eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            sucesor = self.__encontrar_minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self.__eliminar_recursivo(nodo.derecha, sucesor.valor)

        return nodo

    def __encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def imprimir_arbol(self):
        if self.raiz is None:
            print("Arbol sin datos!")
        else:
            self.__imprimir_recursivo(self.raiz, 0)

    def __imprimir_recursivo(self, nodo, nivel):
        if nodo is not None:
            self.__imprimir_recursivo(nodo.derecha, nivel + 1)
            print('  ' * nivel + str(nodo.valor))
            self.__imprimir_recursivo(nodo.izquierda, nivel + 1)

abb = ArbolBinarioBusqueda()

abb.insertar(50)
abb.insertar(30)
abb.insertar(70)
abb.insertar(20)
abb.insertar(10)
abb.insertar(40)
abb.insertar(60)
abb.insertar(80)
abb.insertar(90)


print("Árbol Binario de Búsqueda:")
abb.imprimir_arbol()

print("\nBuscando el valor 40:", abb.buscar(40))
print("Buscando el valor 90:", abb.buscar(90))

abb.eliminar(30)
print("\nÁrbol después de eliminar el 30:")
abb.imprimir_arbol()

abb.eliminar(50)
print("\nÁrbol después de eliminar la raíz (50):")
abb.imprimir_arbol()

abb.vaciar()
abb.imprimir_arbol()

abb.insertar("B")
abb.insertar("G")
abb.insertar("A")
abb.insertar("H")
abb.insertar("I")
abb.insertar("C")
abb.insertar("D")
abb.insertar("J")
abb.insertar("E")
abb.insertar("F")

abb.imprimir_arbol()
print("\nBuscando el valor E:", abb.buscar("E"))