class hashLista():
    def __init__(self,tamanio):
        self.tamanio_max = tamanio
        self.datos = []
        for _ in range(tamanio):
            self.datos.append([])

    def agregar(self,clave):
        indi = clave % self.tamanio_max
        self.datos[indi].append(clave)

    def buscar(self,clave):
        indi = clave % self.tamanio_max
        for elemento in self.datos[indi]:
            if elemento == clave:
                return True
        return False

    def mostrar(self):
        print(self.datos)

# MAIN
hash = hashLista(10)
hash.mostrar()
for i in range(300,500):
    hash.mostrar()
    hash.agregar(i)

hash.mostrar()

print(hash.buscar(30))
print(hash.buscar(61))