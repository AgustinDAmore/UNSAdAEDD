lista_completa = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ","?"]

def ofuscar(corrimiento, mensaje):
    mensajeOfuscado = ""
    for letra in mensaje:
        mensajeOfuscado += lista_completa[(corrimiento+lista_completa.index(letra))%len(lista_completa)]
    return mensajeOfuscado

def desofuscar(corrimiento, mensaje):
    mensajeDesofuscado = ""
    for letra in mensaje:
        mensajeDesofuscado += lista_completa[(lista_completa.index(letra)-corrimiento)%len(lista_completa)]
    
    return mensajeDesofuscado

mensaje = "Hola Como estan?"
corrimiento = 10

print("mensaje: ",mensaje)
mensajeOfuscado = ofuscar(corrimiento, mensaje)
print(mensajeOfuscado)
mensajeDesofuscado = desofuscar(corrimiento,mensajeOfuscado)
print(mensajeDesofuscado)