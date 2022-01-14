def cadastro(dicionario: dict, key: int) -> dict:
    dicionario[key] = [input("Nome:"),
                       input("Sexo:").upper(),
                       int(input("Idade:"))]
    return dicionario


def inserir_dicionario_na_lista(dicionario: dict, lista: list[dict]) -> None:
    lista.append(dicionario)


def media_idade(lista: list[dict]) -> float:
    media: float = 0
    for pessoa in range(0, len(lista)):
        media += lista[pessoa].get(pessoa)[2]
        # print(lista[pessoa].get(pessoa)[2])
    media = media / len(lista)
    return media


def identifica_mulheres(lista: list[dict]) -> int:
    mulheres: int = 0
    for elementos in range(0, len(lista)):
        if lista[elementos].get(elementos)[1] == "FEMININO":
            mulheres += 1
    return mulheres


def idade_acima_da_media(lista: list[dict]) -> list[dict]:
    lista_pessoas_idade_acima_media = []
    media :float = media_idade(lista)
    for pessoa in range(0, len(lista)):
        if lista[pessoa].get(pessoa)[2] > media:
            lista_pessoas_idade_acima_media.append(lista[pessoa])
    return lista_pessoas_idade_acima_media
