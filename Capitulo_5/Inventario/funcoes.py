def opicoes() -> int:
    """Mostra as opições de açoes do app"""
    return int(input("Escolha uma das opições:\n"
                     "<1>Para registrar um ativo\n"
                     "<2>Para persistir em arquivo\n"
                     "<3>Para exibir ativos armazenados\n"))


def registro_ativo(inventario: dict) -> str:
    """Registra um ativo"""
    inventario[input("Digite o número patrimonial:")] = [input("Descrição do ativo:"),
                                                         input("Data da ultima atualização do ativo:"),
                                                         input("Nome do derpatamento:")]
    return "cadastrado com sucesso!!"


def persitir_em_arquivo(invetario: dict) -> str:
    """Tranfere os dados do dicionario para um arquivo .csv"""
    with open("inventario.csv", "a") as inv:
        for chave, valor in invetario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "")
        return "Persistido com sucesso!!"


def exibir_ativos(arquivo) -> list[str]:
    """Exibe todos os ativos do arquivo .csv"""
    with open("inventario.csv", 'r') as inv:
        inventario: list[str] = inv.readlines()
        return inventario


def exibir_ativos_processados(arquivo):
    """Processa o exibir ativos tornando a leitura mais facil"""
    resultado = exibir_ativos(arquivo)
    for linha in resultado:
        lista = linha.split(";")
        print(f"Data........:{lista[1]}\n"
              f"Descricao...:{lista[2]}\n"
              f"Departamento:{lista[3]}")
