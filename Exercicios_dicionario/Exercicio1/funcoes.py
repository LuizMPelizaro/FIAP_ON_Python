def cadastro(dicionario: dict) -> dict:
    nome: str = input("Digite seu nome: ").upper()
    dicionario[nome] = [input("Sexo:").upper(),
                        int(input("Idade:"))]
    return dicionario


def inserir_dicionario_na_lista(dicionario: dict, lista: list[dict]) -> None:
    lista.append(dicionario)


def media_idade(lista: list[dict]) -> float:
    media: float = 0
    for idade in range(0, len(lista)):
        media += lista[idade].get(idade)[1]
    media = media / len(lista)
    return media


def identifica_mulheres(lista: list[dict]) -> int:
    mulheres: int = 0
    for elementos in range(0, len(lista)):
        if lista[elementos].get(elementos)[0] == "FEMININO":
            mulheres += 1
    return mulheres


def idade_acima_da_media(lista: list[dict], media: float) -> list[dict]:
    lista_pessoas_idade_acima_media = []
    for pessoa in range(0, len(lista)):
        if lista[pessoa].get(pessoa)[2] > media:
            lista_pessoas_idade_acima_media.append(lista[pessoa])
    return lista_pessoas_idade_acima_media
