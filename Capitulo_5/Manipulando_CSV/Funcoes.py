def total_voos_2014(arquivo: str) -> int:
    with open(arquivo, "r") as boston:
        total: int = 0
        for linha in boston.readlines()[1:-1]:
            total = total + int(linha.split(',')[3])
    return total


def mes_ano_ocorreu_maior_transito_aerio(arquivo: str) -> str:
    """ Função que procura o mes e o ano que ocorreu a maior taxa de transito aério"""
    with open(arquivo, "r") as boston:
        total: int = 0
        for linha in boston.readlines()[1:-1]:
            valor_linha = int(linha.split(',')[2])
            mes = int(linha.split(',')[1])
            ano = int(linha.split(',')[0])
            if total < valor_linha:
                total = valor_linha
                mes_maior = mes
                ano_maior = ano
        return f"O ano com mairo transito de passageiro foi {ano_maior} mês {mes_maior} numero de passageiros :{total}"


def numero_passageiros(arquivo: str, ano: int) -> str:
    total_passageiros: int = 0
    with open(arquivo, 'r') as boston:
        for linha in boston.readlines()[1:-1]:
            ano_dataset = int(linha.split(',')[0])
            passegeiros_dataset = int(linha.split(',')[2])
            if checa_ano(arquivo, ano):
                if ano_dataset == ano:
                    total_passageiros += passegeiros_dataset
            else:
                return f"O ano digitado não esta na base de dados"
    return f"O numero total de passageiros que passaram pelo aeroporto em {ano} foi de {total_passageiros}"


def maior_media_valor_hotel(arquivo: str, ano: int) -> str:
    """Mostra a maior media de tarifa de hotel naquele ano"""
    maior_media: float = 0
    with open(arquivo, 'r') as boston:
        for linha in boston.readlines()[1:-1]:
            if checa_ano(arquivo, ano):
                diaria_hotel: float = float(linha.split(',')[5])
                mes_dataset: int = int(linha.split(',')[1])
                ano_dataset: int = int(linha.split(',')[0])
                if diaria_hotel > maior_media and ano == ano_dataset:
                    maior_media = diaria_hotel
                    mes = mes_dataset
            else:
                return f"O ano digitado não esta na base de dados"
    return f'A maior media no ano de {ano} foi no mes de {mes} e a media foi de: {maior_media}$'


def checa_ano(arquivo: str, ano: int) -> bool:
    """Classe que checa se o ano existe na base da dados"""
    with open(arquivo, 'r') as boston:
        for linha in boston.readlines()[1:-1]:
            ano_dataset: int = int(linha.split(',')[0])
            if ano == ano_dataset:
                return True
    return False
