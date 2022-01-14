from funcoes_server import obj_socket_server

servidor: str = "127.0.0.1"
port = 43210
max_cliente = 2
obj_socket: object = obj_socket_server(servidor, port, max_cliente)

print("Aguardadando cliente")

while True:
    con, cliente = obj_socket.accept()
    print(f"Conectado com: {cliente}")
    while True:
        msg_recebida = str(con.recv(1024))
        print(f"Recebemos:{str(msg_recebida)[2:-1]}")
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8')
        con.send(msg_enviada)
        break
    con.close()
