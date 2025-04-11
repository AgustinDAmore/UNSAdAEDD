def contadorDeNumeros(lista):
    diccionario = {}
    for elemento in lista:
        if elemento in diccionario.keys():
            cont = diccionario[elemento]
            diccionario[elemento] = cont+1
        else:
            diccionario[elemento] = 1
        
    return diccionario

print(contadorDeNumeros([1,2,3,4,5,6,7,8,9,6]))
            



