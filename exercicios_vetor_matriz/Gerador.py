from random import randrange


def gerador(tamanho_lista: int, ) -> list[int]:
    x = 0
    lista: list[int] = []
    while x < tamanho_lista:
        valor = randrange(100)
        lista.append(valor)
        x += 1
    return lista
