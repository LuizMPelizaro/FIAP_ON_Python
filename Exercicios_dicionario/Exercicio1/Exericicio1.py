#   Exercício Python 094 - Unindo dicionários e listas
#   Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas
#       B) A média de idade
#       C) Uma lista com as mulheres
#       D) Uma lista de pessoas com idade acima da média
from Exercicios_dicionario.Exercicio1.funcoes import *

key = 0
pessoas: dict = {}
lista_pessoas: list[dict] = []
resposta: str = "S"

while resposta == "S":
    print("Insira os dados da pessoa: ")
    cadastro(pessoas, key)
    lista_pessoas.append(pessoas)
    key += 1
    # inserir_dicionario_na_lista(pessoas, lista_pessoas)
    resposta = input("Deseja inserir mais alguma pessoa ?").upper()

print(lista_pessoas)

print(f'A idade media é de: {media_idade(lista_pessoas)}')
print(f'O numero de mulheres é de: {identifica_mulheres(lista_pessoas)}')
print(
    f'As pessoas acima da idade media são: {idade_acima_da_media(lista_pessoas)}')
