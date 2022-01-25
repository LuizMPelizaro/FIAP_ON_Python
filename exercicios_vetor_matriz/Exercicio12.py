from Gerador import gerador_numeros_reais

lista: list[float] = gerador_numeros_reais(6)
maior: float = -200
menor: float = 200
media: float = 0

for valor in range(0, len(lista)):
    if lista[valor] < menor:
        menor = lista[valor]
    if lista[valor] > maior:
        maior = lista[valor]
    media += lista[valor]
media = media / 6

print(f'Vetor {lista}\n'
      f'O menor valor {menor}\n'
      f'O maior valor {maior}\n'
      f'A media {media}')
