continua = 'SIM'
while continua == "SIM":
    nivel_hieraquico: str = input("Digite seu nivel hierarquico : ").upper()
    if nivel_hieraquico == "ADM" or nivel_hieraquico == "USR":
        sexo: str = input("Digite seu sexo : ").upper()
        if nivel_hieraquico == 'USR':
            if sexo == "MASCULINO":
                print("Olá usuario")
            else:
                print("Olá usuaria")
        else:
            if sexo == "FEMININO":
                print("Olá administradora")
            else:
                print("Olá administrador")
    elif nivel_hieraquico == "GUEST":
        print("Ola visitante")
    else:
        print("Ola desconhecido(a)")
    continua = input("Deseja continuar ?? ")
