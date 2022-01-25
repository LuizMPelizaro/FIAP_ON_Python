from Gerador import gerador

lista: list[int] = gerador(20)
lista_auxiliar: list[int] = []

for valor in range(0, len(lista)):
    if lista[valor] not in lista_auxiliar:
        lista_auxiliar.append(lista[valor])

print(f'Lista com duplicidade: {lista}\n'
      f'Lista sem duplicidade: {lista_auxiliar}')

