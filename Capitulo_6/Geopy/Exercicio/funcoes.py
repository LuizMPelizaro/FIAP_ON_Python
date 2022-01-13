import json
import os.path

from geopy.geocoders import Nominatim


def ler_arquivo(arquivo: str) -> dict:
    """
    Le o arquivo json passadoc caso ele exista e o tranforma em um dicionario.
    Caso não exista cria um dicionario vazio
    """
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as arq_json:
            localizacao: dict = json.load(arq_json)
        return localizacao
    localizacao: dict = {}
    return localizacao


def gravar_arquivo(arquivo: str, endereco: dict) -> None:
    """Grava o conteudo em um arquivo .json"""
    with open(arquivo, 'w') as arq_json:
        json.dump(endereco, arq_json)


def formatar_endereco(endereco_dict: dict) -> str:
    """Formata o endereco passado como dicionario , para um string """
    endereco_lista: list[str] = endereco_dict["endereco"]
    endereco_str: str = endereco_lista[0] + "," + endereco_lista[1] + " " + endereco_lista[2]
    return endereco_str


def capturar_cordenadas(endereco_str: str) -> dict:
    """Pega um endereco em string e o utiliza a API para tranformalo em coordenadas 'Latitude' e 'Longitude'"""
    geolocator = Nominatim(user_agent="wazeyes")
    location = geolocator.geocode(endereco_str)
    saida = {"coordenadas": (location.latitude, location.longitude)}
    return saida
