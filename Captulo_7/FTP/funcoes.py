import os
from ftplib import FTP


def opicao() -> int:
    """Mostra o menu da aplicacão"""
    valor_opicao = int(input(
        "Escolha a opção desejada: \n"
        "<1> - Listar arquivos\n"
        "<2> - Definir um diretorio\n"
        "<3> - Baixar um arquivo:\n"))
    return valor_opicao


def conect_ftp(ftp: str) -> object:
    """Conecta ao servidor FTP caso ele exita"""
    ftp = FTP(ftp)
    print(ftp.getwelcome())
    return ftp


def login_ftp(ftp, user: str, senha: str) -> str:
    """Faz login no servidor ftp"""
    ftp.login(user, senha)
    return f"Conexão bem sucedida.\n Diretorio atual de trabalho {ftp.pwd()}"


def listar_arquivo(ftp) -> str:
    """Lista os arquivos do servidor """
    return f"{ftp.dir()}"


def definir_diretorio(ftp, endereco: str) -> str:
    """Define o diretorio caso ele exita"""
    ftp.cwd(endereco)
    return f'O diretorio corrente é: {ftp.pwd()}'


def baixa_arquivo(ftp, tipo: str, nome_arq: str) -> None:
    """Baixa o arquivo caso exista"""
    if tipo == "B":
        baixar_binario(ftp, nome_arq)
    else:
        baixar_arq_ascii(ftp, nome_arq)


def baixar_binario(ftp, nome_arquivo: str) -> str:
    """Baixa arquivo do tipo Binario"""
    with open(nome_arquivo, 'wb') as arq:
        ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
    return "Arquivo baixado com sucesso"





def baixar_arq_ascii(ftp, nome_arquivo: str) -> str:
    """Baixa arquivo do tipo ASCII"""
    def escrever_linha(data):
        arq.write(data)
        arq.write(os.linesep)
    with open(nome_arquivo, 'wb') as arq:
        ftp.retrlines('RETR ' + input("Arquivo de origem: "), escrever_linha)
    return "Arquivo baixado com sucesso"
