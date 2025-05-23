
class Hash():
    def __init__(self, tamanio):
        self.tamanio_max = tamanio
        self.datos = ["*" for _ in range(tamanio)]

    def dibujar(self):
        label_indices = "Índice: "
        parts_indices = []
        for i in range(self.tamanio_max):
            parts_indices.append(f" {i} ")

        linea_indices_final = label_indices + "|" + "|".join(parts_indices) + "|"
        print(linea_indices_final)

        label_valores_con_datos = "Valor:  "
        parts_valores_con_datos = []
        for valor_dato in self.datos:
            parts_valores_con_datos.append(f"{valor_dato:^3}")

        linea_valores_con_datos_final = label_valores_con_datos + "|" + "|".join(parts_valores_con_datos) + "|"
        print(linea_valores_con_datos_final)

    def insertar(self,dato):
        if self.datos.count("*")==0:
            print("Lista llena!")
            return False
        
        posicion = dato%self.tamanio_max
        if self.datos[posicion] == "*":
            self.datos[posicion] = dato
            return True
        
        else:
            for i in range(posicion,self.tamanio_max):
                if self.datos[i] == "*":
                    self.datos[i] = dato
                    return True
            else:
                for i in range(0,posicion):
                    if self.datos[i] == "*":
                        self.datos[i] = dato
                        return True
            return False
    
    def buscar(self,datoBuscado):
        posicion = dato%self.tamanio_max
        if self.datos[posicion] == "*":
            self.datos[posicion] = datoBuscado
        else:
            for i in range(posicion,self.tamanio_max):
                if self.datos[i] == datoBuscado:
                    return True
            else:
                for i in range(0,posicion):
                    if self.datos[i] == datoBuscado:
                        return True
                    
            return False
        
tamanio = 5
datos = [7, 12, 17, 22, 27, 30]

hash = Hash(tamanio)
hash.dibujar()
for dato in datos:
    print(hash.insertar(dato))
    print()
    hash.dibujar()

print(hash.buscar(55))
print(hash.buscar(27))