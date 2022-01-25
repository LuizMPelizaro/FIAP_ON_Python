from Gerador import gerador

lista: list = gerador(6)
print(lista)
fim: int = len(lista)
for item in range(fim - 1, -1, -1):
    print(lista[item])
