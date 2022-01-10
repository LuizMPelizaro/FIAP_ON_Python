import math

lista_real: list[float] = []
lista_quadrado: list[float] = []
numero_elementos = 0

while numero_elementos < 10:
    lista_real.append(float(input("Escreva um numero real: ")))
    numero_elementos += 1

for elemento in range(0, len(lista_real)):
    lista_quadrado.append(math.pow(lista_real[elemento], 2))

print(f'Lista de numeros :{lista_real}')
print(f'Lista de numeros ao quadrado :{lista_quadrado}')
