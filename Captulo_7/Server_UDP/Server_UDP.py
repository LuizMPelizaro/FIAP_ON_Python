from Funcoes_UDP import udp_config

servidor: str = "127.0.0.1"
porta: int = 43210

obj_socket: object = udp_config(servidor, porta)

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print(f"Origem...........: {origem}\n"
          f"Dados recebidos..: {dados.decode()}")
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()
