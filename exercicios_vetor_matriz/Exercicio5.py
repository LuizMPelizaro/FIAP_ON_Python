from random import randrange

lista: list[int] = []
valores_pares: int = 0
lista_valores_pares: list[int] = []
x = 0
while x < 10:
    valor = randrange(100)
    lista.append(valor)
    if lista[x] % 2 == 0:
        valores_pares += 1
        lista_valores_pares.append(lista[x])
    x += 1

print(f'Numero de valores pares na lista {valores_pares}\n'
      f'Numeros que são pares:{lista_valores_pares}')

print(lista)
