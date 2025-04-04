def fibonacci_recursivo(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

numero = 10
for i in range(numero):
  print(fibonacci_recursivo(i))