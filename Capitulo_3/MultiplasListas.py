equipamentos = []
valores = []
numero_serial = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numero_serial.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento:"))
    resposta = input("Digite 'S' para continuar: ").upper()

# O for ira percorer o numero de indices que existir dentro do lista se for 2 ele ira no indice 0 e depois no 1
for indice in range(0, len(equipamentos)):
    print(
        f'Equipamento..: {indice + 1} '
        f'\nNome........: {equipamentos[indice]}'
        f'\nValor........: {valores[indice]}'
        f'\nNumero Serial...: {numero_serial[indice]}'
        f'\nDepartamento....: {departamentos[indice]}\n')

buscar = input("Digite o nome do equipamento que deseja checar: ")
# O for percorre todos os indices e caso ele ache o equipamento desejado ele retorna
for indice in range(0, len(equipamentos)):
    if buscar == equipamentos[indice]:
        print(f'Valor..: {valores[indice]}\n'
              f'Numero Serial.:{numero_serial[indice]}')
