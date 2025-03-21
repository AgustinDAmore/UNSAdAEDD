def eliminarDuplicados(lista):
    listaSinDuplicados = []
    for elemento in lista:
        print("El elemento",elemento," se encuentra veces",listaSinDuplicados.count(elemento))
        if listaSinDuplicados.count(elemento)<1:
            listaSinDuplicados.append(elemento)
    
    return listaSinDuplicados


listaConDuplicados = [1,2,3,1,2,3,45,"Hola",6,7,8,88,5,3,4,99,7]
print(eliminarDuplicados(listaConDuplicados))

listaConDuplicados = [1,1,1,1,1,1,1,1,1,1,1,1,1]
print(eliminarDuplicados(listaConDuplicados))