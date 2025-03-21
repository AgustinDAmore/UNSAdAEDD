def invertirLista(lista):
    listaInvertida = []
    for elemento in lista:
        listaInvertida.insert(0,elemento)
    
    return listaInvertida

listaAInvertir = [1,2,3,4,5]
print(invertirLista(listaAInvertir))