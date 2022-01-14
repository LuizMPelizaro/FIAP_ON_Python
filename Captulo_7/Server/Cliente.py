from socket import AF_INET, SOCK_STREAM, socket

# Criamos duas variaveis uma pra respresenta o servidor , caso não fosse a maquina local e outra a porta
# CUIDADO COM A PORTA POIS TEM QUE SER A MSM QUE O INICIALIZA O SERVIDOR
servidor = "127.0.0.1"
port = 43210

# O usuario passa a msg , e convertemos o conteudo dela para bytes ,
# LEMBRESSE O SOCKET SO TRANSMITE DADOS BYTE
msg: bytes = bytes(input("Digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, port))
obj_socket.send(msg)
# A resposta é limitada a 1024 bytes
resposta = obj_socket.recv(1024)
print("Recebemos: ", resposta)
# fecha a conexão
obj_socket.close()
