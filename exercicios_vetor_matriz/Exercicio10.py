from Gerador import gerador_nota

lista_de_notas: list[float] = gerador_nota(15)
media: float = 0
for valor in range(0, len(lista_de_notas)):
    media += lista_de_notas[valor]

media = media / 15

print(f'A média de notas foi de {media}')
