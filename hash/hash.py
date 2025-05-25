class Hash():
    def __init__(self,tamanio):
        self.tamanio_max = tamanio
        self.datos = []
        for _ in range(tamanio):
            self.datos.append("*")

    def insertar(self,clave):
        indi = clave % self.tamanio_max
        if self.datos[indi] == "*":
            self.datos[indi] = clave
            return True

        for newindi in range(indi,self.tamanio_max):
            if self.datos[newindi] == "*":
                self.datos[newindi] = clave
                return True
            
        for newindi in range(indi):
            if self.datos[newindi] == "*":
                self.datos[newindi] = clave
                return True      
        return False
        
    def buscar(self,claveBuscada):
        indi = claveBuscada % self.tamanio_max
        if self.datos[indi] == claveBuscada:
            return True

        for newindi in range(indi,self.tamanio_max):
            if self.datos[newindi] == claveBuscada:
                return True
            
        for newindi in range(indi):
            if self.datos[newindi] == claveBuscada:
                return True
        return False

    def nuevotamanio(self):
        newsize = self.tamanio_max*2
        newhash = Hash(newsize)
        for elemento in self.datos:
            if elemento != "*":
                newhash.insertar(elemento)

        self.tamanio_max = newsize
        self.datos = newhash.datos
        return True

    def dibujar(self):
        label_indices = "Índice: "
        parts_indices = []
        for i in range(self.tamanio_max):
            parts_indices.append(f" {i} ")

        linea_indices_final = label_indices + "|" + "|".join(parts_indices) + "|"
        print(linea_indices_final)

        label_valores_con_datos = "Valor:  "
        parts_valores_con_datos = []
        cont = 0
        for valor_dato in self.datos:
            parts_valores_con_datos.append(f"{valor_dato:^{len(str(cont))+2}}")
            cont += 1

        linea_valores_con_datos_final = label_valores_con_datos + "|" + "|".join(parts_valores_con_datos) + "|"
        print(linea_valores_con_datos_final)

# MAIN
lista = [7, 12, 17, 22, 27,30]
hash = Hash(5)

hash.dibujar()
for elemento in lista:
    print()
    print(hash.insertar(elemento),"el elemento ",elemento)
    hash.dibujar()

print()
hash.nuevotamanio()
hash.dibujar()

print()
hash.insertar(30)
hash.dibujar()

print()
hash.nuevotamanio()
hash.dibujar()