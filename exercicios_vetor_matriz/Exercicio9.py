from Gerador import gerador_par

lista: list = gerador_par(6)
lista_inversa: list = []
tamanho_lista = len(lista)
for valor in range(tamanho_lista - 1, -1, -1):
    lista_inversa.append(lista[valor])
print(f'Lista normal: {lista}')
print(f'Lista inversa: {lista_inversa}')
