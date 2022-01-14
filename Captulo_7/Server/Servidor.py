# importa todfas as funcionabilidades da biblioteca "Socket"
from socket import socket, AF_INET, SOCK_STREAM

# A variavel servidor guarda o ip da maquina no caso o propio pc , poderia ser utilizado tambem o localhost
servidor: str = "127.0.0.1"
# A porta é um numero entra 0 e 65535 que é escolhida
# As mais famosas sendo 0 a 1023 que sao portar utilizdas por padrão
porta: int = 43210

# A objeto socket "obj_socket" , atribuido por meio da função socket , exige dois parametros
# O primeiro define a familia responsavel por identificar os pacotes
# Nesse caso a AF_INET que significa que iremos a identificação do emissor/receptor dos pacotes vio DNS ou IP
# Ja o segundo parametro refere-se ao transporte desse pacote , que poder ser SOCK_STREAM ,
# Que representara o protocolo TCP
# Ou SOCK_DGRAM que representara o protocolo UDP
obj_socket = socket(AF_INET, SOCK_STREAM)
# Aqui se fez a associação do obj_socket com o servidor e a porta
obj_socket.bind((servidor, porta))
# Nessa linha a função listen define o limite maximo de clientes em nosso server
obj_socket.listen(2)
print("Aguardando cliente....")
# Montasse dois laços infinitos .Esse primeiro aguarda a chamada do cliente , por meio da função accept
# asssim que tivermos, recebera uma tupla e ira direciona a identificação do cliente para a variavel cliente
# e a indentificão da conexao para a variavel con
while True:
    con, cliente = obj_socket.accept()
    print(f"Conectado com: {cliente}")
    # Nesse laço ,aguardando uma solicitação que pode ser transm,itida em pacotes de 1024 bytes
    # Exibiremos a msg recebida e geraremos uma msg para enviar no formato bytes , por isso a msg começa com b
    # E enviamos atraves do metodo send() e enceramos esse laço
    while True:
        msg_recebida: str = str(con.recv(1024))
        print(f"Recebemos {msg_recebida}")
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    # fechamos a conexão e aguardamos outra
    con.close()
