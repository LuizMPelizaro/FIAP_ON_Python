usuarios: dict = {}
resp: str = "S"
emails: list = []

while resp == "S":
    emails.append(input("Digite um e-mail: ").lower())
    resp = input("Digite <S> para continuar: ").upper()

tupla: tuple = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print(f'Email: {tupla[chave][1]}')
    usuarios[tupla[chave]] = input("Digite o nome: "), input("Digite o nivel: ")

for chave, dado in usuarios.items():
    print(f'Usuario.: {chave[0]}\n'
          f'Email...: {chave[1]}\n'
          f'Nome....: {dado[0]}\n'
          f'Nível...: {dado[1]}')
