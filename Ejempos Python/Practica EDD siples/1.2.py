def EncuentraElMinimoYElMaximo(lista):
    if len(lista)!=0:
        minimo = lista[0]
        maximo = lista[0]
        for numero in lista:
            if numero > maximo:
                maximo = numero
            if numero < minimo:
                minimo = numero

        return (minimo,maximo)

    else:
        return "lista sin datos"


listaDeNumeros = [6,1,2,3,4,-1,5,6,7,89,69]
print(EncuentraElMinimoYElMaximo(listaDeNumeros))

listaDeNumeros = [69]
print(EncuentraElMinimoYElMaximo(listaDeNumeros))

listaDeNumeros.clear()
print(EncuentraElMinimoYElMaximo(listaDeNumeros))
