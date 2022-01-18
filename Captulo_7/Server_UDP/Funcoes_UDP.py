from socket import socket, AF_INET, SOCK_DGRAM


def udp_config(servidor: str, porta: int) -> object:
    # SOCK_DEGRAM mostra que sera utilizado o protocolo UDP
    obj_socket = socket(AF_INET, SOCK_DGRAM)
    # O comando bind atribui o servidor e a porta
    obj_socket.bind((servidor, porta))
    print("Servidor pronto....")
    return obj_socket


def udp_connect_cliente(servidor: str, porta: int) -> object:
    obj_socket = socket(AF_INET, SOCK_DGRAM)
    obj_socket.connect((servidor, porta))
    return obj_socket


def enviar_msg(msg: str, obj_socket: object, servidor: str, porta: int) -> str:
    obj_socket.sendto(msg.encode(), (servidor, porta))
    dados, origem = obj_socket.recvfrom(65535)
    return dados.decode()
