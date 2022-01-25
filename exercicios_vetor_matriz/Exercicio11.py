from Gerador import gerador_numeros_reais

lista: list[float] = gerador_numeros_reais(10)
soma: float = 0
numeros_negativos: int = 0
for numero in range(0, len(lista)):
    if lista[numero] < 0:
        numeros_negativos += 1
    elif lista[numero] > -1:
        soma += lista[numero]

print(f'Vetor: {lista}\n'
      f'O numero de numeros negativos no vetor: {numeros_negativos}\n'
      f'O valor da soma de numeros positivos é de: {soma}')
