def divide(value_one: float, value_two: float) -> None:
    """Divide dois numeros , não executa divisão por zero"""
    try:
        result = value_one // value_two
        print(f'O i da divisão de {value_one } por {value_two} é {result}')
    except ZeroDivisionError:
        print('Você esta tentando fazer uma divisão por zero')


def abyb(a: float, b: float) -> None:
    """Executa uma função caso nao de zero o i mostra o i de C """
    try:
        c: float = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("O resultado de a/b é 0")
    else:
        print(c)


def acyc(a: float, b: float) -> None:
    """Divide dois numeros , não executa divisão por zero"""
    try:
        result = a // b
        print(f'O i da divisão  é {result}')
    except ZeroDivisionError:
        print('Você esta tentando fazer uma divisão por zero')
    finally:
        print("Função executada")
