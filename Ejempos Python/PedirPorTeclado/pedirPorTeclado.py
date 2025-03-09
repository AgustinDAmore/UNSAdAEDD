"""
En este archivo arenderemos a perdir datos por teclado
la funcion para pedir datos por teclado en python es mediante input
"""
nombre = input("Ingrese su nombre: ")
print("Hola!",nombre)
# si no nombramos ningun tipo de dato el por defecto es un string.
# en caso de querer pasar algun tipo de dato lo debemos nombrar y entre parentesis envolver la funcion input
numeroEntero = int(input("ingrese un numero entero: ")) # de esta forma pedimos un numero entero
numeroFlotante = float(input("ingrese un numero: ")) # de esta forma pedimos un numero flotante (con parte decimal)
# NOTA: Los decimales son con . (punto) ej: 3.1415 NO 3,1415
print(numeroEntero,"+",numeroFlotante,"=",numeroEntero+numeroFlotante) # mostramos los numeros ingresados y su suma

# Ahora muestre el siguiente mensaje "El la suma que ingreso (nombre) dio como resultado (suma)"
# Su codigo aqui