from Funcoes import *

usuarios: dict = {}
opicao: str = pergunta()
while opicao == "I" or opicao == "P" or opicao == "E" or opicao == "L":
    if opicao == "I":
        inserir(usuarios)

    elif opicao == "P":
        pesquisar(input("Insira a chave que deseja pesquisar: "), usuarios)

    elif opicao == "E":
        excluir(input("Digite a chave de usuario que deseja excluir: "), usuarios)

    elif opicao == "L":
        listar(usuarios)

    opicao = pergunta()
