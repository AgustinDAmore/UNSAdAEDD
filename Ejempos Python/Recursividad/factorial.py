def factorial_recursivo(n):
  if n == 0:
    return 1
  else:
    return n * factorial_recursivo(n - 1)
  
numero = 10
numeros = ["0"]
for i in range(numero):
    for n in range(i):
        numeros.append(str(n+1))
    resultado = factorial_recursivo(i)
    cadena_suma = " * ".join(numeros[::-1])
    if(i == 0 or i == 1):
        print(f"!{i} = {factorial_recursivo(i)}")
    else: 
       print(f"!{i} = {cadena_suma} = {factorial_recursivo(i)}")
    numeros = []