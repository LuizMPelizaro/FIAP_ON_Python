from Gerador import gerador

lista_a: list[int] = gerador(10)
lista_b: list[int] = gerador(10)
lista_soma: list[int] = []
print(f'Lista a : {lista_a}\n'
      f'Lista b : {lista_b}\n')

for i in range(0, len(lista_b) + 2):
    if i % 2 == 0:
        if i < len(lista_b):
            lista_soma.append(lista_b[i] + lista_b[i + 1])
    elif i % 2 == 1:
        if i < len(lista_a):
            lista_soma.append(lista_a[i-1] + lista_a[i])

print(f'Lista intercalada : {lista_soma}')
