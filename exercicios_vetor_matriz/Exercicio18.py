from Gerador import gerador

lista: list[int] = gerador(10)
print(lista)
valor: int = int(input("Digite um dos valores do vetor"))
lista_auxiliar: list[int] = []
if valor not in lista:
    print(f'Erro não existente na lista')
else:
    for i in range(0, len(lista)):
        if lista[i] != 0 and valor % lista[i] == 0:
            lista_auxiliar.append(lista[i])
    print(f'Valores multiplos de {valor} : {lista_auxiliar}')
