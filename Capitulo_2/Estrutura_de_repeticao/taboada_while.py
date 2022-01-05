numero_taboada: int = int(input("Digite uma taboada que deseja ver"))
numero: int = 0
while numero <= 10:
    print(f'{numero_taboada} * {numero} = {numero_taboada * numero}')
    numero = numero + 1
