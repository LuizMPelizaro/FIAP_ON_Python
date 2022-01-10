def pergunta() -> str:
    opicao: str = input(f'Escolha uma das opições abaixo:\n'
                        f'<I> - Adicionar usuarios \n'
                        f'<P> - Pesquisar usuarios \n'
                        f'<E> - Excluir usuarios \n'
                        f'<L> - Listar usuarios \n').upper()
    return opicao


def inserir(dicionario: dict) -> None:
    """
    Essa função insere um usuario no sistema
    """
    # Podemos utilizar sem usar nenhuma variavel , mas o python ir resolver primeiro o que vem depois do  =
    # Entao com isso iremos cadastra em sequencia : Nome, Data de acesso , Local de acessor e a chave por ultimo
    # Nesse exemplo sera guardado em caixa alta
    codigo_lancamento: int = int(input("Insira a chave do usuario: "))
    while not chechar_chave_de_lancamento(dicionario, codigo_lancamento):
        codigo_lancamento: int = int(input("Insira uma chave valida para o usuario: "))
    dicionario[codigo_lancamento] = [input("Login: ").upper(),
                                     input("Nome do usuario: ").upper(),
                                     input("Cargo do usuario: ").upper(),
                                     input("Data do acesso: ").upper(),
                                     input("Hora do login: ").upper(),
                                     input("Local do acesso: ").upper()]


def pesquisar(chave: str, dicionario: dict):
    """
    Função que mostra ao usuario o elemento pesquisado, caso ele exista
    """
    lista: list = dicionario.get(chave)
    print("passou")
    if lista is not None:
        print(f'Nome....:{lista[0]}\n'
              f'Data de Acesso:{lista[1]}\n'
              f'Local do Acesso:{lista[2]}\n')


def excluir(chave: str, dicionario: dict):
    """
    Exclui o dicionario requisitado caso ele exista
    """
    if dicionario.get(chave) is not None:
        del dicionario[chave]
        print("Objeto excluido!!")


def listar(dicionario: dict):
    """Lista todos os elementos do dicionario"""
    # somente um print resolveria a questão mas para que o codigo seja mais agradavel irei concatenalo
    # Neste caso como o existem dois valores o chave e conteudo sera usado no for a chave e o valor
    # O que retornara a Chave e o valor
    for chave, valor in dicionario.items():
        print(f'Objetos......:\n'
              f'Chave....:{chave}\n'
              f'Dados....:{valor}')


def chechar_chave_de_lancamento(dicionario: dict, chave: int) -> bool:
    """
    Função que checa se a chave de lançamento é unica
    """
    if chave in dicionario.keys():
        print("Chave já existente!!")
        return False
    return True
