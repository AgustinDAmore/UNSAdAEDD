""" 
En el siguiente archivo veremos como pasar N datos en una sola variable
si queremos sumar mas de dos numeros podemos hacer def sumar(num1,num2,num3) 
y si ahora queremos sumar 4? def sumar(num1,num2,num3,num4)
y si queremos volver a sumar solo 3 numeros?.
en lugar de estar modificando la funcion con la cant de datos a pasar 
podemos pasarle una lista de numeros! de esta forma podemos sumar 1 o N numeros!
sin tener que modificar la funcion constantemente
"""
def sumarnumeros(listaConNumeros): # solo necesita un unico parametro
    sumaTotal = 0 # en esta variable vamos a guardar la suma de todos los numeros
    for numero in listaConNumeros: # recorremos uno a uno los numeros dentro de a lista
        sumaTotal += numero # los vamos sumando
    return sumaTotal # devolvemos la suma total

print(sumarnumeros([1,2,3,4,5])) # le pasamos una lista llena de numeros
# y si quiero pasar los numeros por teclado en lugar de pasar una lista pre armada?
lista = []
for num in range(5):
    lista.append(int(input("Ingrese el numero: ")))
print(sumarnumeros(lista))
# la forma anterior solo nos permite sumar 5 numeros.
# si queremos sumar la cantidad de numeros que el usuario quiere debemos solicitarlo

# a continuacion te invito a crear dicha forma con lo aprendido arriba
# Su codigo aqui