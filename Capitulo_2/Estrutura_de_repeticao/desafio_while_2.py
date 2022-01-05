nome: str = input("Digite o nome do paciente : ")
idade: int = int(input("Digite a idade do paciente : "))
sexo: str = input("Digite seu sexo : ")
doenca_ifectocontagiosa: bool = input("O paciente tem suspeita de doença contagiosa : ").upper()

while doenca_ifectocontagiosa != "SIM" and doenca_ifectocontagiosa != "NAO":
    doenca_ifectocontagiosa: bool = input("DIGITE SIM OU NÃO ").upper()

if doenca_ifectocontagiosa == 'SIM':
    print('DIRECIONE O PACIENTE PARA A ALA AMARELA')
else :
    print('DIRECIONE O PACIENTE PARA A ALA BRANCA')

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