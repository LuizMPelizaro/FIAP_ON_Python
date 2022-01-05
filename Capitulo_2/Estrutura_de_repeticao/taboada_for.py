numero_taboda:int = int(input("Digite a taboada que deseja ver : "))
for numero in range(0,11,1):
    print(f'{numero} * {numero_taboda} = {numero*numero_taboda}')