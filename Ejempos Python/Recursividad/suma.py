def suma_recursiva(n):
  if n == 0:
    return 0
  else:
    return n + suma_recursiva(n - 1)

numero = 10
numeros = ["0"]
for i in range(numero):
    for n in range(i):
        numeros.append(str(n+1))
    resultado = suma_recursiva(i)
    cadena_suma = " + ".join(numeros[::-1])
    if(i == 0 or i == 1):
        print(f"{i} + {i} = {i+i}")
    else: 
       print(f"{cadena_suma} = {suma_recursiva(i)}")
    numeros = []