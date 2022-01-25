from Gerador import gerador, gerador_numeros_reais

lista: list[float, int] = gerador_numeros_reais(5)
valor_final: int = int(input("Digite 1 para mostra o vetor em na ordem direita\n"
                             "Digite 2 para mostrar ao contrario"))
lista.append(valor_final)
lista_auxiliar: list[float, int] = []
if lista[5] == 1:
    print(f'{lista}')
elif lista[5] == 2:
    for valor in range(len(lista)-1, 0, -1):
        lista_auxiliar.append(lista[valor])
    print(lista_auxiliar)
else:
    print("Codigo invalido")
