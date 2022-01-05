nome: str = input("Digite o nome do paciente : ")
idade: int = int(input("Digite a idade do paciente : "))
doenca_ifectocontagiosa: bool = input("O paciente tem suspeita de doença contagiosa : ").upper()
sexo: str = input("Digite seu sexo : ")

if doenca_ifectocontagiosa == 'SIM':
    print('DIRECIONE O PACIENTE PARA A ALA AMARELA')
elif doenca_ifectocontagiosa == 'NAO':
    print('DIRECIONE O PACIENTE PARA A ALA BRANCA')
else:
    print('Responda se há suspeita de doença contagiosa')

if idade >=65:
    print('PACIENTE COM PRIORIDADE')
else:
    if sexo == 'feminino' and idade > 10:
        gravidez: str = input("A paciente está gravida : ").upper()
        if gravidez == "SIM":
            print('PACIENTE COM PRIORIDADE')
        else:
            print('PACIENTE SEM PRIORIDADE')
    else:
        print('PACIENTE SEM PRIORIDADE')