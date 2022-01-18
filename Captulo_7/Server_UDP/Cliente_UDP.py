from Funcoes_UDP import udp_connect_cliente, enviar_msg

servidor: str = "127.0.0.1"
porta: int = 43210

obj_socket = udp_connect_cliente(servidor, porta)
saida: str = ""

while saida != "X":
    msg = enviar_msg(input("Escreva sua mensagem"), obj_socket, servidor, porta)
    print(msg)
    saida = input("Digite <X> para sair : ").upper()

obj_socket.close()
