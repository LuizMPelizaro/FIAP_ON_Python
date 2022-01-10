from metodos import *

itens: dict = {}
escolha = opicoes()
while escolha == "I" or escolha == "E" or escolha == "P" or escolha == "D" or escolha == "X":
    if escolha == "I":
        inserir_no_invetario(itens)
    elif escolha == "E":
        exibir_inventario(itens)
    elif escolha == "P":
        pesquisar_no_inventario(int(input("Escreva a chave do item que deseja pesquisar: ")), itens)
    elif escolha == "D":
        depreciacao_de_item(int(input("Escreva a chave do item que deseja depreciar: ")), itens)
    elif escolha == "X":
        excluir_item(int(input("Escreva a chave do item que deseja execluir: ")), itens)
    escolha = opicoes()
