#   Exercício Python 094 - Unindo dicionários e listas
#   Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas
#       B) A média de idade
#       C) Uma lista com as mulheres
#       D) Uma lista de pessoas com idade acima da média
from Exercicios_dicionario.Exercicio1.funcoes import *

pessoas: dict = {}
lista_pessoas: list[dict] = []
resposta: str = "S"

while resposta == "S":
    print("Insira os dados da pessoa: ")
    cadastro(pessoas)
    inserir_dicionario_na_lista(pessoas, lista_pessoas)
    resposta = input("Deseja inserir mais alguma pessoa ?").upper()

print(lista_pessoas)

print(media_idade(lista_pessoas))
print(identifica_mulheres(lista_pessoas))
print(media_idade(lista_pessoas))
print(idade_acima_da_media(lista_pessoas, media_idade(lista_pessoas)))
