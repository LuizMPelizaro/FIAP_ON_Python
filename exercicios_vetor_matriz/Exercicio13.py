from Gerador import gerador_numeros_reais

lista: list[float] = gerador_numeros_reais(6)
maior_posicao: int = 0
menor_posicao: int = 0
maior_valor: float = -200
menor_valor: float = 200

for valor in range(0, len(lista)):
    if lista[valor] < menor_valor:
        menor_posicao = valor
        menor_valor = lista[valor]
    if lista[valor] > maior_valor:
        maior_posicao = valor
        maior_valor = lista[valor]
print(f'Vetor {lista}\n'
      f'O maior valor é :{maior_valor} e sua posição é {maior_posicao}\n'
      f'O menor valor é :{menor_valor} e sua posição é {menor_posicao}')
