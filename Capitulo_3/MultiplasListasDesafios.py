equipamentos = []
valores = []
numero_serial = []
departamentos = []
resposta = "S"
''
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numero_serial.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento:"))
    resposta = input("Digite 'S' para continuar: ").upper()

depreciado = input("Digite o nome do equipamento que sera depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciado == equipamentos[indice]:
        print(f'Valor atual: {valores[indice]}')
        valores[indice] = valores[indice] * 0.9
        print(f'Valor novo: {valores[indice]}')

item_danificado = int(input("Digite o numero de serie do item danificado: "))
for indice in range(0, len(numero_serial)):
    if item_danificado == numero_serial[indice]:
        del equipamentos[indice]
        del valores[indice]
        del numero_serial[indice]
        del departamentos[indice]
        # O break sera utilizado pois quando usamos o del eles deleta um indice da lista o que a quebra
        break

# O for ira percorer o numero de indices que existir dentro do lista se for 2 ele ira no indice 0 e depois no 1
for indice in range(0, len(equipamentos)):
    print(
        f'Equipamento..: {indice + 1} '
        f'\nNome........: {equipamentos[indice]}'
        f'\nValor........: {valores[indice]}'
        f'\nNumero Serial...: {numero_serial[indice]}'
        f'\nDepartamento....: {departamentos[indice]}\n')
