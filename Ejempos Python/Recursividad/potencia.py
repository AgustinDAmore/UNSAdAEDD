def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

numero = 10
for i in range(numero):
    resultado_potencia = potencia_recursiva(i, i)
    print(f"({i}^{i}) = {resultado_potencia}")