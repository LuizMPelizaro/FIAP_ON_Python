from random import uniform

x = 0
lista: list[float] = []
while x < 10:
    valor: float = uniform(-100.0, 100.0)
    if valor < 0:
        lista.append(0)
    else:
        lista.append(valor)
    x += 1
print(lista)
