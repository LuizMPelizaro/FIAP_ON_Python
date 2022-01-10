from Gerador import gerador

lista: list[int] = gerador(10)
maior = lista[0]
menor = lista[0]
for x in range(0, len(lista)):
    if maior < lista[x]:
        maior = lista[x]
    elif menor >= lista[x]:
        menor = lista[x]
print(f'Lista:{lista}\n'
      f'Maior numero da lista:{maior}\n'
      f'Menor numero da lista:{menor}')
