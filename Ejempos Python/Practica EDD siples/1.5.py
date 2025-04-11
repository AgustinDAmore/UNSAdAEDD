def buscarElemento(elementoBuscado,lista):
    indice = 0
    for elemento in lista:
        if(elemento == elementoBuscado):
            return indice
        indice += 1
    return -1


def buscarElementoDos(elementoBuscado,lista):
    for indice in range(len(lista)):
        if(elementoBuscado == lista[indice]):
            return indice
    return -1

listaDenumeros = [1,2,3,4,5,6,7,8,9]

print(listaDenumeros.index(9))
print(buscarElemento(9,listaDenumeros))
print(buscarElementoDos(9,listaDenumeros))