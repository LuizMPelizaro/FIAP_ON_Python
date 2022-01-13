import getpass

usuario: str = input("Digite o usuario: ").upper()
senha = getpass.getpass("Digite a senha : ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuario logado !!")
else:
    print("Login negado !!")