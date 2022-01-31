lista: list[int] = []
for i in range(0, 50):
    lista.append((i + 5 * i) % (i + 1))
print(lista)
