# 1. Variables y tipos de datos
nombre = "Python"  # Cadena de texto (string)
version = 3.9       # Número de punto flotante (float)
es_genial = True    # Booleano (boolean)
numeros = [1, 2, 3, 4, 5]  # Lista (list)
tupla = (6, 7, 8)           # Tupla (tuple)
# nombre(string), numeros(list), tupla(tuple) cada elemento tiene un indice que va de 0 a N
print("Obtenemos la primera letra del string ",nombre[0])
print("Obtenemos el primer numero de la lista ",numeros[0])
print("Obtenemos el primer numero de la tupla ",tupla[0])

diccionario = {"clave": "valor", "numero": 10}  # Diccionario (dict)
print(diccionario.get("clave")) # pasando la clave nos devuelve el valor de la misma
# si en lugar de clave escribimos "numero" nos devoelve 10

# 2. Operaciones básicas
suma = 10 + 5 # dos int se suman y devuelven un int.
print("La suma de la linea 17 da: ",suma)
suma2 = 10 + 4.6 # un int + un float devuelven un float
print("La suma de la linea 19 da: ",suma)
concatenar = "Hola " + "Chicos" # los string al usar el operador + se concatenan
print("La unisn de los dos string de la linea 21 dan "+concatenar) # PODEMOS UNIR EL STRING DEL PRINT CON concatenar
# AMBOS SON DEL MISMO TIPO DE DATO. CUANDO MEZCLAMOS TIPOS DE DATOS TENEOS QUE USAR , DENTRO DE LOS PRINT
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5

# 3. Estructuras de control
if suma > resta:
    print("La suma es mayor que la resta.")
else:
    print("La resta es mayor o igual que la suma.")

for numero in numeros: # Extraemos uno a uno los datos dentro de la variable numeros declarada en la linea 5 numeros es un list
    print(numero)

contador = 0
while contador < 3: # mientras contador sea menor a 3 mostramos el valor actual de contador
    print("Contador:", contador)
    contador += 1

# 4. Funciones
def saludar(nombre): # def es una funcion en python. lo que esta dentro de los parentesis son los parametros pedidos por la funcion
    # en este caso solo se pide uno llamado "nombre" 
    """Esta función saluda a la persona con el nombre proporcionado."""
    print(f"¡Hola, {nombre}!")

saludar("Mundo") # aca llamamos a la funcion saludar. pasandole un string como parametro

# 5. Clases y objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 30)
persona1.presentarse()

# 6. Manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError: 
    print("¡No se puede dividir por cero!")

