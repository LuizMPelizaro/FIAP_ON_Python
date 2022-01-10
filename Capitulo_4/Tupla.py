ips = {}
resp: str = "S"
while resp == "S":
    # A primeira coisa inserida é a maquina pois o python a trata com mais prioridade por esta depois do igual
    # Depois os dois octetos do ip
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois ultimos octetos: "))] = input(
        "nome da maquina: ")
    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo ip's: ")
for ip in ips.keys():
    print(f'{ip[0]}.{ip[1]}')

print("Exibindo máquinas com o mesmo endereco: ")
pesquisa = input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if ip[1] == pesquisa:
        print(nome)

print("Exibindo estações na mesma rede: ")
pesquisa = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    if ip[0] == pesquisa:
        print(nome)
