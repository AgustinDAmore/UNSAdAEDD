def clasificarNumeros(lista):
    pares = []
    impares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
        else:
            impares.append(elemento)

    return pares, impares

listaOriginal = [1,2,3,4,5,6,7,8,9]
print("lista:", listaOriginal)

pares, impares = clasificarNumeros(listaOriginal)

print("Pares:",pares)

print("Impares:",impares)