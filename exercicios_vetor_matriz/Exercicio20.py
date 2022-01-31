from Gerador import gerador

lista: list[int] = gerador(10)
lista_impar: list[int] = []

for i in range(0, len(lista)):
    if lista[i] % 2 != 0:
        lista_impar.append(lista[i])
print('Lista')
for i in range(0, len(lista), 2):
    print(lista[i], lista[i + 1])

print('Lista de impares')
for i in range(0, len(lista_impar), 2):
    if len(lista_impar) % 2 == 0:
        print(lista_impar[i], lista_impar[i + 1])
    elif len(lista_impar) % 2 > 0:
        if i < len(lista_impar) and i + 1 < len(lista_impar):
            print(lista_impar[i], lista_impar[i + 1])
        else:
            print(lista_impar[i])
