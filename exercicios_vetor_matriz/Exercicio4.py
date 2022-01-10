import sys

print("Escreva oito numeros")
lista: list[int] = []
while len(lista) < 8:
    lista.append(int(input()))

X: int = int(input("Escreva o valor de um a 0 a 7 "))
Y: int = int(input("Escreva o valor de um a 0 a 7 "))
soma: int = 0
valor_posicao_x: int = -1
valor_posicao_y: int = -1
for x in range(0, len(lista)):
    if X == x:
        soma += lista[x]
        valor_posicao_x = lista[x]
    elif Y == x:
        soma += lista[x]
        valor_posicao_y = lista[x]
    elif X > 7 or Y > 7:
        print("Erro posição maior que 8")
        sys.exit()

print(f'O valor da soma da posições:\n'
      f'X : {X, valor_posicao_x}\n'
      f'Y : {Y, valor_posicao_y}\n'
      f'É igual a : {soma}')
