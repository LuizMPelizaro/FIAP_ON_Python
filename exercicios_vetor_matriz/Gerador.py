from random import randrange, uniform


def gerador(tamanho_lista: int, ) -> list[int]:
    x = 0
    lista: list[int] = []
    while x < tamanho_lista:
        valor = randrange(10)
        lista.append(valor)
        x += 1
    return lista


def gerador_par(tamanho_lista: int) -> list[int]:
    x = 0
    lista: list[int] = []
    while x < tamanho_lista:
        valor = randrange(100)
        if valor % 2 == 0:
            lista.append(valor)
            x += 1
    return lista


def gerador_nota(tamanho_lista: int) -> list[float]:
    x = 0
    lista: list[float] = []
    while x < tamanho_lista:
        valor: float = uniform(0.0, 10)
        lista.append(valor)
        x += 1
    return lista


def gerador_numeros_reais(tamanho_lista: int) -> list[float]:
    x = 0
    lista: list[float] = []
    while x < tamanho_lista:
        valor: float = uniform(-100.0, 100.0)
        lista.append(valor)
        x += 1
    return lista
