import sys

# Definición del Nodo del Árbol AVL
class NodoAVL:
    def __init__(self, clave):
        self.clave = clave  # Valor del nodo
        self.izquierda = None  # Hijo izquierdo
        self.derecha = None  # Hijo derecho
        self.altura = 1  # Altura del subárbol rootedo en este nodo (hoja tiene altura 1)

# Definición de la clase Árbol AVL
class ArbolAVL:

    def __init__(self):
        self.raiz = None

    # --- Funciones de Ayuda ---

    def __altura(self, nodo):
        """Obtiene la altura de un nodo (0 si el nodo es None)."""
        if not nodo:
            return 0
        return nodo.altura

    def __balance(self, nodo):
        """Calcula el factor de balance de un nodo."""
        if not nodo:
            return 0
        # Balance = Altura(Subárbol Izquierdo) - Altura(Subárbol Derecho)
        return self.__altura(nodo.izquierda) - self.__altura(nodo.derecha)

    def __actualizar__altura(self, nodo):
        """Recalcula y actualiza la altura de un nodo."""
        if not nodo:
            return 0 # Altura de un nodo nulo es 0
        nodo.altura = 1 + max(self.__altura(nodo.izquierda), self.__altura(nodo.derecha))
        return nodo.altura

    def __min_valor_nodo(self, nodo):
        """Encuentra el nodo con el valor mínimo en un subárbol (el más a la izquierda)."""
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # --- Rotaciones ---

    def __rotacion_derecha(self, z):
        """Realiza una rotación simple a la derecha."""
        #       z                 y
        #      / \               / \
        #     y   T4   ---->    x   z
        #    / \               / \ / \
        #   x   T3            T1 T2 T3 T4
        #  / \
        # T1  T2
        print(f"Rotación Derecha en {z.clave}")
        y = z.izquierda
        T3 = y.derecha

        # Realizar rotación
        y.derecha = z
        z.izquierda = T3

        # Actualizar alturas (¡el orden importa!)
        self.__actualizar__altura(z) # Actualizar z primero porque ahora es hijo
        self.__actualizar__altura(y) # Actualizar y (nueva raíz del subárbol)

        # Retornar la nueva raíz del subárbol rotado
        return y

    def __rotacion_izquierda(self, y):
        """Realiza una rotación simple a la izquierda."""
        #     y                  z
        #    / \                / \
        #   T1  z     ---->    y   T4
        #      / \            / \ / \
        #     T2  x          T1 T2 T3 T4
        #        / \
        #       T3 T4
        print(f"Rotación Izquierda en {y.clave}")
        z = y.derecha
        T2 = z.izquierda

        # Realizar rotación
        z.izquierda = y
        y.derecha = T2

        # Actualizar alturas (¡el orden importa!)
        self.__actualizar__altura(y) # Actualizar y primero porque ahora es hijo
        self.__actualizar__altura(z) # Actualizar z (nueva raíz del subárbol)

        # Retornar la nueva raíz del subárbol rotado
        return z

    # --- Operación de Inserción ---

    def insertar(self, clave):
        """Interfaz pública para insertar una clave."""
        print(f"\nInsertando {clave}...")
        self.raiz = self.__insertar_recursivo(self.raiz, clave)

    def __insertar_recursivo(self, raiz_actual, clave):
        """Función recursiva para insertar una clave y balancear."""

        # 1. Realizar inserción estándar de BST
        if not raiz_actual:
            print(f"  -> Insertado {clave} como nuevo nodo.")
            return NodoAVL(clave)
        elif clave < raiz_actual.clave:
            raiz_actual.izquierda = self.__insertar_recursivo(raiz_actual.izquierda, clave)
        elif clave > raiz_actual.clave: # Evita duplicados (o puedes manejarlos de otra forma)
             raiz_actual.derecha = self.__insertar_recursivo(raiz_actual.derecha, clave)
        else:
            print(f"  -> Clave {clave} ya existe, no se inserta.")
            return raiz_actual # Clave ya existe

        # 2. Actualizar la altura del nodo ancestro actual
        self.__actualizar__altura(raiz_actual)

        # 3. Obtener el factor de balance de este nodo
        balance = self.__balance(raiz_actual)
        print(f"  Nodo {raiz_actual.clave}: Altura={raiz_actual.altura}, Balance={balance}")

        # 4. Si el nodo está desbalanceado, realizar rotaciones
        # Caso Izquierda-Izquierda (LL)
        if balance > 1 and clave < raiz_actual.izquierda.clave:
            print("  -> Desbalance detectado: Caso Izquierda-Izquierda (LL)")
            return self.__rotacion_derecha(raiz_actual)

        # Caso Derecha-Derecha (RR)
        if balance < -1 and clave > raiz_actual.derecha.clave:
            print("  -> Desbalance detectado: Caso Derecha-Derecha (RR)")
            return self.__rotacion_izquierda(raiz_actual)

        # Caso Izquierda-Derecha (LR)
        if balance > 1 and clave > raiz_actual.izquierda.clave:
            print("  -> Desbalance detectado: Caso Izquierda-Derecha (LR)")
            # Rotar izquierda en el hijo izquierdo primero
            raiz_actual.izquierda = self.__rotacion_izquierda(raiz_actual.izquierda)
            # Luego rotar derecha en el nodo actual
            return self.__rotacion_derecha(raiz_actual)

        # Caso Derecha-Izquierda (RL)
        if balance < -1 and clave < raiz_actual.derecha.clave:
            print("  -> Desbalance detectado: Caso Derecha-Izquierda (RL)")
            # Rotar derecha en el hijo derecho primero
            raiz_actual.derecha = self.__rotacion_derecha(raiz_actual.derecha)
            # Luego rotar izquierda en el nodo actual
            return self.__rotacion_izquierda(raiz_actual)

        # Si no hubo desbalance o ya se corrigió, retornar la raíz (posiblemente actualizada)
        return raiz_actual

    # --- Operación de Borrado ---

    def borrar(self, clave):
        """Interfaz pública para borrar una clave."""
        print(f"\nBorrando {clave}...")
        if not self.raiz:
             print(f"  -> Árbol vacío, no se puede borrar {clave}.")
             return
        self.raiz = self.__borrar_recursivo(self.raiz, clave)
        if self.raiz: # Actualizar altura de la raíz si no quedó vacía
             self.__actualizar__altura(self.raiz)


    def __borrar_recursivo(self, raiz_actual, clave):
        """Función recursiva para borrar una clave y balancear."""

        # 1. Realizar borrado estándar de BST
        if not raiz_actual:
            print(f"  -> Clave {clave} no encontrada.")
            return raiz_actual # Clave no encontrada

        elif clave < raiz_actual.clave:
            raiz_actual.izquierda = self.__borrar_recursivo(raiz_actual.izquierda, clave)
        elif clave > raiz_actual.clave:
            raiz_actual.derecha = self.__borrar_recursivo(raiz_actual.derecha, clave)
        else: # Nodo con la clave a borrar encontrado
            print(f"  -> Nodo {clave} encontrado para borrar.")
            # Caso 1: Nodo con 0 o 1 hijo
            if raiz_actual.izquierda is None:
                temp = raiz_actual.derecha
                print(f"  -> Borrando nodo {clave} (sin hijo izquierdo). Reemplazando con {'nodo ' + str(temp.clave) if temp else 'None'}.")
                raiz_actual = None # Liberar memoria (en Python es automático)
                return temp # El hijo derecho (o None) sube
            elif raiz_actual.derecha is None:
                temp = raiz_actual.izquierda
                print(f"  -> Borrando nodo {clave} (sin hijo derecho). Reemplazando con {'nodo ' + str(temp.clave) if temp else 'None'}.")
                raiz_actual = None
                return temp # El hijo izquierdo sube

            # Caso 2: Nodo con 2 hijos
            # Obtener el sucesor inorden (el menor en el subárbol derecho)
            temp = self.__min_valor_nodo(raiz_actual.derecha)
            print(f"  -> Nodo {clave} tiene dos hijos. Sucesor inorden es {temp.clave}.")

            # Copiar el valor del sucesor inorden a este nodo
            raiz_actual.clave = temp.clave
            print(f"  -> Copiando {temp.clave} a nodo {clave}. Borrando recursivamente {temp.clave} del subárbol derecho.")

            # Borrar el sucesor inorden del subárbol derecho
            raiz_actual.derecha = self.__borrar_recursivo(raiz_actual.derecha, temp.clave)

        # Si el árbol tenía solo un nodo, simplemente retornar
        if raiz_actual is None:
            return raiz_actual

        # 2. Actualizar la altura del nodo actual
        self.__actualizar__altura(raiz_actual)

        # 3. Obtener el factor de balance
        balance = self.__balance(raiz_actual)
        print(f"  Nodo {raiz_actual.clave}: Altura={raiz_actual.altura}, Balance={balance}")

        # 4. Si está desbalanceado, realizar rotaciones (similar a inserción)
        # Caso Izquierda-Izquierda (LL)
        if balance > 1 and self.__balance(raiz_actual.izquierda) >= 0:
             print("  -> Desbalance post-borrado detectado: Caso Izquierda-Izquierda (LL)")
             return self.__rotacion_derecha(raiz_actual)

        # Caso Izquierda-Derecha (LR)
        if balance > 1 and self.__balance(raiz_actual.izquierda) < 0:
            print("  -> Desbalance post-borrado detectado: Caso Izquierda-Derecha (LR)")
            raiz_actual.izquierda = self.__rotacion_izquierda(raiz_actual.izquierda)
            return self.__rotacion_derecha(raiz_actual)

        # Caso Derecha-Derecha (RR)
        if balance < -1 and self.__balance(raiz_actual.derecha) <= 0:
            print("  -> Desbalance post-borrado detectado: Caso Derecha-Derecha (RR)")
            return self.__rotacion_izquierda(raiz_actual)

        # Caso Derecha-Izquierda (RL)
        if balance < -1 and self.__balance(raiz_actual.derecha) > 0:
            print("  -> Desbalance post-borrado detectado: Caso Derecha-Izquierda (RL)")
            raiz_actual.derecha = self.__rotacion_derecha(raiz_actual.derecha)
            return self.__rotacion_izquierda(raiz_actual)

        # Retornar la raíz (posiblemente actualizada)
        return raiz_actual

    # --- Operación de Búsqueda ---
    def buscar(self, clave):
        """Busca una clave en el árbol."""
        return self.__buscar_recursivo(self.raiz, clave)

    def __buscar_recursivo(self, raiz_actual, clave):
        if not raiz_actual:
            return False
        if clave == raiz_actual.clave:
            return True
        elif clave < raiz_actual.clave:
            return self.__buscar_recursivo(raiz_actual.izquierda, clave)
        else:
            return self.__buscar_recursivo(raiz_actual.derecha, clave)


    # --- Recorridos para Visualización ---

    def preorden(self):
        """Realiza un recorrido preorden (Raíz, Izquierda, Derecha)."""
        nodos = []
        self.__preorden_recursivo(self.raiz, nodos)
        print("Recorrido Preorden:", nodos)

    def __preorden_recursivo(self, nodo, nodos):
        if nodo:
            # Incluye clave y altura para depuración
            nodos.append(f"{nodo.clave}(h={nodo.altura},b={self.__balance(nodo)})")
            self.__preorden_recursivo(nodo.izquierda, nodos)
            self.__preorden_recursivo(nodo.derecha, nodos)

    def inorden(self):
        """Realiza un recorrido inorden (Izquierda, Raíz, Derecha). Útil para ver ordenado."""
        nodos = []
        self.__inorden_recursivo(self.raiz, nodos)
        print("Recorrido Inorden:", nodos)

    def __inorden_recursivo(self, nodo, nodos):
         if nodo:
            self.__inorden_recursivo(nodo.izquierda, nodos)
            nodos.append(nodo.clave) # Solo la clave para ver orden
            self.__inorden_recursivo(nodo.derecha, nodos)

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    miArbol = ArbolAVL()
    claves = [10, 20, 30, 40, 50, 25] # Causa varias rotaciones

    for clave in claves:
        miArbol.insertar(clave)
        miArbol.preorden() # Muestra estado después de cada inserción
        miArbol.inorden()  # Verifica que sigue ordenado

    print("\n--- Búsquedas ---")
    print(f"Buscar 30: {miArbol.buscar(30)}")
    print(f"Buscar 99: {miArbol.buscar(99)}")


    print("\n--- Borrados ---")
    # Borrar nodo hoja (40) - Sin rotación necesaria inicialmente
    miArbol.borrar(40)
    miArbol.preorden()
    miArbol.inorden()

    # Borrar nodo con un hijo (50) - Sin rotación
    miArbol.borrar(50)
    miArbol.preorden()
    miArbol.inorden()

    # Borrar nodo raíz (30) - que tiene 2 hijos y causará rebalanceo
    miArbol.borrar(30)
    miArbol.preorden()
    miArbol.inorden()

    # Borrar nodo que causa desbalance complejo (10)
    miArbol.borrar(10)
    miArbol.preorden()
    miArbol.inorden()