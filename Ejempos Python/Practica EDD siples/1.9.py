def unirListas(lista1,lista2):
    for elemento in lista1:
        if elemento not in lista2:
            lista2.append(elemento)
    
    return lista2


print(unirListas([1,2,3,4,5,6,7,8],[3,11,6,37,21]))