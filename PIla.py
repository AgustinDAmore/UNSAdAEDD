# EDD Pila
class Pila():
    # el usuario que use nuestra EDD se encuentra abstraido toda esta seccion
    def __init__(self): # Constructor 
        self.items = [] # inicailizamos una lista vacia al momento de crear nuetra pila
        self.size = 0 # inicializamos un contador el cual nos va a ayudar para saber si 
        # la pila cuenta con elementos cargardos
    
    #modificadoras # estas son todas la funciones que modifican internamente nuestra EDD
    def apilar(self,item):
        self.items.append(item) # agregamos el elemento dentro de la pila
        self.size +=1 # incrementamos en uno el tamaño de la pila
        return item # devolvemos el item agregado a la pila

    def desapilar(self):
        if self.esta_vacia(): # si no hay elementos para quitar mostramos el print
            return "La pila esta vacia"
        else: # si no 
            self.size -=1 # decrementamos en 1 el tamaño de la pila
            return self.items.pop() # devolvemos el elemento quitado de la pila

    # consultores # estas son todas la funciones que NO modifican internamente nuestra EDD
    def esta_vacia(self): # devolvemos True si la pila esta vacia o False si existe 1 o mas elementos dentro
        return self.size == 0
    
    def tamano(self):
        return self.size # devolvemos la cantidad de elementos dentro de la pila este numero se encuentra entre 0 o N
    
    def cima(self): #en caso de que no existan elementos dentro de la pila mostramos "La pila esta vacia"
        if self.esta_vacia():
            return "La pila esta vacia"
        else: # si existe por lo menos un elemento mostramos el elemento 1 o si hay N elemento mostramos el ultimo apilado
            return self.items[-1]
    

# inicio de las pruebas # esto es lo que ve el usuario que utiliza nuestra EDD
pila = Pila() # creamos la variable pila llamando a la clase Pila
print("La pila esta vacia?: ",pila.esta_vacia()) # mostramos por pantalla el estado actual de la pila
# al no contener elementos esta devuelve True

# comenzamos a apilar datos dentro de la pila
print("apilamos el elemento 1: ",pila.apilar(1))
print("apilamos el elemento 2: ",pila.apilar(2))
print("apilamos el elemento 6: ",pila.apilar(6))
print("apilamos el elemento 5: ",pila.apilar(5))

# mostramos el estado actual de la pila
# al contener elementos esta devuelve False
print("La pila esta vacia?: ",pila.esta_vacia())
#Mostramos el elemento que se encuentra en la cima de la pila
print("el elemento en la cima de la pila es: ",pila.cima())
# Mostramos la cantidad de elementos guardados dentro de la pila
print("hay ",pila.tamano()," elementos dentro de la pila")
# quitamos el ultimo elemento cargado en la pila.
# el ultimo en ingresar en el primero en salir
print("El elemento que desapilamos es: ",pila.desapilar())

#Mostramos el elemento que se encuentra actualmente en la cima de la pila
print("el elemento en la cima de la pila es: ",pila.cima())
# Mostramos la cantidad de elementos guardados dentro de la pila
print("hay ",pila.tamano()," elementos dentro de la pila")

#hacemos un for de 0 a 4. dentro de la pila solo tenemos 3 elementos
# cuando queremos desapilar el 4 elemento (el cual no existe) nos muestra el mensaje de "La pila esta vacia"
print("comienzo del for")
for i in range(4):
    print("El elemento que desapilamos es: ",pila.desapilar())

# la pila al ya no contener elementos al querer ver el elemento que se encuentra en la cima esta miestra "La pila esta vacia"
print("el elemento en la cima de la pila es: ",pila.cima())
# al no contener elementos dentro el tamaño de la pila es 0 
print("hay ",pila.tamano()," dentro de la pila")
# asi que al preguntarle si esta vacia esta nuvamente nos responde con True
print("La pila esta vacia?: ",pila.esta_vacia())
