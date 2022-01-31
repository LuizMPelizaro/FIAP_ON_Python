from Gerador import gerador

lista_a: list[int] = gerador(10)
lista_b: list[int] = gerador(10)
lista_c: list[int] = []

for i in range(0, len(lista_a)):
    lista_c.append(lista_a[i] - lista_b[i])

print(f'Lista A :{lista_a}\n'
      f'Lista B :{lista_b}\n'
      f'Lista C = A-B :{lista_c}')
