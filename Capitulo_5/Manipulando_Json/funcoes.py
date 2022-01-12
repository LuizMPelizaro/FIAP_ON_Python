import json
import os.path


def ler_arquivo(arquivo: str) -> dict:
    """Le o arquivo json e caso já exista um ele o importa no dicionario"""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as arq_json:
            dicionario = json.load(arq_json)
        return dicionario
    dicionario: dict = {}
    return dicionario


def gravar_arquivo(dicionario: dict, arquivo: str) -> None:
    """Grava o dicionario em um arquivo Json"""
    with open(arquivo, 'w') as arq_json:
        json.dump(dicionario, arq_json)


def opicoes() -> int:
    """Mostra as opições de açoes do app"""
    return int(input("Escolha uma das opições:\n"
                     "<1>Para registrar um ativo\n"
                     "<2>Para exibir ativos armazenados\n"))


def registro_ativo(inventario: dict, arquivo: str) -> str:
    """Registra um ativo"""
    respota = "S"
    while respota == "S":
        inventario[input("Digite o número patrimonial:")] = [input("Descrição do ativo:"),
                                                             input("Data da ultima atualização do ativo:"),
                                                             input("Nome do derpatamento:")]
        respota = input("Deseja fazer uma nova insersão:").upper()
        gravar_arquivo(inventario, arquivo)
    return "Cadastrado com sucesso!!"


def exibir_ativos(arquivo):
    """Exibe o que esta escrito no arquivo json"""
    with open(arquivo, 'r') as arq_json:
        resultado = json.load(arq_json)
    for chave, dado in resultado.items():
        print(f"Data........:{dado[0]}\n"
              f"Descricao...:{dado[1]}\n"
              f"Departamento:{dado[2]}\n")
