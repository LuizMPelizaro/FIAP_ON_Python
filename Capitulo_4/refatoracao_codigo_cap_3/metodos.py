def opicoes() -> str:
    """Mostra as opições de escolha do aplicativo"""
    escolha: str = input("Escolha o que deseja fazer :\n"
                         "I - Inserir um item no inventario\n"
                         "E - Exibir inventario\n"
                         "P - Pesquisar um item do inventario\n"
                         "D - Depreciar um item do inventario\n"
                         "X - Excluir um item do inventario\n").upper()
    return escolha


def inserir_no_invetario(inventario: dict) -> None:
    """Inseri um item novo no inventario"""
    codigo_item: int = int(input("Insira a chave do item:"))
    while not checar_codigo_item(inventario, codigo_item):
        codigo_item: int = int(input("ERRO CHAVE INVALIDA\n"
                                     "Insira uma chave valida:"))
    inventario[codigo_item] = [input("Nome do item:"),
                               int(input("Valor do item:")),
                               input("Codigo de serie:"),
                               input("Departamento:")]


def exibir_inventario(inventario: dict) -> None:
    """Exibe o inventario inteiro"""
    for codigo, dados in inventario.items():
        print(f"INVENTARIO:"
              f"Codigo:{codigo}\n"
              f"Dados.:{dados}\n")


def pesquisar_no_inventario(chave_item: int, inventario: dict) -> None:
    """Exibe o item pesquisado no inventario caso ele exista"""
    if chave_item in inventario.keys():
        print(inventario.get(chave_item))
    else:
        print("ERRO !!\n"
              "ITEM NÃO ENCONTRADO")


def depreciacao_de_item(chave_item: int, inventario: dict) -> None:
    """Deprecia o i do item em 10% do i original"""
    if chave_item in inventario.keys():
        print(f"Valor antigo: {inventario[chave_item][1]}")
        inventario[chave_item][1] *= 0.9
        print(f"Novo i: {inventario[chave_item][1]}")
    else:
        print("ERRO ITEM NÃO ENCONTRADO")


def excluir_item(chave_item: int, inventario: dict) -> None:
    """Exclui o item caso ele exista"""
    if chave_item in inventario.keys():
        del inventario[chave_item]
        print("Item excluido com sucesso")
    else:
        print("ERRO ITEM NÃO ENCONTRADO")


def checar_codigo_item(inventario: dict, codigo_item: int) -> bool:
    """Checa se o codigo de item ja exite no inventario"""
    if codigo_item in inventario.keys():
        print("Codigo de item ja existente")
        return False
    return True
