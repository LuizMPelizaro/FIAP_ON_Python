from Gerador import gerador

lista: list[int] = gerador(10)
lista_auxiliar: list[int] = []
rodou = 1
print(lista)

for valor in range(0, len(lista)):
    valor_a_checar: int = lista[valor]
    for checa in range(0, len(lista)):
        if lista.count(valor_a_checar) > 1:
            if valor_a_checar not in lista_auxiliar:
                lista_auxiliar.append(valor_a_checar)
            break

print(f'Os valores que se repentem {lista_auxiliar}')
