numero_elementos: int = 0
lista: list[int] = []
while numero_elementos < 6:
    lista.append(int(input("Digite um numero inteiro: ")))
    numero_elementos += 1
print(f'Lista de numeros passados: {lista}')

