from socket import socket, AF_INET, SOCK_STREAM


def obj_socket_server(servidor: str, porta: int, max_cliente: int) -> object:
    var_obj_socket = socket(AF_INET, SOCK_STREAM)
    var_obj_socket.bind((servidor, porta))
    var_obj_socket.listen(max_cliente)
    return var_obj_socket


def obj_sockert_client(servidor: str, porta: int) -> object:
    var_obj_socket = socket(AF_INET, SOCK_STREAM)
    var_obj_socket.connect((servidor, porta))
    return var_obj_socket
