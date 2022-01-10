from funcoes.IndentificarFunçoes import *

minha_lista = []
print("Preenchendo")
preencher_inventario(minha_lista)
print("Exibindo")
exibir_inventario(minha_lista)

print("Pesquisando")
buscar_no_inventario(minha_lista)
print("Alterando")
depreciacao(minha_lista)

print("Excluindo")
print(excluir(minha_lista))

exibir_inventario(minha_lista)
