from Gerador import gerador

lista: list[int] = gerador(10)
maior = lista[0]
posicao_maior = -1
for x in range(0, len(lista)):
    if maior < lista[x]:
        maior = lista[x]
        posicao_maior = x

print(f'Lista: {lista}\n'
      f'Maior valor: {maior}\n'
      f'Posição do maior: {posicao_maior + 1}')
